# ==========================================================
# IMPORTS
# ==========================================================

import streamlit as st

from src.utils import (
    load_css,
    search_customer_profile,
    search_customer_features
)

from src.components import (
    create_page_header,
    create_customer_search,
    create_customer_profile,
    create_loan_form,
    create_generate_button,
    create_risk_summary_card,
    create_ifrs9_summary,
    assessment_card
)

from src.prediction import (
    predict_risk,
    predict_probability,
    map_risk_grade,
    run_credit_assessment
)

from IFRS9_engine import (
    generate_risk_report,
    format_risk_report
)




# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

load_css()

# ==========================================================
# SESSION STATE
# ==========================================================

defaults = {
    "current_applicant": None,
    "current_profile": None,
    "current_features": None,
    "current_risk": None,
    "current_report": None
}

if "original_loan" not in st.session_state:
    st.session_state.original_loan = None

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


if "what_if_mode" not in st.session_state:
    st.session_state.what_if_mode = False



# ==========================================================
# PAGE HEADER
# ==========================================================

create_page_header(
    "📝 New Loan Assessment",
    "AI-powered Credit Risk Evaluation"
)


# ==========================================================
# CUSTOMER SEARCH
# ==========================================================

applicant_id, search_clicked = create_customer_search()

if search_clicked: 
    with st.spinner("🔍 Retrieving customer profile..."):

        customer_profile = search_customer_profile(applicant_id)
        customer_features = search_customer_features(applicant_id)

        if customer_profile is None or customer_features is None :
            st.error("Applicant ID not found.")

        else:


            predicted_class = predict_risk(customer_features)
            risk_grade = map_risk_grade(predicted_class)

            st.session_state.current_applicant = applicant_id
            st.session_state.current_profile = customer_profile
            st.session_state.current_features = customer_features
            st.session_state.current_risk = risk_grade

            st.session_state.current_report = None
            st.success("Customer profile loaded successfully.")


# ==========================================================
# DISPLAY CUSTOMER INFORMATION
# ==========================================================

if st.session_state.current_profile is not None:

    create_customer_profile(
        st.session_state.current_profile
    )

    create_risk_summary_card(
        st.session_state.current_risk
    )


# ==========================================================
# LOAN DETAILS
# ==========================================================


loan_data = create_loan_form()



# ==========================================================
# GENERATE IFRS 9 ASSESSMENT
# ==========================================================

generate = create_generate_button()

if (
    generate
    and st.session_state.current_profile is not None
):
    
    report = run_credit_assessment(
    applicant_id=st.session_state.current_applicant,
    risk_grade=st.session_state.current_risk,
    loan_data=loan_data
)

    st.session_state.current_report = report

    # Freeze the original proposal
    st.session_state.original_loan = loan_data.copy()

    st.session_state.current_report_raw = report
    st.session_state.current_report = format_risk_report(report)


if st.session_state.current_report is not None:

    create_ifrs9_summary(
    st.session_state.current_report
)
    if not st.session_state.what_if_mode:

        if st.button(
            "🔄 What-If Analysis",
            use_container_width=True
        ):
            st.session_state.what_if_mode = True
            st.rerun()
    

