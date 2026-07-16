import streamlit as st
import pandas as pd
from src.config import MODEL_DIR

classification_report_df = pd.read_csv(
    MODEL_DIR / "classification_report.csv"
)


st.title("📈 Model Performance")

st.caption(
    "Performance evaluation and explainability of the LightGBM credit risk model."
)


#================================================================================
# Models Overview
#================================================================================

st.divider()

st.header("🤖 Model Overview")

col1, col2 = st.columns(2)

with col1:

    st.metric("Algorithm", "LightGBM")

    st.metric("Prediction Type", "Multiclass Classification")

    st.metric("Risk Classes", "P1 • P2 • P3 • P4")

with col2:

    st.metric("Training Features", "56")

    st.metric("Explainability", "SHAP")

    st.metric("Status", "Final Tuned Model")

#================================================================================
# Performance Metrics
#================================================================================
st.divider()

st.header("📊 Performance Metrics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Accuracy", "79.18%")

with c2:
    st.metric("Precision", "77.15%")

with c3:
    st.metric("Recall", "79.18%")

with c4:
    st.metric("F1 Score", "77.82%")

#================================================================================
# Classification Report
#================================================================================

st.divider()
st.header("🧩 LightGBM Classification Report")
st.dataframe(
    classification_report_df,
    use_container_width=True
)
st.info(
    "The classification Report shows how the model performance on various different metrics"
)

#================================================================================
# Confusion Matrix
#================================================================================

st.divider()

st.header("🧩 Confusion Matrix")

st.image(
    MODEL_DIR / "confusion_matrix.png",
    use_container_width=True
)

st.info(
    "The confusion matrix illustrates how accurately the LightGBM model classifies borrowers into the four internal risk grades (P1–P4)."
)

#================================================================================
# Normalized Confusion Matrix
#================================================================================

st.divider()

st.header("📊 Normalized Confusion Matrix")

st.image(
    MODEL_DIR / "normalized_confusion_matrix.png",
    use_container_width=True
)

st.info(
    "Normalized values make it easier to compare performance across risk grades regardless of class imbalance."
)

#================================================================================
# ROC-AUC Curve
#================================================================================

st.divider()

st.header("📈 ROC-AUC Curve")

st.image(
    MODEL_DIR / "roc_curve.png",
    use_container_width=True
)

st.info(
    "ROC curves evaluate the discrimination ability of the classifier for each internal risk grade."
)

#================================================================================
# Prediction Confidence
#================================================================================

st.divider()

st.header("🎯 Prediction Confidence")

st.image(
    MODEL_DIR / "prediction_confidence.png",
    use_container_width=True
)

st.info(
    "The probability distribution illustrates the model's confidence in assigning borrowers to the predicted risk grade."
)

#================================================================================
# SHAP Explainability
#================================================================================

st.divider()

st.header("🔍 SHAP Explainability")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Summary",
        "Beeswarm",
        "Correct Prediction",
        "Misclassified Prediction"
    ]
)

with tab1:
    st.image(
        MODEL_DIR / "shap_summary.png",
        use_container_width=True
    )

with tab2:
    st.image(
        MODEL_DIR / "shap_beeswarm.png",
        use_container_width=True
    )

with tab3:
    st.image(
        MODEL_DIR / "waterfall_correct.png",
        use_container_width=True
    )

with tab4:
    st.image(
        MODEL_DIR / "waterfall_incorrect.png",
        use_container_width=True
    )

#================================================================================
# Models Insights
#================================================================================

st.divider()

st.header("💡 Model Insights")

st.success("""

• LightGBM achieved the best overall performance among all evaluated models.

• The model demonstrates strong discrimination across the four internal risk grades.

• Recent credit enquiries and historical delinquency behaviour are among the strongest predictors of borrower risk.

• SHAP analysis confirms that the model learns meaningful relationships rather than relying on a small number of dominant features.

• The model provides transparent predictions through both global and local explainability.

""")

#================================================================================
# WHY LightGBM
#================================================================================


st.divider()

st.header("🏆 Why LightGBM?")

st.write("""

LightGBM was selected as the final production model after evaluating multiple baseline classifiers.

Reasons for selecting LightGBM include:

- Highest overall predictive performance.
- Fast training and inference.
- Handles nonlinear feature interactions effectively.
- Excellent scalability for large credit datasets.
- Native compatibility with SHAP explainability.
- Suitable for enterprise credit risk modelling applications.

""")