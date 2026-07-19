import streamlit as st
from src.utils import format_currency,format_months,format_number,format_percentage,format_text
from src.config import RISK_LEVEL_MAPPING
# ==========================================================
# SECTION HEADER
# ==========================================================

def create_section_header(title: str):
    st.subheader(title)
    st.divider()


# ==========================================================
# PAGE HEADER
# ==========================================================

def create_page_header(title: str, subtitle: str):
    st.title(title)
    st.caption(subtitle)


# ==========================================================
# WELCOME BANNER
# ==========================================================

def create_welcome_banner():

    with st.container(border=True):

        st.subheader("👋 Welcome")

        st.info(
            """
            This enterprise decision support system assists credit officers in
            evaluating loan applications using Machine Learning, IFRS 9
            Expected Credit Loss methodology, and Explainable AI.

            Use the navigation below to begin a new loan assessment,
            review model performance, or learn more about the application.
            """
        )


# ==========================================================
# KPI CARD
# ==========================================================

def create_metric_card(title: str, value: str, icon: str):

    with st.container(border=True):

        st.markdown(
            f"""
<div style="text-align:center">

<h1>{icon}</h1>

<p style="font-size:23px;">
{title}
</p>

<h3>{value}</h3>

</div>
""",
            unsafe_allow_html=True
        )


# ==========================================================
# SYSTEM OVERVIEW
# ==========================================================

def create_system_overview():

    create_section_header("📊 System Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        create_metric_card(
            "Customers",
            "51,246",
            "👥"
        )

    with col2:
        create_metric_card(
            "Model",
            "LightGBM",
            "🤖"
        )

    with col3:
        create_metric_card(
            "Risk Grades",
            "P1 - P4",
            "📈"
        )

    with col4:
        create_metric_card(
            "IFRS 9",
            "Score System",
            "🏦"
        )


# ==========================================================
# QUICK ACTIONS
# ==========================================================

def create_quick_actions():
    st.divider()

    st.subheader("🚀 Quick Actions")
    st.caption("Navigate to the major modules of the application.")
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):

            st.markdown("### 📝 Loan Assessment")

            st.write(
                "Evaluate a loan application using Machine Learning and IFRS 9."
            )

            if st.button(
                "Open Assessment",
                use_container_width=True
            ):
                st.switch_page("pages/Loan_Assessment.py")

    with col2:
        with st.container(border=True):

            st.markdown("### 📈 Model Performance")

            st.write(
                "Review evaluation metrics, SHAP explainability and model insights."
            )

            if st.button(
                "View Performance",
                use_container_width=True
            ):
                st.switch_page("pages/Model_Performance.py")

    with col3:
        with st.container(border=True):

            st.markdown("### ℹ️ About")

            st.write(
                "Explore the business problem, architecture and technology stack."
            )

            if st.button(
                "Learn More",
                use_container_width=True
            ):
                st.switch_page("pages/About.py")


# ==========================================================
# BUSINESS WORKFLOW
# ==========================================================

def create_business_workflow():

    create_section_header("🏦 Business Workflow")

    with st.expander(
        "View Complete Workflow",
        expanded=True
    ):

        st.markdown("""
1. Search Customer

⬇️

2. Retrieve Customer Profile

⬇️

3. Enter Loan Details

⬇️

4. Predict Risk Grade (P1-P4)

⬇️

5. Calculate PD, LGD, EAD

⬇️

6. Calculate Expected Credit Loss

⬇️

7. Generate Lending Decision

⬇️

8. Download Credit Risk Report
""")


# ==========================================================
# PROJECT HIGHLIGHTS
# ==========================================================

def create_project_highlights():
    st.divider()
    create_section_header("⭐ Key Features")

    col1, col2 = st.columns(2)

    with col1:

        st.success("AI Risk Prediction")

        st.success("IFRS 9 Compliant")

        st.success("Expected Credit Loss")

    with col2:

        st.success("SHAP Explainability")

        st.success("Decision Support")

        st.success("Enterprise Dashboard")


# ==========================================================
# FOOTER
# ==========================================================

