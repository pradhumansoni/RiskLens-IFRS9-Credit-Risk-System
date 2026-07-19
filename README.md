# 🏦 RiskLens

> AI-Powered IFRS 9 Credit Risk Assessment & Expected Credit Loss (ECL) Decision Support System

![Dashboard](screenshots/about_page.png)

---

## 📌 Overview

RiskLens is an end-to-end AI-powered decision support system developed to assist credit officers in evaluating loan applications using IFRS 9 Expected Credit Loss (ECL) methodology.

The application combines machine learning, explainable AI, and banking business rules to generate transparent, data-driven lending recommendations.

---

## ✨ Features

- 🤖 AI-powered borrower risk prediction (LightGBM)
- 📊 IFRS 9 Expected Credit Loss (ECL) estimation
- 📈 PD, LGD & EAD calculations
- 🏦 IFRS Stage Classification
- 📋 Credit Decision Support
- 🔄 Interactive What-If Analysis
- 🧠 SHAP Explainability
- 📉 Comprehensive Model Validation Dashboard
- 🎯 Professional Streamlit Interface

---

## 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Machine Learning | LightGBM, Scikit-learn |
| Explainable AI | SHAP |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Frontend | Streamlit |

---

# 📸 Application Showcase

## Dashboard

The landing page provides a high-level overview of the system and quick navigation to the major modules.

![Dashboard](screenshots/dashboard.png)

---

## Loan Assessment & Decision Support

Evaluate borrower profiles, estimate IFRS 9 metrics, generate lending decisions, and compare alternative loan scenarios using What-If Analysis.

![Loan Assessment](screenshots/full_loan_assessment.png)

---

## Model Development & Performance

Comprehensive overview of the deployed LightGBM model, validation metrics, and model selection process.

![Model Overview](screenshots/model_overview.png)

---

## Confusion Matrix Analysis

Detailed evaluation of classification performance across all internal credit risk grades.

![Confusion Matrix](screenshots/validation_confusion.png)

---

## Global Explainability

Understand which borrower characteristics contribute most to model predictions using SHAP feature importance.

![Global SHAP](screenshots/SHAP_global.png)

---

## Individual Prediction Explainability

Explain individual borrower predictions using SHAP waterfall analysis for transparent decision support.

![Local SHAP](screenshots/SHAP_local.png)

---

## About the Application

Project overview, architecture, workflow, and technology stack.

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
- Explainable AI using SHAP
- IFRS 9 compliant Expected Credit Loss framework
- Interactive banking decision support system
- Professional Streamlit application
- Production-inspired modular architecture

---

## 📜 Disclaimer

This project was developed for educational and portfolio purposes. The IFRS 9 implementation is a simplified demonstration intended to showcase machine learning, explainable AI, and decision support concepts rather than serve as a production-ready banking solution.

---

## 👨‍💻 Author

**Pradhuman Kumar Soni**

M.Sc. Mathematics & Scientific Computing

AI • Machine Learning • Credit Risk Analytics • Data Science
