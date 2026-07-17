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


# ============================================
# Display Formatting Helpers
# ============================================

import math


def format_currency(value):
    """Format currency using Indian Rupee notation."""

    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "-"

    return f"₹{value:,.0f}"


def format_percentage(value, decimals=1):
    """Format percentage values."""

    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "-"

    value = round(float(value), decimals)

    if value.is_integer():
        return f"{int(value)}%"

    return f"{value:.{decimals}f}%"


def format_number(value):
    """Display integer values without unnecessary decimals."""

    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "-"

    value = float(value)

    if value.is_integer():
        return str(int(value))

    return f"{value:.1f}"


def format_months(value):
    """Format bureau month-based features."""

    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "-"

    value = int(round(float(value)))

    if value == 1:
        return "1 month"

    return f"{value} months"


def format_text(value):
    """Convert ALL CAPS text into readable title case."""

    if value is None:
        return "-"

    value = str(value).strip()

    if value == "":
        return "-"

    return (
        value.replace("_", " ")
             .replace("-", " ")
             .title()
    )