def create_footer():

    st.divider()

    st.caption(
        "RiskLens | IFRS 9 Credit Risk & ECL Platform | Developed by Pradhuman Kumar Soni"
    )

# ==========================================================
# Customer Search
# ==========================================================

def create_customer_search():
    """
    Render the customer search section.

    Returns
    -------
    tuple
        applicant_id (str), search_clicked (bool)
    """

    st.subheader("🔍 Applicant Data Search")

    applicant_id = st.text_input(
    "Applicant ID",
    key="search_applicant",
    placeholder="e.g., APP1234 for ApplicantID = 1234",
    help = "Enter a Unique Applicant ID"
)

    search_clicked = st.button(
        "Search Customer",
        type="primary",
        use_container_width=True
    )

    return applicant_id, search_clicked

# ==========================================================
# Create Customer Profile
# ==========================================================

import streamlit as st


def create_customer_profile(customer):

    st.divider()
    st.subheader("👤 Applicant Profile")

    left, right = st.columns(2)

    # =====================================================
    # LEFT COLUMN
    # =====================================================

    with left:

        # -----------------------------
        # Personal Information
        # -----------------------------
        with st.container(border=True):

            st.markdown("### 👤 Personal Information")

            info_row("Applicant ID", customer["Applicant ID"])
            info_row("Gender", customer["Gender"])
            info_row("Education", format_text(customer["Education"]))
            info_row("Marital Status", customer["Marital Status"])
            info_row("Monthly Income", customer["Monthly Income (₹)"])
            info_row("Latest Employment Duration", customer["Employment Duration (Months)"])

        # -----------------------------
        # Credit Behaviour
        # -----------------------------
        with st.container(border=True):

            st.markdown("### 📊 Credit Behaviour")

            info_row(
                "Oldest Credit Line Age",
                format_months(customer["Oldest Credit Line (Months)"])
            )

            info_row(
                "Newest Credit Line Age",
                format_months(customer["Newest Credit Line (Months)"])
            )

            info_row(
                "Months Since Last Payment",
                format_months(customer["Months Since Last Payment"])
            )

            info_row(
                "Months Since Last Credit Enquiry",
                format_months(customer["Months Since Last Credit Enquiry"])
            )

        # -----------------------------
        # Credit Enquiries
        # -----------------------------
        with st.container(border=True):

            st.markdown("### 🔍 Credit Enquiries")

            info_row(
                "Credit Enquiries (Last 3 Months)",
                format_number(customer["Credit Enquiries (Last 3 Months)"])
            )

            info_row(
                "Credit Card Enquiries (12 Months)",
                format_number(customer["Credit Card Enquiries (12 Months)"])
            )

            info_row(
                "Personal Loan Enquiries (12 Months)",
                format_number(customer["Personal Loan Enquiries (12 Months)"])
            )

    # =====================================================
    # RIGHT COLUMN
    # =====================================================

    with right:

        # -----------------------------
        # Credit Portfolio
        # -----------------------------
        with st.container(border=True):

            st.markdown("### 💳 Credit Portfolio")

            info_row(
                "Home Loan Accounts",
                customer["Home Loan Accounts"]
            )

            info_row(
                "Personal Loan Accounts",
                customer["Personal Loan Accounts"]
            )

            info_row(
                "Credit Card Accounts",
                customer["Credit Card Accounts"]
            )

            info_row(
                "Secured Loan Accounts",
                customer["Secured Loan Accounts"]
            )

            info_row(
                "Unsecured Loan Accounts",
                customer["Unsecured Loan Accounts"]
            )

            info_row(
                "Other Loan Accounts",
                customer["Other Loan Accounts"]
            )

            info_row(
                "Total Active Loan Accounts",
                customer["Total Active Loan Accounts"]
            )

        # -----------------------------
        # Repayment Behaviour
        # -----------------------------
        with st.container(border=True):

            st.markdown("### ⚠️ Repayment Behaviour")

            info_row(
                "Total Missed Payments",
                customer["Total Missed Payments"]
            )

            info_row(
                "Current Delinquency Level",
                customer["Current Delinquency Level"]
            )

            info_row(
                "Highest Recent Delinquency",
                customer["Highest Recent Delinquency"]
            )

            info_row(
                "60+ DPD Occurrences",
                customer["60+ DPD Occurrences"]
            )

        # -----------------------------
        # Exposure Summary
        # -----------------------------
        with st.container(border=True):

            st.markdown("### 💰 Exposure Summary")

            info_row(
                "Current Balance Ratio",
                customer["Current Balance Ratio (%)"]
            )

            info_row(
                "Maximum Unsecured Exposure",
                customer["Maximum Unsecured Exposure (%)"]
            )


