import streamlit as st
from src.utils import load_css

load_css()

st.set_page_config(
    page_title="AI Credit Risk System",
    page_icon="🏦",
    layout="wide"
)

dashboard = st.Page("pages/Dashboard.py", title="🏠 Dashboard")
loan = st.Page("pages/Loan_Assessment.py", title="📝 Loan Assessment")
model = st.Page("pages/Model_Performance.py", title="Ⓜ️ Model Performance")
about = st.Page("pages/About.py", title="ℹ️ About")

st.sidebar.title("🏦 AI Credit Risk System")
st.sidebar.markdown("---")

pg = st.navigation([dashboard, loan, model , about])
pg.run()