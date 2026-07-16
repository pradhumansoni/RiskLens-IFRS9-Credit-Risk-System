"""
==========================================================
IFRS 9 Risk Engine

Author : Pradhuman Kumar Soni

Description:
Enterprise Risk Engine for IFRS 9 Credit Risk Assessment.
This module contains all business logic required for
credit risk evaluation and lending decision support.

==========================================================
"""


# ==========================================================
# IMPORTS
# ==========================================================

from typing import Dict
from src.config import (
    PD_MAPPING,
    LGD_RULES,
    STAGE_MAPPING,
    DECISION_RULES,
    RISK_LEVEL_MAPPING
)

# ==========================================================
# CONFIGURATION
# ==========================================================

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
# PD ENGINE
# ==========================================================

# Reusable Function To Calculate PD based on The Risk grades
def calculate_pd(risk_grade: str) -> float:
    """
    Convert an internal risk grade (P1-P4)
    into its corresponding Probability of Default (PD).

    Parameters
    ----------
    risk_grade : str
        Predicted internal credit risk grade.

    Returns
    -------
    float
        Probability of Default.
    """

    risk_grade = risk_grade.upper()

    if risk_grade not in PD_MAPPING:
        raise ValueError(
            f"Invalid Risk Grade '{risk_grade}'. "
            "Expected one of: P1, P2, P3 or P4."
        )

    return PD_MAPPING[risk_grade]['pd']

# ==========================================================
# LGD ENGINE
# ==========================================================

# LGD Function
def calculate_lgd(
    loan_amount: float,
    collateral_value: float
):
    """
    Calculate Loss Given Default (LGD)
    using collateral coverage.

    Parameters
    ----------
    loan_amount : float
        Requested loan amount.

    collateral_value : float
        Bank-assessed collateral value.

    Returns
    -------
    tuple
        (LGD, Coverage Ratio)
    """

    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    coverage = collateral_value / loan_amount

    for rule in LGD_RULES:
        if coverage >= rule["min_coverage"]:
            return rule["lgd"], coverage

    return 0.90, coverage

# ==========================================================
# EAD ENGINE
# ==========================================================

def calculate_ead(loan_amount: float) -> float:
    """
    Calculate Exposure at Default (EAD).

    For this project, EAD is assumed to be equal
    to the requested loan amount.

    Parameters
    ----------
    loan_amount : float
        Requested loan amount.

    Returns
    -------
    float
        Exposure at Default.
    """

    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    return loan_amount

# ==========================================================
# ECL ENGINE
# ==========================================================

def calculate_ecl(
    pd: float,
    lgd: float,
    ead: float
) -> float:
    """
    Calculate Expected Credit Loss (ECL).

    Parameters
    ----------
    pd : float
        Probability of Default.

    lgd : float
        Loss Given Default.

    ead : float
        Exposure at Default.

    Returns
    -------
    float
        Expected Credit Loss.
    """

    if not (0 <= pd <= 1):
        raise ValueError("PD must be between 0 and 1.")

    if not (0 <= lgd <= 1):
        raise ValueError("LGD must be between 0 and 1.")

    if ead < 0:
        raise ValueError("EAD cannot be negative.")

    return pd * lgd * ead

# ==========================================================
# IFRS 9 STAGE CLASSIFICATION
# ==========================================================

def classify_stage(risk_grade: str) -> str:
    """
    Map an internal risk grade (P1-P4)
    to the corresponding IFRS 9 stage.
    """

    risk_grade = risk_grade.upper()

    if risk_grade not in STAGE_MAPPING:
        raise ValueError(
            f"Invalid Risk Grade '{risk_grade}'. "
            "Expected one of: P1, P2, P3 or P4."
        )

    return STAGE_MAPPING[risk_grade]

# ==========================================================
# LENDING DECISION ENGINE
# ==========================================================

# building the decision Engine
def generate_decision(
    stage: str,
    ecl: float,
    ead: float
):
    """
    Generate lending recommendation based on
    IFRS 9 Stage and Expected Loss Ratio.

    Parameters
    ----------
    stage : str
        IFRS 9 Stage.

    ecl : float
        Expected Credit Loss.

    ead : float
        Exposure at Default.

    Returns
    -------
    dict
        Lending recommendation.
    """

    if ead <= 0:
        raise ValueError("EAD must be greater than zero.")

    loss_ratio = ecl / ead

    for rule in DECISION_RULES:

        if (
            stage == rule["stage"]
            and loss_ratio <= rule["max_loss_ratio"]
        ):

            return {
                "Loss Ratio": loss_ratio,
                "Decision": rule["decision"],
                "Monitoring": rule["monitoring"],
                "Reason":rule["reason"]
            }

    return {
    "Loss Ratio": loss_ratio,
    "Decision": "Manual Review Required",
    "Monitoring": "Senior Credit Committee",
    "Reason": "Application requires manual credit assessment."
}

# ==========================================================
# RISK REPORT GENERATOR
# ==========================================================

def generate_risk_report(
    applicant_id,
    risk_grade,
    loan_amount,
    collateral_value
):
    risk_level = RISK_LEVEL_MAPPING[risk_grade]
    pd = calculate_pd(risk_grade)
    lgd, coverage = calculate_lgd(
        loan_amount,
        collateral_value
    )
    ead = calculate_ead(loan_amount)
    ecl = calculate_ecl(
        pd,
        lgd,
        ead
    )
    stage = classify_stage(risk_grade)
    decision = generate_decision(
        stage,
        ecl,
        ead
    )
    return {

        "Applicant ID": applicant_id,

        "Risk Grade": risk_grade,

        "Risk Level": risk_level,

        "PD": pd,

        "LGD": lgd,

        "Loan Amount":loan_amount,

        "Collateral Value": collateral_value,

        "Collateral Coverage": coverage,

        "EAD": ead,

        "ECL": ecl,

        "IFRS Stage": stage,

        "Decision": decision["Decision"],

        "Monitoring": decision["Monitoring"],

        "Reason": decision["Reason"],

        "Loss Ratio": decision["Loss Ratio"]

    }

def format_risk_report(report: Dict) -> Dict:
    """
    Format the risk report for display.
    """

    formatted = report.copy()

    formatted["PD"] = f"{report['PD']:.2%}"
    formatted["LGD"] = f"{report['LGD']:.2%}"
    formatted["Collateral Coverage"] = f"{report['Collateral Coverage']:.2%}"
    formatted["Loss Ratio"] = f"{report['Loss Ratio']:.2%}"

    formatted["Loan Amount"] = f"₹{report['Loan Amount']:,.2f}"
    formatted["Collateral Value"] = f"₹{report['Collateral Value']:,.2f}"
    formatted["EAD"] = f"₹{report['EAD']:,.2f}"
    formatted["ECL"] = f"₹{report['ECL']:,.2f}"

    return formatted