# ==========================================================
# Row-wise Customer Data Display
# ==========================================================

def info_row(label, value):
    """
    Display a single information row in banking style.
    """

    col1, col2 = st.columns([2.4, 2])

    with col1:
        st.markdown(
            f"<span style='font-weight:600;'>{label}</span>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(str(value))

# ==========================================================
# Create loan Form
# ==========================================================

import streamlit as st


def create_loan_form():
    """
    Loan details entered by the credit officer.
    """

    st.subheader("💰 Loan Proposal")

    col1, col2 = st.columns(2)

    with col1:
        loan_amount = st.number_input(
            "Requested Loan Amount (₹)",
            min_value=50000.0,
            step=50000.0
        )

    with col2:
        

        collateral = st.number_input(
            "Collateral Value (₹)",
            min_value=0.0,
            step=10000.0
        )
    return {
        "loan_amount": loan_amount,
        "collateral": collateral
    }

# ==========================================================
# Generate Button
# ==========================================================

def create_generate_button():

    st.divider()

    return st.button(
        "🚀 Generate Risk Assessment",
        type="primary",
        use_container_width=True
    )


# ==========================================================
# Creating Risk Summary After Model Running On Applicant ID
# ==========================================================


def create_risk_summary_card(risk_grade):

    st.divider()

    st.subheader("🤖 Current Credit Risk Assessment")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Risk Grade",
            risk_grade
        )

    with col2:
        st.metric(
            "Risk Level",
            RISK_LEVEL_MAPPING[risk_grade]
        )

# ==========================================================
# IFRS 9 ASSESSMENT SUMMARY
# ==========================================================

