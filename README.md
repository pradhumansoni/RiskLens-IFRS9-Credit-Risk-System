# 🏦 RiskLens

> Machine Learning-Based IFRS 9 Credit Risk & Expected Credit Loss (ECL) Decision Support Platform

![Dashboard](screenshots/about_page.png)

---

## 📌 Overview

RiskLens is an end-to-end machine learning-based decision support platform developed to assist credit officers in evaluating loan applications using the IFRS 9 Expected Credit Loss (ECL) framework.

The application integrates predictive machine learning, explainable model interpretation, and banking business rules to deliver transparent, data-driven lending decisions.

---

## ✨ Features

- 🤖 Machine Learning-based Borrower Risk Prediction (LightGBM)
- 📊 IFRS 9 Expected Credit Loss (ECL) Estimation
- 📈 Probability of Default (PD), Loss Given Default (LGD) & Exposure at Default (EAD)
- 🏦 IFRS 9 Stage Classification
- 📋 Credit Decision Support Engine
- 🔄 Interactive What-If Analysis
- 🧠 SHAP-Based Model Explainability
- 📉 Comprehensive Model Validation Dashboard
- 🎯 Professional Streamlit Banking Interface

---

## 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Machine Learning | LightGBM, Scikit-learn |
| Explainability | SHAP |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Frontend | Streamlit |

---

# 📸 Application Showcase

## Dashboard

The landing page provides a high-level overview of the platform and quick access to its major modules.

![Dashboard](screenshots/dashboard.png)

---

## Loan Assessment & Decision Support

Retrieve customer information, evaluate borrower risk, calculate IFRS 9 metrics, generate lending recommendations, and perform scenario-based What-If Analysis.

![Loan Assessment](screenshots/full_loan_assessment.png)

---

## Model Development & Performance

Review the deployed LightGBM model, validation metrics, model comparison, and deployment rationale.

![Model Overview](screenshots/model_overview.png)

---

## Confusion Matrix Analysis

Analyze classification accuracy and misclassification patterns across all internal credit risk grades.

![Confusion Matrix](screenshots/validation_confusion.png)

---

## Global Explainability

Identify the most influential borrower characteristics using SHAP global feature importance.

![Global SHAP](screenshots/SHAP_global.png)

---

## Individual Prediction Explainability

Interpret individual borrower predictions using SHAP waterfall explanations for transparent credit risk assessment.

![Local SHAP](screenshots/SHAP_local.png)

---

## About the Application

Explore the project architecture, technology stack, workflow, and implementation overview.

![About](screenshots/about_page.png)

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/RiskLens.git

cd RiskLens

pip install -r requirements.txt

streamlit run app.py
```

---

## 📂 Project Structure

```text
RiskLens/
│
├── app.py
├── pages/
├── src/
├── models/
├── data/
├── notebooks/
├── assets/
├── requirements.txt
└── README.md
```

---

## 🎯 Project Highlights

- End-to-end Machine Learning workflow
- Explainable Credit Risk Modelling using SHAP
- IFRS 9 Expected Credit Loss (ECL) Framework
- Interactive Banking Decision Support Platform
- Modular Streamlit Application
- Production-inspired Software Architecture

---

## 📜 Disclaimer

This project was developed for educational and portfolio purposes. The IFRS 9 implementation is a simplified demonstration intended to showcase machine learning, explainability, and decision support concepts rather than serve as a production-ready banking solution.

---

## 👨‍💻 Author

**Pradhuman Kumar Soni**

*M.Sc. Mathematics & Scientific Computing*

Machine Learning • Credit Risk Analytics • Financial Modelling • Data Science
