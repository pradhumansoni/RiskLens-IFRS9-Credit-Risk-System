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

from src.config import (
    RISK_GRADE_SCORE,
    IFRS_STAGE_SCORE,
    PD_SCORE,
    COLLATERAL_SCORE,
    LGD_SCORE,
    LOAN_AMOUNT_SCORE,
    ECL_SCORE,
    LOSS_RATIO_SCORE,
    DECISION_THRESHOLDS
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
        "monitoring": "Not Applicable(Should Decline the Application)",
        "reason": "Credit risk exceeds the bank's acceptable lending policy."
    }
]

RISK_LEVEL_MAPPING = {
    "P1": "Very Low Risk",
    "P2": "Low Risk",
    "P3": "Moderate Risk",
    "P4": "High Risk"
}

# We are implementing the score system based on these IFRS9 Results + Model Risk Class + Stage

# ==========================================================
# GENERIC SCORE LOOKUP
# ==========================================================

def lookup_score(value, rules):

    for threshold, score in rules:

        if value <= threshold:
            return score

    return 0

# ==========================================================
# GENERIC REVERSE LOOKUP
# ==========================================================

# ==========================================================
# HIGHER IS BETTER SCORE LOOKUP
# ==========================================================

def lookup_high_score(value, rules):
    """
    Lookup helper for metrics where higher values
    receive higher scores.

    Example:
        Collateral Coverage
    """

    for threshold, score in reversed(rules):

        if value >= threshold:
            return score

    return 0

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
# CREDIT DECISION SCORE
# ==========================================================

def compute_credit_decision_score(
    risk_grade,
    stage,
    pd,
    loan_amount,
    collateral_coverage,
    lgd,
    ecl,
    loss_ratio
):
    """
    Computes the final Credit Decision Score (0-100).

    Returns
    -------
    dict
        {
            "Risk Grade Score": ...,
            "Stage Score": ...,
            "PD Score": ...,
            "Borrower Risk Score": ...,

            "Collateral Score": ...,
            "LGD Score": ...,
            "Loan Amount Score": ...,
            "Loan Structure Score": ...,

            "ECL Score": ...,
            "Loss Ratio Score": ...,
            "Expected Loss Score": ...,

            "Final Score": ...
        }
    """

    # ======================================================
    # BORROWER RISK (40)
    # ======================================================

    risk_grade_score = RISK_GRADE_SCORE[risk_grade]

    stage_score = IFRS_STAGE_SCORE[stage]

    pd_score = lookup_score(
        pd,
        PD_SCORE
    )

    borrower_score = (
        risk_grade_score +
        stage_score +
        pd_score
    )

    # ======================================================
    # LOAN STRUCTURE (30)
    # ======================================================

    collateral_score = lookup_high_score(
        collateral_coverage,
        COLLATERAL_SCORE
    )

    lgd_score = lookup_score(
        lgd,
        LGD_SCORE
    )

    loan_amount_score = lookup_score(
        loan_amount,
        LOAN_AMOUNT_SCORE
    )

    loan_structure_score = (
        collateral_score +
        lgd_score +
        loan_amount_score
    )

    # ======================================================
    # EXPECTED LOSS (30)
    # ======================================================

    ecl_score = lookup_score(
        ecl,
        ECL_SCORE
    )

    loss_ratio_score = lookup_score(
        loss_ratio,
        LOSS_RATIO_SCORE
    )

    expected_loss_score = (
        ecl_score +
        loss_ratio_score
    )

    # ======================================================
    # FINAL SCORE
    # ======================================================

    final_score = (
        borrower_score +
        loan_structure_score +
        expected_loss_score
    )

    return {

        # Borrower Risk
        "Risk Grade Score": risk_grade_score,
        "Stage Score": stage_score,
        "PD Score": pd_score,
        "Borrower Risk Score": borrower_score,

        # Loan Structure
        "Collateral Score": collateral_score,
        "LGD Score": lgd_score,
        "Loan Amount Score": loan_amount_score,
        "Loan Structure Score": loan_structure_score,

        # Expected Loss
        "ECL Score": ecl_score,
        "Loss Ratio Score": loss_ratio_score,
        "Expected Loss Score": expected_loss_score,

        # Final
        "Final Score": final_score

    }

# ==========================================================
# GENERATE LENDING DECISION
# ==========================================================

def generate_decision(decision_score):
    """
    Generate the final lending decision based on the
    Credit Decision Score.
    """

    if decision_score >= 85:

        return {

            "Decision": "Approve",

            "Monitoring": "Standard Annual Review",

            "Reason": (
                "Excellent borrower profile with very low expected "
                "credit risk."
            )

        }

    elif decision_score >= 70:

        return {

            "Decision": "Approve with Monitoring",

            "Monitoring": "Quarterly Credit Review",

            "Reason": (
                "Loan can be approved, but periodic monitoring is "
                "recommended due to moderate credit risk."
            )

        }

    elif decision_score >= 55:

        return {

            "Decision": "Additional Collateral Required",

            "Monitoring": "Collateral Verification Required",

            "Reason": (
                "Current collateral protection is insufficient for the "
                "identified credit risk. Additional security is recommended."
            )

        }

    elif decision_score >= 40:

        return {

            "Decision": "Manual Credit Committee Review",

            "Monitoring": "Senior Credit Officer Review",

            "Reason": (
                "Application requires manual assessment before a final "
                "lending decision can be made."
            )

        }

    else:

        return {

            "Decision": "Decline Application",

            "Monitoring": "No Further Processing",

            "Reason": (
                "Overall credit risk exceeds the bank's acceptable "
                "lending policy."
            )

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

    # ======================================================
    # IFRS 9 CALCULATIONS
    # ======================================================

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

    loss_ratio = ecl / loan_amount if loan_amount > 0 else 0


    # ======================================================
    # CREDIT DECISION SCORE
    # ======================================================

    score = compute_credit_decision_score(

        risk_grade=risk_grade,

        stage=stage,

        pd=pd,

        loan_amount=loan_amount,

        collateral_coverage=coverage,

        lgd=lgd,

        ecl=ecl,

        loss_ratio=loss_ratio

    )


    # ======================================================
    # FINAL DECISION
    # ======================================================

    decision = generate_decision(
        score["Final Score"]
    )


    # ======================================================
    # RETURN REPORT
    # ======================================================

    return {

        "Applicant ID": applicant_id,

        "Risk Grade": risk_grade,

        "Risk Level": risk_level,

        "PD": pd,

        "LGD": lgd,

        "Loan Amount": loan_amount,

        "Collateral Value": collateral_value,

        "Collateral Coverage": coverage,

        "EAD": ead,

        "ECL": ecl,

        "IFRS Stage": stage,

        "Decision": decision["Decision"],

        "Monitoring": decision["Monitoring"],

        "Reason": decision["Reason"],

        "Loss Ratio": loss_ratio,

        # ------------------------
        # Credit Decision Score
        # ------------------------

        # Overall Score
        "Decision Score": score["Final Score"],

        # Section Scores
        "Borrower Risk Score": score["Borrower Risk Score"],
        "Loan Structure Score": score["Loan Structure Score"],
        "Expected Loss Score": score["Expected Loss Score"],

        # Detailed Scores
        "Risk Grade Score": score["Risk Grade Score"],
        "Stage Score": score["Stage Score"],
        "PD Score": score["PD Score"],

        "Collateral Score": score["Collateral Score"],
        "LGD Score": score["LGD Score"],
        "Loan Amount Score": score["Loan Amount Score"],

        "ECL Score": score["ECL Score"],
        "Loss Ratio Score": score["Loss Ratio Score"],

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

