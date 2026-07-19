import streamlit as st

from src.utils import load_css

from src.components import (
    create_page_header,
    create_welcome_banner,
    create_system_overview,
    create_quick_actions,
    create_project_highlights,
    create_footer
)

load_css()

import streamlit as st

# ==========================================================
# Application Branding
# ==========================================================

st.title("🏦 RiskLens")

st.markdown(
    "### IFRS 9 Compliant Credit Risk & Expected Credit Loss (ECL) Platform"
)

st.write(
    """
An AI-powered decision support system that assists credit officers in borrower
risk assessment, IFRS 9 Expected Credit Loss (ECL) estimation, and transparent
lending decisions through explainable machine learning.
"""
)

st.divider()

create_welcome_banner()

create_system_overview()

create_quick_actions()


create_project_highlights()

create_footer()