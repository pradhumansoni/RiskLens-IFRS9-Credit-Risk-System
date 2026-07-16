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