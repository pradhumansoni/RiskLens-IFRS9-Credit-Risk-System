from pathlib import Path
import pandas as pd
import streamlit as st

# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"
ASSETS_DIR = PROJECT_ROOT / "assets"

# ============================================================
# Load CSS
# ============================================================

def load_css():

    css_file = ASSETS_DIR / "styles.css"

    if css_file.exists():

        with open(css_file) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )


# ============================================================
# Search Customer Profile (Human Readable)
# ============================================================

def search_customer_profile(applicant_id):

    customer_profile = pd.read_csv(
        DATA_DIR / "customer_profile.csv"
    )

    customer = customer_profile[
        customer_profile["Applicant ID"] == applicant_id
    ]

    if customer.empty:
        return None

    return customer.iloc[0]


# ============================================================
# Search Customer Features (Encoded)
# ============================================================

def search_customer_features(applicant_id):

    customer_database = pd.read_csv(
        DATA_DIR / "customer_database.csv"
    )

    customer = customer_database[
        customer_database["PROSPECTID"] == applicant_id
    ]

    if customer.empty:
        return None

    return customer.iloc[0]