#================================================================================
# What-If Analysis
#================================================================================
if (
    st.session_state.what_if_mode
    and st.session_state.original_loan is not None
):

    st.divider()

    st.subheader("🔄 What-If Analysis")

    left, right = st.columns(2)

    loan = st.session_state.original_loan

    with left:

        st.markdown("### Current Proposal")

        st.metric(
        "Loan Amount",
        f"₹{loan['loan_amount']:,.0f}"
    )

        st.metric(
            "Collateral Value",
            f"₹{loan['collateral']:,.0f}"
    )

    with right:

        st.markdown("### Alternative Proposal")

        new_loan_amount = st.number_input(
            "Loan Amount (₹)",
            value=float(loan["loan_amount"]),
            min_value=0.0,
            step=50000.0,
            key="whatif_loan_amount"
        )

        if new_loan_amount <= 0:
            st.error("Loan amount must be greater than zero.")
            st.stop()


        new_collateral = st.number_input(
            "Collateral Value (₹)",
            value=float(loan["collateral"]),
            min_value=0.0,
            step=10000.0,
            key="whatif_collateral"
        )


    # Comaparison Button + Code    

    st.divider()

    compare = st.button(
        "📊 Compare Scenarios",
        type="primary",
        use_container_width=True
    )

    if compare:
        
        original_report = run_credit_assessment(
            applicant_id=st.session_state.current_applicant,
            risk_grade=st.session_state.current_risk,
            loan_data=st.session_state.original_loan
        )
        original_display = format_risk_report(original_report)

        new_loan = {
            "loan_amount": new_loan_amount,
            "collateral": new_collateral
        }

        alternative_report = run_credit_assessment(
            applicant_id=st.session_state.current_applicant,
            risk_grade=st.session_state.current_risk,
            loan_data=new_loan
        )
        alternative_display = format_risk_report(alternative_report)

        # ==========================================
        # Calculate comparison metrics
        # ==========================================

        score_diff = (
            alternative_report["Decision Score"]
            - original_report["Decision Score"]
        )

        ecl_diff = (
            alternative_report["ECL"]
            - original_report["ECL"]
        )

        lgd_diff = (
            alternative_report["LGD"]
            - original_report["LGD"]
        )

        pd_diff = (
            alternative_report["PD"]
            - original_report["PD"]
        )

        coverage_original = (
            st.session_state.original_loan["collateral"]
            / st.session_state.original_loan["loan_amount"]
        ) * 100

        coverage_alternative = (
            new_loan["collateral"]
            / new_loan["loan_amount"]
        ) * 100

        coverage_diff = (
            coverage_alternative
            - coverage_original
        )

        st.success("Comparison executed successfully!")

        st.subheader("📊 Scenario Comparison")

        left, right = st.columns(2)

        with left:

            assessment_card(
                title="Current Assessment",
                proposal=st.session_state.original_loan,
                report=original_report,
                formatted=original_display
            )

        with right:

            assessment_card(
                title="Alternative Assessment",
                proposal=new_loan,
                report=alternative_report,
                formatted=alternative_display,
                score_delta=score_diff
            )

        # ==========================================================
        # BUSINESS IMPACT SUMMARY
        # ==========================================================

        st.subheader("📌 Business Impact Summary")

        loan_original = st.session_state.original_loan["loan_amount"]
        loan_new = new_loan["loan_amount"]

        coll_original = st.session_state.original_loan["collateral"]
        coll_new = new_loan["collateral"]

        coverage_original = (coll_original / loan_original) * 100
        coverage_new = (coll_new / loan_new) * 100

        score_diff = alternative_report["Decision Score"] - original_report["Decision Score"]

        # ----------------------------------------------------------
        # Build Dynamic Narrative
        # ----------------------------------------------------------

        intro = ""

        if loan_new > loan_original and coll_new == coll_original:

            intro = (
                f"The requested loan amount increased from **₹{loan_original:,.0f}** "
                f"to **₹{loan_new:,.0f}**, while the collateral value remained unchanged. "
                "This increased the bank's credit exposure without improving the available security."
            )

        elif loan_new > loan_original and coll_new > coll_original:

            intro = (
                f"The requested loan amount increased from **₹{loan_original:,.0f}** "
                f"to **₹{loan_new:,.0f}**. The borrower also increased the collateral "
                f"from **₹{coll_original:,.0f}** to **₹{coll_new:,.0f}**, partially offsetting the additional exposure."
            )

        elif loan_new == loan_original and coll_new > coll_original:

            intro = (
                f"The requested loan amount remained unchanged while the collateral "
                f"increased from **₹{coll_original:,.0f}** to **₹{coll_new:,.0f}**. "
                "This strengthened the bank's security position."
            )

        elif loan_new == loan_original and coll_new < coll_original:

            intro = (
                f"The requested loan amount remained unchanged, but the collateral "
                f"decreased from **₹{coll_original:,.0f}** to **₹{coll_new:,.0f}**, "
                "reducing the security available against the loan."
            )

        elif loan_new < loan_original:

            intro = (
                f"The requested loan amount decreased from **₹{loan_original:,.0f}** "
                f"to **₹{loan_new:,.0f}**, reducing the bank's overall credit exposure."
            )

        else:

            intro = (
                "The proposed loan structure remained materially unchanged."
            )

        # ----------------------------------------------------------
        # Risk Impact
        # ----------------------------------------------------------

        risk = (
            f"As a consequence, collateral coverage changed from "
            f"**{coverage_original:.1f}%** to **{coverage_new:.1f}%**. "
            f"This changed the **Loss Given Default (LGD)** from "
            f"**{original_display['LGD']}** to **{alternative_display['LGD']}**, "
            f"and the **Expected Credit Loss (ECL)** from "
            f"**{original_display['ECL']}** to **{alternative_display['ECL']}**."
        )

        # ----------------------------------------------------------
        # Credit Score
        # ----------------------------------------------------------

        if score_diff < 0:

            score_text = (
                f"The Overall Credit Score decreased by **{abs(score_diff):.0f} points**, "
                "indicating a decrease in chance of getting a loan approval with new loan data"
            )

        elif score_diff > 0:

            score_text = (
                f"The Overall Credit Score improved by **{score_diff:.0f} points**, "
                "indicating an increase in chance of getting a loan approval with new loan data."
            )

        else:

            score_text = (
                "The Overall Credit Score remained unchanged."
            )

        # ----------------------------------------------------------
        # Display Summary
        # ----------------------------------------------------------

        st.markdown("### Assessment Summary")

        st.markdown(
            intro +
            "\n\n" +
            risk +
            "\n\n" +
            score_text
        )

        # ----------------------------------------------------------
        # Final Decision
        # ----------------------------------------------------------

        if original_display["Decision"] != alternative_display["Decision"]:

            st.warning(
                f"""
        ### Final Credit Decision

        **{original_display['Decision']}**
        &nbsp;&nbsp;⬇️
        **{alternative_display['Decision']}**

        The change in loan structure materially affected the bank's risk profile,
        resulting in an updated lending recommendation.
        """
            )

        else:

            st.success(
                f"""
        ### Final Credit Decision

        **{alternative_display['Decision']}**

        Although the proposal changed, the overall lending recommendation remains unchanged.
        """
            )