def create_ifrs9_summary(report: dict):
    """
    Display the IFRS 9 assessment using native Streamlit components.
    """

    st.divider()
    st.header("📉 IFRS 9 Risk Assessment")

    # ==========================================================
    # BORROWER RISK
    # ==========================================================

    with st.container(border=True):

        st.subheader("👤 Borrower Risk")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Risk Grade", report["Risk Grade"])

        with c2:
            st.metric("Risk Level", report["Risk Level"])

        with c3:
            st.metric("IFRS Stage", report["IFRS Stage"])

    # ==========================================================
    # LOAN DETAILS
    # ==========================================================

    with st.container(border=True):

        st.subheader("💰 Loan Details")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Loan Amount", report["Loan Amount"])

        with c2:
            st.metric("Collateral Value", report["Collateral Value"])

        with c3:
            st.metric("Coverage", report["Collateral Coverage"])

    # ==========================================================
    # IFRS 9 METRICS
    # ==========================================================

    with st.container(border=True):

        st.subheader("📊 IFRS 9 Metrics")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("PD", report["PD"])

        with c2:
            st.metric("LGD", report["LGD"])

        with c3:
            st.metric("EAD", report["EAD"])

        with c4:
            st.metric("Loss Ratio", report["Loss Ratio"])

    # ==========================================================
    # EXPECTED CREDIT LOSS
    # ==========================================================

    with st.container(border=True):

        st.subheader("💸 Expected Credit Loss")

        st.metric(
            label="Expected Credit Loss (ECL)",
            value=report["ECL"]
        )

    # ==========================================================
    # DECISION
    # ==========================================================

    st.divider()
    st.header("🏦 Lending Decision")

    decision = report["Decision"]

    if "Reject" in decision or "Decline" in decision:

        st.error(f"❌ {decision}")

    elif "Manual" in decision:

        st.warning(f"🟡 {decision}")

    elif "Monitor" in decision:

        st.info(f"🔵 {decision}")

    else:

        st.success(f"✅ {decision}")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("📅 Monitoring")

            st.write(report["Monitoring"])

    with col2:

        with st.container(border=True):

            st.subheader("📝 Reason")

            st.write(report["Reason"])


    # ==========================================================
    # CREDIT DECISION SCORE
    # ==========================================================

    with st.container(border=True):

        st.subheader("📊 Credit Decision Score")

        st.metric(
            "Overall Score",
            f"{report['Decision Score']} / 100"
        )

        st.progress(report["Decision Score"] / 100)
        if report["Decision Score"] >= 85:

            st.success("Excellent Credit Profile")

        elif report["Decision Score"] >= 70:

            st.info("Good Credit Profile")

        elif report["Decision Score"] >= 55:

            st.warning("Moderate Credit Profile")

        else:

            st.error("High Credit Risk")

        st.divider()

        # ======================================================
        # SECTION SCORES
        # ======================================================

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Borrower Risk",
                f"{report['Borrower Risk Score']} / 40"
            )

        with c2:
            st.metric(
                "Loan Structure",
                f"{report['Loan Structure Score']} / 30"
            )

        with c3:
            st.metric(
                "Expected Loss",
                f"{report['Expected Loss Score']} / 30"
            )

        # ======================================================
        # BORROWER RISK
        # ======================================================

        with st.expander("👤 Borrower Risk Assessment"):

            st.markdown("#### Risk Grade")

            st.write(
               f" {risk_grade_status(report['Risk Grade'])}  ({report['Risk Level']})"
            )

            st.caption(
                f"Score: {report['Risk Grade Score']} / 20"
            )

            st.divider()

            st.markdown("#### IFRS Stage")

            st.write(
                f"{ifrs_status(report['IFRS Stage'])}"
            )

            st.caption(
                f"Score: {report['Stage Score']} / 10"
            )

            st.divider()

            st.markdown("#### Probability of Default")

            st.write(
                report["PD"]
            )

            st.caption(
                f"Score: {report['PD Score']} / 10"
            )

        # ======================================================
        # LOAN STRUCTURE
        # ======================================================

        with st.expander("💰 Loan Structure Assessment"):

            st.markdown("#### Collateral Coverage")
            st.write(collateral_status(report["Collateral Score"]))
            st.caption(f"Score: {report['Collateral Score']} / 15")

            st.divider()

            st.markdown("#### Loss Given Default")
            st.write(lgd_status(report["LGD Score"]))
            st.caption(f"Score: {report['LGD Score']} / 10")

            st.divider()

            st.markdown("#### Loan Exposure")
            st.write(exposure_status(report["Loan Amount Score"]))
            st.caption(f"Score: {report['Loan Amount Score']} / 5")

        # ======================================================
        # EXPECTED LOSS
        # ======================================================

        with st.expander("📉 Expected Loss Assessment"):

            st.markdown("#### Expected Credit Loss")

            st.write(
                ecl_status(
                    report["ECL Score"]
                )
            )

            st.caption(
                f"Score: {report['ECL Score']} / 20"
            )

            st.divider()

            st.markdown("#### Loss Ratio")

            st.write(
                loss_ratio_status(
                    report["Loss Ratio Score"]
                )
            )

            st.caption(
                f"Score: {report['Loss Ratio Score']} / 10"
            )


    


# =====================================================
# Section Header Function
# =====================================================

def section_header(title):

    st.markdown(

        f"""

<div class="section-box">

<div class="section-title">

{title}

</div>

<div class="section-divider"></div>

""",

        unsafe_allow_html=True

    )


# =====================================================
# End Section
# =====================================================

def end_section():

    st.markdown(

        "</div>",

        unsafe_allow_html=True

    )

# =====================================================
# Assessment Card For What if Analysis
# =====================================================


