# Developer & Agent Guidance: IFRS 9 Credit Risk Rating & ECL System

This document serves as an exhaustive, step-by-step master plan and technical blueprint for an automated agent or developer tasked with building a production-grade, IFRS 9-compliant Credit Risk Rating and Expected Credit Loss (ECL) system.

---

## 1. Project Overview & Context

### Core Objective
The target of this system is to classify retail/commercial borrowers into specific risk grades (**P1, P2, P3, P4**) via a predictive modeling framework using the target variable `Approved_Flag`. These risk grades are then translated into standard **IFRS 9 metrics**:
* **Probability of Default (PD)**
* **Loss Given Default (LGD)**
* **Exposure at Default (EAD)**
* **Stage Classification** (Stages 1, 2, and 3)
* **Expected Credit Loss (ECL)** calculation and aggregation

### Technical Framework
* **Backend & Core Language:** Python (Pandas, NumPy, Scikit-Learn, XGBoost)
* **API Layer:** FastAPI (for programmatic scoring, ECL generation, and analytical queries)
* **UI Layer:** Streamlit (interactive dashboards for scoring, ECL modeling, and portfolio-wide stress testing)

---

## 2. Structural Requirements for Every Phase

For every chapter and milestone executed, the agent or developer **must** explicitly document and implement the following seven core governance anchors:
1.  **Objective:** Clear business and technical goal for the specific module.
2.  **Inputs:** Precise datasets, parameters, or upstream variables required.
3.  **Outputs:** Formatted dataframes, artifacts, model weights, or metrics produced.
4.  **Assumptions:** Analytical or regulatory assumptions made (critical for audit transparency).
5.  **Validation Checks:** Unit tests, data assertions, or metric benchmarks to guarantee correctness.
6.  **Risks & Mitigation:** Potential failure points (e.g., data leakage, systemic overfitting, numeric underflow) and defensive solutions.
7.  **Deliverables:** Specific code modules (`.py` files), serializations (`.pkl`), or reporting tables generated.

---

## 3. End-to-End Chapter Execution Playbook

### Phase I: Data Foundations & Preprocessing

#### Chapter 1: Dataset Overview & Ingestion
* **Task:** Establish the ingestion pipeline for the primary datasets (`case_study1` and `case_study2`) totaling 51,336 customer records.
* **Details:** * `case_study1`: Map and parse bureau trade-line features, including `Total_TL`, `Active_TL`, `Closed_TL`, secured vs. unsecured credit flags, and account maturity/age metrics.
    * `case_study2`: Parse behavioral variables, including delinquency histories, hard/soft enquiry records, credit card/line utilization flags, monthly income (`NETMONTHLYINCOME`), credit scores, and the modeling target `Approved_Flag`.
* **Validation:** Verify relational integrity using `PROSPECTID` as the primary key.

#### Chapter 2: Business Objective & Target Mapping
* **Task:** formalize the relationship between multi-class grading (`P1-P4`) and portfolio underwriting risk.
* **Details:** Isolate `Approved_Flag` as the absolute optimization target. Set up the operational ledger mapping model output probabilities to specific risk tiers.

#### Chapter 3: Data Dictionary Strategy
* **Task:** Build an automated data dictionary.
* **Details:** Standardize and programmatically tag every column into six core functional domains: Bureau, Delinquency, Enquiry, Utilization, Demographic, and Exposure.

#### Chapter 4: Data Quality Checks (DQC)
* **Task:** Establish an automated defensive cleaning pipeline.
* **Details:** Implement explicit checks and structural overrides for:
    * Missing values and imputation logic.
    * Duplicate `PROSPECTID` identification and removal.
    * Outlier detection using robust statistical bounds (e.g., IQR or percentiles for income).
    * Impossible values (e.g., negative account age or utilization > 1000%).
    * Skewed feature transformations.

#### Chapter 5: Exploratory Data Analysis (EDA)
* **Task:** Generate visual and statistical insights of primary risk drivers.
* **Details:** Code profiling scripts for distributions of `Credit_Score`, `NETMONTHLYINCOME`, credit card utilization rates, historical delinquency timelines, and base target class proportions.

---

### Phase II: Feature Engineering & Mathematical Transformation

#### Chapter 6: Feature Engineering Pipeline
* **Task:** Construct reproducible feature transformation blocks.
* **Details:** Derived features must explicitly include:
    * **Utilization Buckets:** Categorical/ordinal transformations of balance-to-limit ratios.
    * **Delinquency Intensity:** Rolling windows or velocity tracking of past-due events.
    * **Account Maturity Metrics:** Derived interaction terms between account age and credit types.
    * **Secured-Unsecured Ratios:** Structural calculation of exposure distributions.
    * **Enquiry Intensity Scores:** Rolling short-term vs. long-term credit seeking indicators.

#### Chapter 7: Weight of Evidence (WOE) Framework
* **Task:** Convert raw continuous and categorical variables into monotonic risk spaces.
* **Details:** Perform optimal supervised binning on engineered attributes. Transform values to WOE scale based on target distributions, ensuring strict monotonic trends relative to risk grades wherever possible to satisfy regulatory interpretability.

#### Chapter 8: Information Value (IV) Filtering
* **Task:** Conduct programmatic feature selection.
* **Details:** Calculate the Information Value (IV) for all WOE-transformed features. Rank variables and apply strict drop thresholds (e.g., drop if IV < 0.02, monitor for overfitting if IV > 0.5) to keep the final modeling table mathematically lean and robust.

