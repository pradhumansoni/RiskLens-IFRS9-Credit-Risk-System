import streamlit as st
from src.components import create_footer
# ==========================================================
# Page Creation
# ==========================================================



st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Page")

st.subheader(
    "IFRS 9 Compliant Credit Risk Analysis & Decision Support System"
)

st.divider()


# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("---")

st.markdown(
"""
# 🏦 IFRS 9 Compliant Credit Risk Analysis &
## Decision Support System

### Enterprise Banking Application

Machine Learning • IFRS 9 • Explainable AI • Streamlit
"""
)

st.write(
"""
This application is an enterprise banking decision support system designed
to assist credit officers in evaluating loan applications using Machine
Learning and IFRS 9 Expected Credit Loss methodology.

The system combines predictive analytics with banking business rules to
generate transparent, explainable and risk-aware lending decisions.
"""
)

st.markdown("---")

# ==========================================================
# Key Features
# ==========================================================

st.header("✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
"""
🧠 **ML Risk Prediction**

Predicts internal borrower risk grades
using a trained LightGBM model.
"""
    )

    st.info(
"""
📊 **IFRS 9 Engine**

Calculates PD, LGD, EAD,
IFRS Stage and Expected Credit Loss.
"""
    )

with col2:

    st.info(
"""
🔄 **What-If Analysis**

Compare multiple loan scenarios
before approving a proposal.
"""
    )

    st.info(
"""
⚖️ **Decision Support**

Generates transparent
business-oriented lending recommendations.
"""
    )

with col3:

    st.info(
"""
📈 **Model Performance**

Interactive model evaluation,
confusion matrix and ROC analysis.
"""
    )

    st.info(
"""
🔍 **Explainable AI**

Understand model predictions
through SHAP explainability.
"""
    )

st.markdown("---")


# ==========================================================
# System Workflow
# ==========================================================

st.header("🔄 System Workflow")

st.code(
"""
Customer Search
      │
      ▼
Retrieve Customer Profile
      │
      ▼
Enter Loan Proposal
      │
      ▼
ML Risk Prediction
      │
      ▼
IFRS 9 Calculations
      │
      ▼
Credit Decision
      │
      ▼
Scenario Analysis
""",
language="text"
)

st.markdown("---")


# ==========================================================
# TECH STACK
# ==========================================================


st.header("🛠 Technology Stack")

c1, c2 = st.columns(2)

with c1:

    st.subheader("Machine Learning")

    st.markdown("""
- Python
- Scikit-learn
- LightGBM
- SHAP
""")

    st.subheader("Data Processing")

    st.markdown("""
- Pandas
- NumPy
""")

with c2:

    st.subheader("Frontend")

    st.markdown("""
- Streamlit
- Matplotlib
""")

    st.subheader("Banking Framework")

    st.markdown("""
- IFRS 9
- Expected Credit Loss (ECL)
- Risk-Based Lending
""")

st.markdown("---")

# ==========================================================
# MODEL OVERVIEW
# ==========================================================


st.header("🧠 Model Overview")

st.write(
"""
The application uses a LightGBM multiclass classification model
to predict internal borrower risk grades (P1–P4).

The predicted risk grade is mapped to a Probability of Default (PD),
which is combined with Loss Given Default (LGD) and Exposure at
Default (EAD) to estimate Expected Credit Loss (ECL) in accordance
with IFRS 9 principles.

The application also supports scenario-based What-If Analysis,
allowing credit officers to compare multiple lending proposals
before making a final credit decision.
"""
)

st.markdown("---")

# ==========================================================
# APP ARCHITECTURE
# ==========================================================


st.header("🏗 Application Architecture")

st.code(
"""
app.py
   │
   ├──────── Dashboard
   ├──────── Loan Assessment
   ├──────── Model Performance
   └──────── About

                │

                ▼

Prediction Engine

IFRS 9 Engine

Machine Learning Model

Utilities & Components
""",
language="text"
)

st.markdown("---")


# ==========================================================
# DISCLAIMER
# ==========================================================

st.header("⚠ Disclaimer")

st.warning(
"""
This application has been developed for educational
and demonstration purposes.

The implementation follows simplified IFRS 9 concepts
and should not be considered a production-ready banking
solution without regulatory validation and institution-
specific calibration.
"""
)

st.divider()

create_footer()

