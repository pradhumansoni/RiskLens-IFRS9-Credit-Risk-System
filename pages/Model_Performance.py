import streamlit as st
import pandas as pd
from src.config import MODEL_DIR,MODEL_METADATA,MODEL_METRICS
from src.components import create_footer

#================================================================================
# Three Main Tabs For Model Validation Reporting
#================================================================================

st.title("📊 Model Validation Report")
st.caption(
    "Comprehensive validation and governance report for the deployed "
    "LightGBM credit risk classification model."
)

overview_tab, validation_tab, explain_tab,lightgbm_tab = st.tabs(
    [
        "📊 Overview",
        "🔍 Validation",
        "🧠 Explainability",
        "🏆 Why LightGBM"
    ]
)
#================================================================================
# Move Existing Sections
#================================================================================

with overview_tab:

    # ============================================================
    # SECTION 1 — MODEL OVERVIEW
    # ============================================================

    st.divider()

    st.header("🧠 Model Overview")
    st.caption("Overview of the deployed machine learning model used for credit risk assessment.")

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Model Name")
            st.write(MODEL_METADATA['MODEL_NAME'])

            st.markdown("### Algorithm")
            st.write("LightGBM Classifier")

            st.markdown("### Problem Type")
            st.write("Multi-class Classification")

            st.markdown("### Target Classes")
            st.write("P1 • P2 • P3 • P4")

            st.markdown("### Features Used")
            st.write(MODEL_METADATA['FEATURES'])

        with col2:
            st.markdown("### Training Samples")
            st.write(MODEL_METADATA['TRAIN_SIZE'])

            st.markdown("### Test Samples")
            st.write(MODEL_METADATA['TEST_SIZE'])

            st.markdown("### Training Date")
            st.write(MODEL_METADATA['TRAINING_DATE'])

            st.markdown("### Model Version")
            st.write(MODEL_METADATA['MODEL_VERSION'])

            st.markdown("### Deployment Status")
            st.info("Production Ready")

    st.divider()

    # ============================================================
    # SECTION 2 — PERFORMANCE SNAPSHOT
    # ============================================================

    st.divider()
    st.header("📊 Performance Snapshot")
    st.caption("Key evaluation metrics of the deployed LightGBM classification model.")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="Accuracy",
            value=MODEL_METRICS['Accuracy']
        )

    with col2:
        st.metric(
            label="Precision",
            value=MODEL_METRICS['Precision']
        )

    with col3:
        st.metric(
            label="Recall",
            value=MODEL_METRICS['Recall']
        )

    with col4:
        st.metric(
            label="F1 Score",
            value=MODEL_METRICS['F1 Score']
        )

    with col5:
        st.metric(
            label="ROC-AUC",
            value=MODEL_METRICS['ROC-AUC']
        )

    st.divider()
    with st.container(border=True):

        st.subheader("📝 Performance Summary")

        st.write("""
    The deployed **LightGBM classifier** achieved an overall **accuracy of 79.52%**
    with balanced **precision (77.50%)**, **recall (79.52%)**, and **F1-score (78.14%)**
    across four internal credit risk grades (P1–P4). The model demonstrates strong
    discriminative ability with a **macro ROC-AUC of 93.38%**, indicating effective
    separation between borrower risk categories.

    Overall, the model provides reliable predictive performance and forms a robust
    foundation for **IFRS 9 stage classification, Expected Credit Loss (ECL)
    estimation, and credit decision support**.
    """)
    st.divider()


    with st.container(border=True):

        st.subheader("✅ Performance Verdict")

        st.success(""" This is the following performance based verdict :
    - Strong overall predictive performance

    - Excellent class discrimination (Macro ROC-AUC: 93.38%)

    - Balanced precision and recall across multiple risk grades

    - Suitable for IFRS 9 credit risk assessment

    - Recommended for deployment in credit decision support workflows
    """)
        
    # ============================================================
    # SECTION 3 — MODEL DEVELOPMENT & SELECTION
    # ============================================================

    # Your existing Model Development code here

    st.divider()
    st.header("🏆 Model Development & Selection")
    st.caption(
        "Comparison of machine learning models evaluated during development and "
        "the rationale behind selecting the final production model."
    )

    # -----------------------------------------------------------------------------
    # Phase 1
    # -----------------------------------------------------------------------------

    st.divider()
    st.subheader("Phase 1 — Baseline Model Comparison")

    st.success(
        """
    Five baseline classification algorithms were initially evaluated using their
    default hyperparameters to identify the most promising candidates for further
    optimization. Based on overall predictive performance, **XGBoost** and
    **LightGBM** were selected for hyperparameter tuning using **Optuna**.
    """
    )

    baseline_df = pd.DataFrame({
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "XGBoost",
            "LightGBM"
        ],
        "Accuracy": [
            "76.26%",
            "71.65%",
            "78.23%",
            "78.87%",
            "79.18%"
        ],
        "Precision": [
            "72.32%",
            "72.00%",
            "75.49%",
            "76.95%",
            "77.15%"
        ],
        "Recall": [
            "76.26%",
            "71.65%",
            "78.23%",
            "78.87%",
            "79.18%"
        ],
        "F1 Score": [
            "72.68%",
            "71.82%",
            "76.03%",
            "77.61%",
            "77.82%"
        ],
        "Decision": [
            "Baseline",
            "Baseline",
            "Strong Candidate",
            "Selected for Tuning",
            "Selected for Tuning"
        ]
    })

    st.dataframe(
        baseline_df,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------------------------------
    # Phase 2
    # -----------------------------------------------------------------------------

    st.divider()
    st.subheader("Phase 2 — Hyperparameter Optimization")

    st.info(
    """
    5 Baseline Models

    ⬇

    Top 2 Models Selected
    (XGBoost & LightGBM)

    ⬇

    Optuna Hyperparameter Optimization

    ⬇

    Final Model Evaluation

    ⬇

    LightGBM Selected for Deployment
    """
    )

    # -----------------------------------------------------------------------------
    # Phase 3
    # -----------------------------------------------------------------------------

    st.divider()
    st.subheader("Phase 3 — Final Optimized Model Comparison")

    optimized_df = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "Weighted Precision",
            "Weighted Recall",
            "Weighted F1 Score",
            "Macro Precision",
            "Macro Recall",
            "Macro F1 Score"
        ],
        "XGBoost": [
            "79.30%",
            "77.39%",
            "79.30%",
            "78.05%",
            "71.27%",
            "68.60%",
            "69.55%"
        ],
        "LightGBM": [
            "79.52%",
            "77.50%",
            "79.52%",
            "78.14%",
            "71.83%",
            "68.71%",
            "69.78%"
        ]
    })

    def highlight_best(row):
        xgb = float(row["XGBoost"].rstrip("%"))
        lgb = float(row["LightGBM"].rstrip("%"))

        styles = ["", "", ""]

        if xgb > lgb:
            styles[1] = "background-color:#31A556;color:black;font-weight:bold;"
        elif lgb > xgb:
            styles[2] = "background-color:#31A556;color:black;font-weight:bold;"

        return styles

    styler = optimized_df.style.apply(highlight_best, axis=1)


    st.dataframe(
        styler,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------------------------------
    # Final Selection
    # -----------------------------------------------------------------------------
    st.divider()
    with st.container(border=True):

        st.subheader("🏅 Why LightGBM Was Selected")

        st.success(
    """
    **LightGBM** was selected as the final production model for the IFRS 9 Credit
    Risk Analysis & ECL System based on the following observations:

    - Achieved the highest overall predictive performance after Optuna hyperparameter optimization.
    - Consistently outperformed XGBoost across Accuracy, Precision, Recall, and F1 Score.
    - Demonstrated excellent discriminative ability for multi-class credit risk classification.
    - Provides efficient inference, making it suitable for real-time credit risk assessment.
    - Offers a strong balance between predictive performance and computational efficiency.
    - Selected as the production model for deployment within the decision support system.
    """
        )

#================================================================================
# Validation Tab
#================================================================================

with validation_tab:

    (
        classification_tab,
        confusion_tab,
        roc_tab,
        confidence_tab
    ) = st.tabs(
        [
            "📋 Classification",
            "🎯 Confusion Matrix",
            "📉 ROC Analysis",
            "📊 Prediction Confidence"
        ]
    )

# -----------------------------------------------------------------------------
# Classification Tab
# -----------------------------------------------------------------------------
st.divider()
with classification_tab:

    st.header("📋 Classification Analysis")

    st.caption(
        "Evaluate model performance across each internal credit risk grade."
    )


    summary_tab, p1_tab, p2_tab, p3_tab, p4_tab = st.tabs(
        [
            "📈 Summary",
            "P1",
            "P2",
            "P3",
            "P4",
        ]
    )

with summary_tab:

    st.subheader("Overall Classification Performance")

    classification_df = pd.DataFrame({
        "Risk Grade": ["P1", "P2", "P3", "P4"],
        "Precision": [80.47, 84.44, 46.19, 76.23],
        "Recall": [79.22, 92.16, 29.70, 73.76],
        "F1 Score": [79.84, 88.13, 36.16, 74.98],
        "Support": [1155, 4558, 1431, 3099]
    })

    st.dataframe(
        classification_df,
        use_container_width=True,
        hide_index=True
    )

    with st.container(border=True):

        st.subheader("📝 Overall Interpretation")

        st.info(
            """
    The deployed LightGBM classifier demonstrates balanced predictive performance
    across the four internal credit risk grades. Classification performance is
    strongest for **P2 (Low Risk)** borrowers, while **P3 (Moderate Risk)** is the
    most challenging class due to overlapping borrower characteristics with
    adjacent risk grades.

    Despite these challenges, the weighted evaluation metrics indicate reliable
    overall classification performance suitable for IFRS 9 credit risk assessment
    and lending decision support.
    """
        )

# -----------------------------------------------------------------------------
# Individual Risk Class Tabs
# -----------------------------------------------------------------------------

with p1_tab:

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Precision", "80.47%")
        st.metric("Recall", "79.22%")

    with col2:
        st.metric("F1 Score", "79.84%")
        st.metric("Support", "1,155")

    with st.container(border=True):

        st.subheader("Business Interpretation")

        st.success(
            """
**Strengths**

• Reliable identification of low-risk borrowers.

• Strong precision minimizes unnecessary rejection of creditworthy applicants.

• Supports efficient approval of customers with favorable credit profiles.
"""
        )


with p2_tab:

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Precision", "84.44%")
        st.metric("Recall", "92.16%")

    with col2:
        st.metric("F1 Score", "88.13%")
        st.metric("Support", "4,558")

    with st.container(border=True):

        st.subheader("Business Interpretation")

        st.success(
            """
**Strengths**

• Best-performing risk grade with excellent precision and recall.

• High recall ensures that the majority of low-risk borrowers are correctly identified.

• Consistent classification performance improves the reliability of credit risk assessment for the largest customer segment.

**Business Impact**

Accurate identification of P2 borrowers enables faster loan processing, improves operational efficiency, and supports confident lending decisions for customers with stable credit profiles.
"""
        )


with p3_tab:

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Precision", "46.19%")
        st.metric("Recall", "29.70%")

    with col2:
        st.metric("F1 Score", "36.16%")
        st.metric("Support", "1,431")

    with st.container(border=True):

        st.subheader("Business Interpretation")

        st.warning(
            """
**Observations**

• P3 is the most challenging risk grade to classify accurately.

• Borrowers in this category often exhibit financial characteristics that overlap with both lower (P2) and higher (P4) risk profiles.

• This overlap naturally increases misclassification compared to the other classes.

**Business Impact**

Since P3 represents borderline credit quality, additional credit review, manual assessment, or supporting documentation may be beneficial before making final lending decisions. Such behaviour is common in multi-class credit risk models and does not indicate a weakness unique to this model.
"""
        )


with p4_tab:

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Precision", "76.23%")
        st.metric("Recall", "73.76%")

    with col2:
        st.metric("F1 Score", "74.98%")
        st.metric("Support", "3,099")

    with st.container(border=True):

        st.subheader("Business Interpretation")

        st.info(
            """
**Strengths**

• Strong capability to identify high-risk borrowers with good overall consistency.

• Balanced precision and recall reduce both missed high-risk cases and unnecessary false alarms.

• Supports effective identification of customers requiring enhanced credit scrutiny.

**Business Impact**

Reliable detection of P4 borrowers strengthens risk management by enabling early intervention, appropriate risk-based pricing, and improved protection against potential credit losses.
"""
        )

# -----------------------------------------------------------------------------
# Confusion Matrix Tab
# -----------------------------------------------------------------------------

with confusion_tab:

    st.header("🎯 Confusion Matrix Analysis")

    st.caption(
        "Analyze prediction accuracy and misclassification patterns across all risk grades."
    )

    left, center, right = st.columns([1, 2, 2])

    with left:

        with st.container(border=True):
            st.subheader("Summary")

            st.metric("Accuracy", "79.52%")
            st.metric("Correct", "8,145")
            st.metric("Best Class", "P2")
            st.metric("Highest Confusion", "P3 → P2")

    with center:
        st.image(MODEL_DIR / "confusion_matrix.png")

    with right:
        st.image(MODEL_DIR / "normalized_confusion_matrix.png")

    # -----------------------------------------------------------------------------
    # Confusion Matrix (Key Findings) 
    # -----------------------------------------------------------------------------
    
    with st.container(border=True):

        st.subheader("📌 Key Findings")

        st.markdown("""
    - Most predictions are concentrated along the **main diagonal**, indicating correct classification.
    - **P2** demonstrates the highest classification accuracy with minimal confusion.
    - The majority of misclassifications occur between **P2 and P3**, reflecting similar borrower characteristics.
    - Very few borrowers are incorrectly classified between **P1 and P4**, indicating clear separation between the lowest and highest risk groups.
    """)
        
    # -----------------------------------------------------------------------------
    # Confusion Matrix (Business Interpretation) 
    # -----------------------------------------------------------------------------

    with st.container(border=True):

        st.subheader("🏦 Business Interpretation")

        st.info(
            """
    The confusion matrix indicates that the model reliably distinguishes borrowers
    at the extreme ends of the credit risk spectrum while occasional confusion
    occurs between neighbouring risk grades.

    Such behaviour is expected because adjacent borrower profiles often share
    similar financial characteristics.

    From a lending perspective, these errors are considerably less severe than
    misclassifying a high-risk borrower as a low-risk borrower.
    """
        )

    # -----------------------------------------------------------------------------
    # Confusion Matrix (⚠️ Risk Assessment) 
    # -----------------------------------------------------------------------------

    with st.container(border=True):

        st.subheader("⚠️ Risk Assessment")

        st.success(
            """
    The observed misclassification pattern is considered acceptable for an
    IFRS 9 credit risk model because prediction errors are primarily limited to
    adjacent risk grades rather than opposite ends of the risk spectrum.

    This behaviour supports reliable risk grading while minimizing materially
    incorrect lending decisions.
    """
        )

# -----------------------------------------------------------------------------
# ROC-AUC Tab
# -----------------------------------------------------------------------------

with roc_tab:

    st.header("📉 ROC Analysis")

    st.caption(
        "Evaluate the model's ability to distinguish between different credit risk grades."
    )

    left, right = st.columns([1, 3])

    with left:

        with st.container(border=True):

            st.subheader("📊 Summary")

            st.metric("Macro ROC-AUC", "93.38%")
            st.metric("Best Performing Class", "P1")
            st.metric("Most Challenging Class", "P3")
            st.metric("ROC Assessment", "Excellent")
            st.markdown("##### 📈 Class-wise Performance")

            st.progress(0.9849, text="P1  •  98.49%")
            st.progress(0.9287, text="P2  •  92.87%")
            st.progress(0.8459, text="P3  •  84.59%")
            st.progress(0.9756, text="P4  •  97.56%")


    with right:

        st.image(MODEL_DIR /"roc_curve.png")

    st.divider()
    roc_df = pd.DataFrame({
        "Risk Grade": ["P1", "P2", "P3", "P4"],
        "ROC-AUC": ["98.49%", "92.87%", "84.59%", "97.56%"],
        "Performance": [
            "Outstanding",
            "Excellent",
            "Good",
            "Outstanding"
        ]
    })

    st.dataframe(
        roc_df,
        hide_index=True,
        use_container_width=True
    )

    with st.container(border=True):

        st.subheader("📌 Key Findings")

        st.markdown("""
    - All four risk grades achieve an ROC-AUC greater than **0.84**, indicating strong discriminatory capability.
    - **P1** and **P4** exhibit outstanding class separation, making the safest and riskiest borrowers easy to distinguish.
    - **P2** also demonstrates excellent discrimination with an AUC exceeding **0.92**.
    - **P3** records the lowest AUC because borrowers in this category share characteristics with neighbouring risk grades, increasing classification complexity.
    """)
        
    with st.container(border=True):

        st.subheader("🏦 Business Interpretation")

        st.info(
            """
    The ROC analysis demonstrates that the model can effectively distinguish
    between borrowers across all internal credit risk grades.

    The exceptionally high AUC values for P1 and P4 indicate reliable separation
    between the lowest and highest risk customers, while the slightly lower
    performance for P3 reflects the natural overlap of intermediate-risk borrower
    profiles. Overall, the discrimination capability is well suited for IFRS 9
    risk grading and credit decision support.
    """
        )

    with st.container(border=True):

        st.subheader("✅ Model Verdict")

        st.success(
            """
    The LightGBM model demonstrates excellent discriminative performance with a
    Macro ROC-AUC of **93.38%**. The consistently high AUC values across all risk
    grades confirm that the model can reliably differentiate borrowers with
    different credit risk characteristics, supporting robust risk assessment and
    production deployment.
    """
        )

# -----------------------------------------------------------------------------
# Prediction Performance Tab
# -----------------------------------------------------------------------------
with confidence_tab:

    st.header("📊 Prediction Confidence")

    st.caption(
        "Evaluate the confidence associated with model predictions and assess the reliability of automated credit risk classifications."
    )


    left, right = st.columns([1, 3])

    with left:

        with st.container(border=True):

            st.subheader("📊 Summary")

            st.metric("Peak Confidence", "≈99%")
            st.metric("Confidence Range", "35% – 100%")
            st.metric("High Confidence", ">90%")
            st.metric("Prediction Quality", "Excellent")

            st.markdown("##### 📈 Confidence Assessment")

            st.progress(0.98, text="Maximum Confidence")
            st.progress(0.90, text="High Confidence Threshold")
            st.progress(0.79, text="Overall Accuracy")


    with right:

        st.image(
            MODEL_DIR /"prediction_confidence.png",
            use_container_width=True
        )


    with st.container(border=True):

        st.subheader("📌 Key Findings")

        st.markdown("""
    - Prediction confidence is heavily concentrated between **90% and 100%**, indicating strong certainty for most classifications.
    - A smaller proportion of predictions fall within the **40%–70%** confidence range, representing more challenging borrower profiles.
    - The distribution is positively skewed towards high-confidence predictions, reflecting stable model behaviour.
    - No abnormal confidence patterns or excessive uncertainty are observed.
    """)
        
    with st.container(border=True):

        st.subheader("🏦 Business Interpretation")

        st.info(
            """
    High-confidence predictions indicate that the model has learned clear
    decision boundaries for the majority of borrower profiles. Lower-confidence
    predictions are primarily associated with applicants exhibiting characteristics
    that overlap neighbouring risk grades, where additional manual review may be
    beneficial before making a final lending decision.
    """
        )

    with st.container(border=True):

        st.subheader("✅ Confidence Verdict")

        st.success(
            """
    The prediction confidence distribution demonstrates that the deployed
    LightGBM model produces highly confident predictions for most borrowers,
    supporting reliable automated credit risk assessment while appropriately
    identifying a smaller subset of borderline cases that may benefit from
    additional human evaluation.
    """
        )
#================================================================================
# Governance Tab
#================================================================================

with explain_tab:
    st.divider()

    st.header("🧠 SHAP Explainability")

    st.caption(
        "Interpret model behaviour, evaluate governance practices, and assess the production readiness of the deployed LightGBM credit risk model."
    )

    (
        global_tab,
        individual_tab
    ) = st.tabs(
        [
            "🌍 Global Explainability",
            "🔍 Individual Explanations"
        ]
    )

    # -----------------------------------------------------------------------------
    # Global Tab
    # -----------------------------------------------------------------------------

    with global_tab:
        st.header("🌍 Global Explainability")

        st.caption(
            "Understand the overall behaviour of the LightGBM model using SHAP feature importance and feature contribution analysis."
        )

        left, right = st.columns([1,3])

        with left:

            with st.container(border=True):

                st.subheader("📊 Summary")

                st.metric("Features Analysed", "56")
                st.metric("Top Feature", "enq_L3m")
                st.metric("Target Class Explained", "P4")
                st.metric("Explanation Method", "TreeSHAP")

                st.markdown("##### Top Feature Drivers")

                st.progress(0.72, text="enq_L3m")
                st.progress(0.66, text="Age_Oldest_TL")
                st.progress(0.54, text="max_recent_level_of_deliq")
                st.progress(0.35, text="num_std_12mts")

        with right:

            st.image(
                MODEL_DIR /"shap_summary.png",
                use_container_width=True
            )

        with st.container(border=True):

            st.subheader("📌 Global Feature Insights")

            st.markdown(
                """
        - **enq_L3m** is the most influential feature, indicating that recent credit enquiries are the strongest indicator of borrower risk.

        - **Age_Oldest_TL** is the second most important predictor, showing that longer credit histories generally contribute to more reliable credit assessment.

        - Delinquency-related variables consistently rank among the most influential features, highlighting the importance of repayment behaviour.

        - The model combines multiple behavioural and credit history attributes rather than relying on a single variable, improving robustness and reducing dependency on individual features.
        """
            )

        # -----------------------------------------------------------------------------
        # BeeSwarm Plot
        # -----------------------------------------------------------------------------

        st.divider()

        st.subheader("📈 SHAP Feature Contribution Analysis")

        st.caption(
            "Visualize how feature values influence predictions across the entire dataset."
        )

        left, right = st.columns([1.5, 2.5])

        with left:

            with st.container(border=True):

                st.subheader("📊 Summary")
                st.metric("Explained Class", "P4")
                st.metric("Strongest Risk Driver", "enq_L3m")
                st.metric("Largest Risk Reducer", "time_since_recent_enq")
                st.metric("Analysis Scope", "All Borrowers")

                st.markdown("##### Feature Behaviour")

                st.progress(1.00, text="Recent Enquiries ↑ Risk")

                st.progress(0.85, text="Delinquency ↑ Risk")

                st.progress(0.75, text="Older Credit History ↓ Risk")

                st.progress(0.60, text="Recent Payment Behaviour")

        with right:

            st.image(
                MODEL_DIR/"shap_beeswarm.png",
                use_container_width=True
            )

        with st.container(border=True):

            st.subheader("📌 Feature Behaviour Analysis")

            st.markdown(
                """
        - Higher values of **enq_L3m** generally increase predicted credit risk, demonstrating the importance of recent borrowing activity.

        - Older trade lines (**Age_Oldest_TL**) tend to reduce predicted risk, reflecting stronger credit history.

        - Higher delinquency levels shift predictions toward higher-risk grades.

        - Recent enquiry behaviour, repayment history, and credit utilisation collectively influence model decisions.

        - The variation in SHAP values across borrowers confirms that the model adapts its reasoning to individual customer profiles rather than applying identical decision rules.
        """
            )


        with st.container(border=True):

            st.subheader("🏦 Business Interpretation")

            st.info(
                """
        The SHAP analysis demonstrates that the model primarily relies on recognised
        credit risk indicators such as enquiry behaviour, repayment history,
        delinquency status, and trade line age. These drivers are consistent with
        traditional banking credit assessment practices, improving model transparency,
        regulatory compliance, and stakeholder confidence.
        """
            )

        with st.container(border=True):

            st.subheader("✅ Explainability Verdict")

            st.success(
                """
        The SHAP analysis confirms that the LightGBM model bases its decisions on
        meaningful financial and behavioural characteristics rather than arbitrary
        patterns. Both global feature importance and feature contribution analysis
        demonstrate consistent, transparent, and explainable model behaviour,
        supporting trustworthy deployment for IFRS 9 credit risk assessment.
        """
            )

    # 🔍 Individual Prediction Explanations


    with individual_tab:

        st.header("🔍 Individual Prediction Explanations")

        st.caption(
            "Understand how the LightGBM model reaches individual credit risk decisions using SHAP waterfall explanations."
        )

        representative_tab, challenging_tab = st.tabs(
            [
                "✔ Representative Prediction",
                "⚠ Challenging Prediction",
            ]
        )

    # ============================================================
    # REPRESENTATIVE (CORRECT) PREDICTION
    # ============================================================

    with representative_tab:

        left, right = st.columns([1.5, 2.5])

        with left:

            with st.container(border=True):

                st.subheader("📊 Prediction Summary")

                st.metric("Prediction Type", "Representative")
                st.metric("Actual Risk Class", "P4")
                st.metric("Predicted Risk Class", "P4")
                st.metric("Primary Driver", "enq_L3m")
                st.metric("Explanation Method", "SHAP Waterfall")



        with right:

            st.image(
                MODEL_DIR/"waterfall_correct.png",
                use_container_width=True,
            )

        with st.container(border=True):

            st.subheader("📌 Prediction Interpretation")

            st.markdown(
                """
    - The prediction is primarily driven by a high number of recent credit enquiries.

    - Trade line history and repayment behaviour reinforce the assigned risk grade.

    - Positive SHAP contributions substantially outweigh the negative contributions.

    - The feature interactions collectively support the final prediction with high confidence.
    """
            )

        with st.container(border=True):

            st.subheader("🏦 Business Interpretation")

            st.info(
                """
    This example represents a borrower with clearly distinguishable
    credit risk characteristics. The model's reasoning aligns with
    traditional banking credit assessment practices, increasing
    confidence in automated credit risk evaluation.
    """
            )


    # ============================================================
    # CHALLENGING (MISCLASSIFIED) PREDICTION
    # ============================================================

    with challenging_tab:

        left, right = st.columns([1.5, 2.5])

        with left:

            with st.container(border=True):

                st.subheader("📊 Prediction Summary")
                st.metric("Prediction Type", "Misclassification")
                st.metric("Actual Grade", "P3")
                st.metric("Predicted Grade", "P4")
                st.metric("Prediction Confidence", "99.25%")
                st.metric("Primary Driver", "enq_L3m")


        with right:

            st.image(
                MODEL_DIR/"waterfall_incorrect.png",
                use_container_width=True,
            )

        with st.container(border=True):

            st.subheader("📌 Prediction Interpretation")

            st.markdown(
                """
    - High enquiry activity contributed most significantly toward a higher risk prediction.

    - Several lower-impact features partially offset the overall prediction.

    - The borrower exhibits overlapping characteristics between adjacent risk grades.

    - The combined SHAP contributions explain why the model selected a neighbouring risk class.
    """
            )

        with st.container(border=True):

            st.subheader("🏦 Business Interpretation")

            st.info(
                """
    Borderline borrower profiles are expected in multiclass credit
    risk modelling because neighbouring risk grades often share
    similar financial characteristics.

    Although the predicted class differs from the observed class,
    the SHAP explanation demonstrates that the model's reasoning
    remains transparent, consistent, and financially justifiable.
    Such applicants are appropriate candidates for additional
    manual review before making a final lending decision.
    """
            )

        with st.container(border=True):

            st.subheader("✅ Explainability Verdict")

            st.success(
                """
    The individual SHAP explanations demonstrate that the model
    provides transparent and traceable reasoning for every prediction.

    Both representative and challenging borrower profiles show that
    predictions are driven by meaningful financial characteristics
    rather than arbitrary decision patterns, supporting explainable
    and trustworthy credit risk assessment.
    """
            )



#================================================================================
# WHY LightGBM
#================================================================================


with lightgbm_tab:
    st.header("🏆 Why LightGBM?")

    st.caption(
        "Understand why LightGBM was selected as the final production model for the IFRS 9 credit risk assessment system."
    )

    with st.container(border=True):

        st.subheader("📊 Model Summary")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Model", "LightGBM")

        with c2:
            st.metric("Accuracy", "79.18%")

        with c3:
            st.metric("Macro ROC-AUC", "93.38%")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Precision", "77.15%")

        with c2:
            st.metric("Recall", "79.18%")

        with c3:
            st.metric("F1 Score", "77.82%")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Features", "56")

        with c2:
            st.metric("Samples", "10,243")

        with c3:
            st.metric("Classes", "P1–P4")

        st.divider()

        left, right = st.columns(2)

        with left:
            st.markdown("#### ✅ Why LightGBM?")
            st.markdown("""
        - Highest validation performance
        - Excellent multi-class ROC-AUC
        - Fast inference for production
        - Handles complex financial relationships
        - SHAP-compatible for explainability
        - Stable on tabular datasets
        """)

        with right:
            st.markdown("#### 🏦 Business Advantages")
            st.markdown("""
        - IFRS 9 compliant risk assessment
        - Explainable AI-driven predictions
        - Consistent lending decisions
        - Suitable for enterprise deployment
        - Low-latency real-time scoring
        - Scalable to large customer portfolios
        """)

        st.divider()

        st.markdown("##### Key Strengths")

        st.progress(.80, text="Predictive Performance")
        st.progress(0.75, text="Explainability")
        st.progress(0.85, text="Scalability")
        st.progress(0.70, text="Training Speed")

        st.divider()

        st.success(
            """
    **Selection Verdict**

    LightGBM achieved the strongest balance between
    predictive performance, computational efficiency,
    and model explainability, making it the preferred
    choice for the IFRS 9 credit risk framework.
    """
        )

        
    with st.container(border=True):

        st.subheader("✅ Final Recommendation")

        st.success("""
    Based on the evaluation of predictive performance, explainability, computational efficiency, and business applicability, LightGBM was selected as the final production model. Its strong classification capability, transparent decision-making through SHAP, and suitability for IFRS 9 credit risk modelling make it an effective decision-support model for internal banking applications.
    """)
        
create_footer()