import streamlit as st


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

    st.info(
        """
### Welcome

Welcome to the **Enterprise AI Credit Risk Management System**.

This application helps bank credit officers evaluate loan applications
using Machine Learning and IFRS 9 Expected Credit Loss methodology.
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

<p style="font-size:15px;">
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
            "Enabled",
            "🏦"
        )


# ==========================================================
# QUICK ACTIONS
# ==========================================================

def create_quick_actions():

    create_section_header("🚀 Quick Actions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📝 New Loan Assessment",
            use_container_width=True
        ):
            st.switch_page("pages/Loan_Assessment.py")

    with col2:

        if st.button(
            "📈 Portfolio Analytics",
            use_container_width=True
        ):
            st.switch_page("pages/Portfolio_Analytics.py")


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

    create_section_header("⭐ Project Highlights")

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
        "Developed by Pradhuman Kumar Soni | Enterprise AI Credit Risk Management System"
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

    st.subheader("🔍 Customer Search")

    applicant_id = st.text_input(
    "Applicant ID",
    key="search_applicant"
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
    st.subheader("👤 Customer Profile")

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
            info_row("Education", customer["Education"])
            info_row("Marital Status", customer["Marital Status"])
            info_row("Monthly Income", customer["Monthly Income (₹)"])
            info_row("Employment Duration", customer["Employment Duration (Months)"])

        # -----------------------------
        # Credit Behaviour
        # -----------------------------
        with st.container(border=True):

            st.markdown("### 📊 Credit Behaviour")

            info_row(
                "Oldest Credit Line",
                customer["Oldest Credit Line (Months)"]
            )

            info_row(
                "Newest Credit Line",
                customer["Newest Credit Line (Months)"]
            )

            info_row(
                "Months Since Last Payment",
                customer["Months Since Last Payment"]
            )

            info_row(
                "Months Since Last Credit Enquiry",
                customer["Months Since Last Credit Enquiry"]
            )

        # -----------------------------
        # Credit Enquiries
        # -----------------------------
        with st.container(border=True):

            st.markdown("### 🔍 Credit Enquiries")

            info_row(
                "Credit Enquiries (Last 3 Months)",
                customer["Credit Enquiries (Last 3 Months)"]
            )

            info_row(
                "Credit Card Enquiries (12 Months)",
                customer["Credit Card Enquiries (12 Months)"]
            )

            info_row(
                "Personal Loan Enquiries (12 Months)",
                customer["Personal Loan Enquiries (12 Months)"]
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

    st.subheader("💰 Loan Details")

    col1, col2 = st.columns(2)

    with col1:
        loan_amount = st.number_input(
            "Requested Loan Amount (₹)",
            min_value=0.0,
            step=10000.0
        )

        interest_rate = st.number_input(
            "Interest Rate (%)",
            min_value=0.0,
            max_value=30.0,
            step=0.25
        )

        loan_type = st.selectbox(
            "Loan Type",
            [
                "Home Loan",
                "Personal Loan",
                "Vehicle Loan",
                "Education Loan",
                "Business Loan"
            ]
        )

    with col2:
        tenure = st.number_input(
            "Loan Tenure (Years)",
            min_value=1,
            max_value=40,
            value=10
        )

        collateral = st.number_input(
            "Collateral Value (₹)",
            min_value=0.0,
            step=10000.0
        )

    return {
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "loan_type": loan_type,
        "tenure": tenure,
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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Risk Grade",
            risk_grade
        )

    with col2:
        st.metric(
            "Model",
            "LightGBM"
        )

    with col3:
        st.metric(
            "Prediction",
            "Success"
        )