---

### Phase III: Model Development & Evaluation

#### Chapter 9: Core Modeling Suite
* **Task:** Train and cross-validate the complete benchmarking model matrix.
* **Details:** Implement, tune, and persist the following algorithms:
    * Regularized Logistic Regression (as the classic scorecard baseline)
    * k-Nearest Neighbors (KNN)
    * Decision Trees
    * Random Forest
    * XGBoost (optimized via multi-class hyperparameter search)

#### Chapter 10: Model Evaluation & Misclassification Analysis
* **Task:** Execute multi-dimensional model diagnostics.
* **Details:** Evaluate performance using multi-class Accuracy, Macro/Micro F1-scores, and complete Confusion Matrices. Conduct a deep-dive misclassification analysis to evaluate adjacent-class errors (e.g., P1 misclassified as P2 vs. P1 misclassified as P4).

---

### Phase IV: IFRS 9 Accounting Engine Design

#### Chapter 11: IFRS 9 Framework Architecture
* **Task:** Wire the end-to-end accounting pipeline logic.
* **Details:** Connect downstream processing blocks in sequence: `Risk Grade Prediction` $ightarrow$ `PD Mapping` $ightarrow$ `LGD Generation` $ightarrow$ `EAD Generation` $ightarrow$ `Stage Assignment` $ightarrow$ `ECL Core Calculation`.

#### Chapter 12: PD Mapping & Calibration
* **Task:** Map predicted risk grades to operational Probabilities of Default.
* **Details:** Set up baseline anchors: **P1 = 1%**, **P2 = 3%**, **P3 = 8%**, and **P4 = 20%**. Code a calibration overlay that takes continuous multi-class model output probabilities and fits them to empirical historical default curves.

#### Chapter 13: LGD Methodology
* **Task:** Calculate Loss Given Default parameters.
* **Details:** Apply structural pricing and security hair-cuts. Assign lower LGD to secured products (mortgage, asset-backed) and high LGD to unsecured instruments (personal loans, credit cards). Integrate parameter sensitivity bands to stress recovery expectations.

#### Chapter 14: EAD Methodology
* **Task:** Model dynamic Exposure at Default across portfolio categories.
* **Details:** Combine nominal balance sheets, credit conversion factors (CCF) for undrawn limits, and utilization metrics to accurately estimate total absolute exposure at the moment of default.

#### Chapter 15: Stage Assignment Logic
* **Task:** Build the IFRS 9 three-stage classification engine.
* **Details:** Imbed logic thresholds:
    * **Stage 1:** Low credit risk or stable performance (12-month ECL applied).
    * **Stage 2:** Significant Increase in Credit Risk (SICR) triggered by rating downgrades, utilization spikes, or behavioral deterioration (Lifetime ECL applied).
    * **Stage 3:** High risk / Credit Impaired / Default assets (Lifetime ECL applied, interest calculated on net basis).

#### Chapter 16: ECL Engine Implementation
* **Task:** Code the matrix engine for expected credit loss calculations.
* **Details:** Program the core equation: 
    $$	ext{ECL} = 	ext{PD} 	imes 	ext{LGD} 	imes 	ext{EAD}$$
    Provide full capabilities to aggregate calculations up from individual contractual accounts to specific segments and entire portfolio structures.

#### Chapter 17: Macroeconomic Stress Testing
* **Task:** Build forward-looking macroeconomic overlay modules.
* **Details:** Define scenario frameworks across three standard paths: **Base, Optimistic, and Pessimistic**. Code macroeconomic shock parameters that mathematically shift the baseline PD and LGD distributions according to simulated downturn severity.

#### Chapter 18: Regulatory Validation Metrics
* **Task:** Code validation and stability metrics.
* **Details:** Program standard independent risk validation tests: Kolmogorov-Smirnov (KS) test, Gini Coefficient, Population Stability Index (PSI) to track feature/score drift over time, and Hosmer-Lemeshow goodness-of-fit tests.

---

### Phase V: Production Deployment & Interview Preparation

#### Chapter 19: FastAPI Core Backend Delivery
* **Task:** Develop the enterprise API gateway.
* **Details:** Expose production-ready REST endpoints for:
    * `/score`: Real-time borrower multi-class risk scoring.
    * `/ecl`: Real-time individual/batch Expected Credit Loss computation.
    * `/analytics`: Dynamic summary portfolio distributions and reporting aggregation.

#### Chapter 20: Streamlit Dashboard UI Delivery
* **Task:** Build the interactive corporate front-end.
* **Details:** Implement four dedicated, clean interactive layout pages:
    1.  *Customer Scoring Page:* Manual input forms and batch file processors for calculating risk grades.
    2.  *ECL Dashboard:* Granular breakdowns of portfolio provisions across Stage 1, 2, and 3.
    3.  *Portfolio Monitoring Page:* Real-time tracking of asset drift, PSI values, and metric tracking.
    4.  *Stress Testing Page:* Scenario controls to shift macroeconomic paths and instantly visualize updated provision levels.

#### Chapter 21: System Integrity & Interview Verification
* **Task:** Prepare core defense materials and logic validation reviews.
* **Details:** Document concise technical explanations and unit tests around WOE/IV selection bias, IFRS 9 timing rules (12-month vs. lifetime transitions), selection criteria for XGBoost over simple models, and real-time inference architectural choices.
