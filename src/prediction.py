from pathlib import Path
import joblib
import pandas as pd

# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_DIR = PROJECT_ROOT / "models"


# ============================================================
# Load Trained Model
# ============================================================

def load_model():
    """
    Load the trained LightGBM model.
    """

    model = joblib.load(
        MODEL_DIR / "final_lgbm_model.pkl"
    )

    return model


# ============================================================
# Predict Risk Class
# ============================================================

def predict_risk(customer_features):
    """
    Predict encoded risk class.

    Returns:
        int : 0, 1, 2 or 3
    """

    model = load_model()

    # Remove Applicant ID
    features = customer_features.drop(labels=["PROSPECTID"])

    # Convert Series -> DataFrame
    features = features.to_frame().T
    features = features.apply(pd.to_numeric)
    prediction = model.predict(features)

    return int(prediction[0])


# ============================================================
# Predict Class Probabilities
# ============================================================

def predict_probability(customer_features):
    """
    Returns class probabilities.
    """

    model = load_model()

    features = customer_features.drop(labels=["PROSPECTID"])

    features = features.to_frame().T
    features = features.apply(pd.to_numeric)
    probability = model.predict_proba(features)

    return probability[0]


# ============================================================
# Business Mapping
# ============================================================

def map_risk_grade(encoded_prediction):

    mapping = {
        0: "P1",
        1: "P2",
        2: "P3",
        3: "P4"
    }

    return mapping[encoded_prediction]


# ============================================================
# Run Credit Assessment
# ============================================================

from IFRS9_engine import (
    generate_risk_report,
    format_risk_report
)


def run_credit_assessment(
    applicant_id: str,
    risk_grade: str,
    loan_data: dict
) -> dict:
    """
    Run the complete IFRS 9 credit assessment pipeline.

    Parameters
    ----------
    applicant_id : str
    risk_grade : str
    loan_data : dict

    Returns
    -------
    dict
        Formatted IFRS 9 report.
    """

    report = generate_risk_report(
        applicant_id=applicant_id,
        risk_grade=risk_grade,
        loan_amount=loan_data["loan_amount"],
        collateral_value=loan_data["collateral"]
    )

    return format_risk_report(report)