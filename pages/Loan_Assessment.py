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
    create_ifrs9_summary
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
    customer_profile = search_customer_profile(applicant_id)
    customer_features = search_customer_features(applicant_id)

    if customer_profile is None:

        st.error("Applicant ID not found.")

    else:


        predicted_class = predict_risk(customer_features)
        risk_grade = map_risk_grade(predicted_class)

        st.session_state.current_applicant = applicant_id
        st.session_state.current_profile = customer_profile
        st.session_state.current_features = customer_features
        st.session_state.current_risk = risk_grade

        st.session_state.current_report = None


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

    report = format_risk_report(report)

    st.session_state.current_report = report


if st.session_state.current_report is not None:

    create_ifrs9_summary(
    st.session_state.current_report
)
    

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
            "Interest Rate",
            f"{loan['interest_rate']:.2f}%"
        )

        st.metric(
            "Loan Tenure",
            f"{loan['tenure']} Years"
        )

        st.metric(
            "Collateral",
            f"₹{loan['collateral']:,.0f}"
        )

        st.metric(
            "Loan Type",
            loan["loan_type"]
        )

    with right:

        st.markdown("### Alternative Proposal")

        new_loan_amount = st.number_input(
            "Loan Amount (₹)",
            value=float(loan["loan_amount"]),
            step=10000.0,
            key="whatif_loan_amount"
        )

        new_interest_rate = st.number_input(
            "Interest Rate (%)",
            value=float(loan["interest_rate"]),
            step=0.25,
            key="whatif_interest"
        )

        new_tenure = st.number_input(
            "Loan Tenure (Years)",
            value=int(loan["tenure"]),
            key="whatif_tenure"
        )

        new_collateral = st.number_input(
            "Collateral Value (₹)",
            value=float(loan["collateral"]),
            step=10000.0,
            key="whatif_collateral"
        )

        loan_types = [
    "Home Loan",
    "Personal Loan",
    "Vehicle Loan",
    "Education Loan",
    "Business Loan"
]

        new_loan_type = st.selectbox(
            "Loan Type",
            loan_types,
            index=loan_types.index(loan["loan_type"]),
            key="whatif_loan_type"
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

    new_loan = {
        "loan_amount": new_loan_amount,
        "interest_rate": new_interest_rate,
        "loan_type": new_loan_type,
        "tenure": new_tenure,
        "collateral": new_collateral
    }

    alternative_report = run_credit_assessment(
        applicant_id=st.session_state.current_applicant,
        risk_grade=st.session_state.current_risk,
        loan_data=new_loan
    )

    st.success("Comparison executed successfully!")

    comparison = {
    "Metric": [
        "Risk Grade",
        "IFRS Stage",
        "PD",
        "LGD",
        "ECL",
        "Decision Score",
        "Recommendation"
    ],

    "Current": [
        original_report["Risk Grade"],
        original_report["IFRS Stage"],
        original_report["PD"],
        original_report["LGD"],
        original_report["ECL"],
        original_report["Decision Score"],
        original_report["Decision"]
    ],

    "Alternative": [
        alternative_report["Risk Grade"],
        alternative_report["IFRS Stage"],
        alternative_report["PD"],
        alternative_report["LGD"],
        alternative_report["ECL"],
        alternative_report["Decision Score"],
        alternative_report["Decision"]
    ]
}

    st.subheader("📊 Scenario Comparison")

    st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
    )

    st.subheader("📌 Impact Summary")
    if original_report["Decision"] != alternative_report["Decision"]:
        st.warning(
            f"Recommendation changed from "
            f"**{original_report['Decision']}** "
            f"to "
            f"**{alternative_report['Decision']}**."
        )
    else:
        st.success(
            "The lending recommendation remains unchanged."
        )

    score_diff = (
    alternative_report["Decision Score"]
    - original_report["Decision Score"]
)

    if score_diff > 0:
        st.success(f"Decision Score improved by {score_diff} points.")
    elif score_diff < 0:
        st.error(f"Decision Score decreased by {abs(score_diff)} points.")
    else:
        st.info("Decision Score remains unchanged.")

