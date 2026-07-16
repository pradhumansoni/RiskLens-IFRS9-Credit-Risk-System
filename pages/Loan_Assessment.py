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
    create_risk_summary_card
)

from src.prediction import (
    predict_risk,
    predict_probability,
    map_risk_grade
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

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value



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
    
    report = generate_risk_report(

        applicant_id=st.session_state.current_applicant,

        risk_grade=st.session_state.current_risk,

        loan_amount=loan_data["loan_amount"],

        collateral_value=loan_data["collateral"]

    )

    report = format_risk_report(report)

    st.session_state.current_report = report


if st.session_state.current_report is not None:

    st.write(st.session_state.current_report)