def assessment_card(
    title: str,
    proposal: dict,
    report: dict,
    formatted: dict,
    score_delta: int | None = None,
):
    """
    Render a professional credit assessment card.
    """

    with st.container(border=True):

        st.markdown(f"## {title}")

        # =====================================
        # Loan Proposal
        # =====================================

        st.markdown("### 🏦 Loan Proposal")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Loan Amount",
                f"₹{proposal['loan_amount']:,.0f}"
            )

        with c2:
            st.metric(
                "Collateral",
                f"₹{proposal['collateral']:,.0f}"
            )

        coverage = (
            proposal["collateral"]
            / proposal["loan_amount"]
        ) * 100

        st.metric(
            "Collateral Coverage",
            f"{coverage:.1f}%"
        )

        st.divider()

        # =====================================
        # Risk Assessment
        # =====================================

        st.markdown("### 📊 Risk Assessment")

        st.metric(
            "Risk Grade",
            formatted["Risk Grade"],
            formatted["Risk Level"]
        )

        st.metric(
            "IFRS Stage",
            formatted["IFRS Stage"]
        )

        r1, r2 = st.columns(2)

        with r1:

            st.metric(
                "Probability of Default",
                formatted["PD"]
            )

        with r2:

            st.metric(
                "Loss Given Default",
                formatted["LGD"]
            )

        st.divider()

        # =====================================
        # Lending Decision
        # =====================================

        st.markdown("### ✅ Lending Decision")

        if score_delta is None:

            st.metric(
                "Overall Credit Score",
                f"{report['Decision Score']:.0f}/100"
            )

        else:

            st.metric(
                "Overall Credit Score",
                f"{report['Decision Score']:.0f}/100",
                delta=f"{score_delta:+.0f}"
            )

        st.metric(
            "Expected Credit Loss",
            formatted["ECL"]
        )

        decision = formatted["Decision"]

        if decision == "Approve":
            st.success(decision)

        elif decision == "Approve with Monitoring":
            st.info(decision)

        elif decision == "Additional Collateral Required":
            st.warning(decision)

        else:
            st.error(decision)


# ==========================================================
# BUSINESS LABELS
# ==========================================================

def collateral_status(score):

    if score >= 13:
        return "🟢 Excellent Security"

    elif score >= 10:
        return "🟢 Good Security"

    elif score >= 6:
        return "🟡 Moderate Security"

    elif score >= 2:
        return "🟠 Weak Security"

    return "🔴 Unsecured"


def risk_grade_status(score):

    if score == "P1":
        return "🟢 P1"

    elif score == "P2":
        return "🟡 P2"

    elif score == "P3":
        return "🟠 P3"

    elif score == "P4":
        return "🔴 P4"


def ifrs_status(score):

    if score == "Stage 1":
        return "🟢 Stage 1"

    elif score == "Stage 2":
        return "🟡 Stage 2 "

    elif score == "Stage 3":
        return "🔴 Stage 3"



def lgd_status(score):

    if score >= 10:
        return "🟢 Very Low Loss Severity"

    elif score >= 8:
        return "🟢 Low Loss Severity"

    elif score >= 5:
        return "🟡 Moderate Loss Severity"

    elif score >= 2:
        return "🟠 High Loss Severity"

    return "🔴 Severe Loss Severity"


def exposure_status(score):

    if score >= 5:
        return "🟢 Very Small Exposure"

    elif score >= 4:
        return "🟢 Small Exposure"

    elif score >= 3:
        return "🟡 Moderate Exposure"

    elif score >= 2:
        return "🟠 High Exposure"

    return "🔴 Very High Exposure"


def ecl_status(score):

    if score >= 20:
        return "🟢 Very Low Expected Loss"

    elif score >= 16:
        return "🟢 Low Expected Loss"

    elif score >= 12:
        return "🟡 Moderate Expected Loss"

    elif score >= 8:
        return "🟠 High Expected Loss"

    return "🔴 Very High Expected Loss"


def loss_ratio_status(score):

    if score >= 10:
        return "🟢 Minimal Portfolio Impact"

    elif score >= 8:
        return "🟢 Low Portfolio Impact"

    elif score >= 6:
        return "🟡 Moderate Portfolio Impact"

    elif score >= 3:
        return "🟠 High Portfolio Impact"

    return "🔴 Severe Portfolio Impact"


