# ==========================================================
# APP INFORMATION
# ==========================================================

APP_TITLE = "AI Credit Risk Management System"
APP_ICON = "🏦"

# ==========================================================
# COLOR PALETTE
# ==========================================================

PRIMARY = "#1E3A5F"       # Navy Blue
SECONDARY = "#0F766E"     # Teal
SUCCESS = "#16A34A"       # Green
WARNING = "#F59E0B"       # Amber
DANGER = "#DC2626"        # Red

BACKGROUND = "#F8FAFC"
CARD = "#FFFFFF"
TEXT = "#1F2937"

# ==========================================================
# MODEL PATHS
# ==========================================================


from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIR = PROJECT_ROOT / "assets"


MODEL_DIR = ASSETS_DIR / "model"

MODEL_PATH = "models/final_lgbm_model.pkl"

DATA_PATH = "data/processed/encoded_dataset.csv"

# ==========================================================
# Customer Profile Columns
# ==========================================================

PROFILE = {
    "APPLICANT_ID": "Applicant ID",
    "GENDER": "Gender",
    "EDUCATION": "Education",
    "MARITAL_STATUS": "Marital Status",
    "MONTHLY_INCOME": "Monthly Income (₹)",
    "EMPLOYMENT_DURATION": "Employment Duration (Months)",

    "HOME_LOANS": "Home Loan Accounts",
    "PERSONAL_LOANS": "Personal Loan Accounts",
    "CREDIT_CARDS": "Credit Card Accounts",

    "SECURED_LOANS": "Secured Loan Accounts",
    "UNSECURED_LOANS": "Unsecured Loan Accounts",
    "OTHER_LOANS": "Other Loan Accounts",

    "TOTAL_ACTIVE_LOANS": "Total Active Loan Accounts",

    "OLDEST_TL": "Oldest Credit Line (Months)",
    "NEWEST_TL": "Newest Credit Line (Months)",

    "LAST_PAYMENT": "Months Since Last Payment",
    "LAST_ENQUIRY": "Months Since Last Credit Enquiry",

    "MISSED_PAYMENTS": "Total Missed Payments",
    "CURRENT_DELINQ": "Current Delinquency Level",
    "MAX_DELINQ": "Highest Recent Delinquency",
    "DPD60": "60+ DPD Occurrences",

    "ENQ_3M": "Credit Enquiries (Last 3 Months)",
    "CC_ENQ": "Credit Card Enquiries (12 Months)",
    "PL_ENQ": "Personal Loan Enquiries (12 Months)"
}

# ============================================================
# IFRS 9 Configuration
# ============================================================

PD_MAPPING = {
    "P1": {
        "description": "Very Low Risk",
        "pd": 0.01
    },
    "P2": {
        "description": "Low Risk",
        "pd": 0.03
    },
    "P3": {
        "description": "Medium Risk",
        "pd": 0.08
    },
    "P4": {
        "description": "High Risk",
        "pd": 0.20
    }
}

LGD_RULES = [
    {"min_coverage": 1.00, "lgd": 0.20},
    {"min_coverage": 0.80, "lgd": 0.35},
    {"min_coverage": 0.50, "lgd": 0.50},
    {"min_coverage": 0.20, "lgd": 0.70},
    {"min_coverage": 0.00, "lgd": 0.90}
]

STAGE_MAPPING = {
    "P1": "Stage 1",
    "P2": "Stage 1",
    "P3": "Stage 2",
    "P4": "Stage 3"
}

DECISION_RULES = [
    {
        "stage": "Stage 1",
        "max_loss_ratio": 0.02,
        "decision": "Approve",
        "monitoring": "Standard Annual Review",
        "reason": "Low expected credit loss and strong borrower credit profile."
    },
    {
        "stage": "Stage 1",
        "max_loss_ratio": 0.05,
        "decision": "Approve with Monitoring",
        "monitoring": "Semi-Annual Review",
        "reason": "Moderate expected credit loss. Regular monitoring is recommended."
    },
    {
        "stage": "Stage 2",
        "max_loss_ratio": 0.05,
        "decision": "Approve with Additional Collateral",
        "monitoring": "Quarterly Review",
        "reason": "Additional collateral is recommended to reduce the bank's potential loss."
    },
    {
        "stage": "Stage 2",
        "max_loss_ratio": 1.00,
        "decision": "Manual Review Required",
        "monitoring": "Senior Credit Committee",
        "reason": "High expected credit loss requires manual credit assessment."
    },
    {
        "stage": "Stage 3",
        "max_loss_ratio": 1.00,
        "decision": "Decline Application",
        "monitoring": "Not Applicable",
        "reason": "Credit risk exceeds the bank's acceptable lending policy."
    }
]

RISK_LEVEL_MAPPING = {
    "P1": "Very Low Risk",
    "P2": "Low Risk",
    "P3": "Moderate Risk",
    "P4": "High Risk"
}

# ==========================================================
# CREDIT DECISION SCORECARD
# ==========================================================

# -----------------------------
# Borrower Risk (40)
# -----------------------------

RISK_GRADE_SCORE = {
    "P1": 20,
    "P2": 16,
    "P3": 10,
    "P4": 4
}

IFRS_STAGE_SCORE = {
    "Stage 1": 10,
    "Stage 2": 6,
    "Stage 3": 2
}

PD_SCORE = [
    (0.03, 10),
    (0.08, 8),
    (0.15, 6),
    (0.25, 3),
    (1.00, 1)
]


# -----------------------------
# Loan Structure (30)
# -----------------------------

COLLATERAL_SCORE = [
    (0.50, 2),
    (0.80, 6),
    (1.00, 10),
    (1.50, 13),
    (float("inf"), 15)
]

LGD_SCORE = [
    (0.20, 10),
    (0.40, 8),
    (0.60, 5),
    (1.00, 2)
]

LOAN_AMOUNT_SCORE = [
    (200000, 5),
    (500000, 4),
    (1000000, 3),
    (2000000, 2),
    (float("inf"), 1)
]


# -----------------------------
# Expected Loss (30)
# -----------------------------

ECL_SCORE = [
    (5000, 20),
    (25000, 16),
    (50000, 12),
    (100000, 8),
    (float("inf"), 4)
]

LOSS_RATIO_SCORE = [
    (0.01, 10),
    (0.03, 8),
    (0.05, 6),
    (0.10, 3),
    (1.00, 1)
]


# ==========================================================
# FINAL DECISION
# ==========================================================

DECISION_THRESHOLDS = [

    (85, "Approve"),

    (70, "Approve with Monitoring"),

    (55, "Additional Collateral Required"),

    (40, "Manual Credit Committee Review"),

    (0, "Decline Application")

]