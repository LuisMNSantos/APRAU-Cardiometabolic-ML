# Cardiometabolic Disease Prediction — APRAU 2026/27

**Machine Learning assignment** for the course *Aprendizagem Automática* (APRAU), MEI — ISEP, 2026/2027.

## Overview

This project applies classical machine learning methods to a clinical dataset of **2,000 patient records** derived from a cardiometabolic disease screening program. The dataset contains demographic, anthropometric, lifestyle, and laboratory biomarker features, with two target variables:

- `target_class` — categorical diagnosis label (classification task)
- `target_regression` — continuous laboratory biomarker (regression task)

## Project Structure

```
Projeto/
├── dataset_grupo_18.csv                  # Dataset (2000 patient records, excluded from VCS)
├── Trabalho_APRAU_2026_27_step1.pdf      # Assignment specification
├── notebooks/
│   └── aprau_grupo18.ipynb               # Main project notebook (all tasks)
├── requirements.txt
└── README.md
```

## Tasks

### 1. Exploratory Data Analysis (EDA)
- Descriptive statistics
- Univariate analysis (distribution of individual features)
- Bivariate analysis (correlations between features and target variables)
- Identification and removal of uninformative, constant, or redundant features
- Multicollinearity assessment via VIF
- Data treatment and export of cleaned dataset

### 2. Regression — predicting `target_regression`
- **Simple Linear Regression** — single feature selection and evaluation
- **Multiple Linear Regression** — feature combination exploration
- Evaluation: R², MAE, RMSE (holdout method)

### 3. Classification — predicting `target_class`
- Methods: **Logistic Regression** and **Discriminant Analysis (LDA)**
- Resampling strategies:
  - Holdout
  - Stratified Cross-Validation (k=5 and k=10)
  - Leave-One-Out Cross-Validation (LOOCV)
  - Bootstrap (OOB estimate)
- Analysis of how variance is affected by each resampling method

### 4. Feature Selection
- Regularization methods: **Ridge** (L2), **Lasso** (L1), and **Elastic Net** (L1+L2)
- Automatic hyperparameter tuning via cross-validation (`RidgeCV`, `LassoCV`, `ElasticNetCV`)
- Post-selection VIF analysis
- Comparison between full-feature and reduced-feature models
- Discussion of impact on classification performance

## Dataset Features

| Category | Features |
|---|---|
| Demographics | `age`, `age_normalized`, `age_level`, `gender`, `education_level`, `employment_status` |
| Anthropometric | `bmi`, `bmi_level` |
| Lifestyle | `smoking`, `physical_activity`, `stress_level`, `sleep_hours`, `alcohol_intake`, `salt_intake`, `sugar_consumption`, `family_history` |
| Blood Pressure | `systolic_bp`, `diastolic_bp`, `blood_pressure`, `systolic_index` |
| Lipid Profile | `cholesterol`, `triglycerides`, `hdl`, `ldl`, `low_hdl_cholesterol`, `high_ldl_cholesterol`, `ldl_alternative` |
| Clinical Biomarkers | `heart_rate`, `HbA1c_level`, `crp_level`, `homocysteine_level`, `calcium_baseline`, `plasma_value` |
| Targets | `target_class`, `target_regression` |

## Deadlines

| Submission | Date | Weight |
|---|---|---|
| Intermediate | 2 November 2026 | 25% of final grade |
| Final | 20 December 2026 | 45% of final grade |

> Individual defense accounts for **70% of the project grade**.

## Requirements

```
python >= 3.10
numpy
pandas
matplotlib
seaborn
scikit-learn
scipy
jupyter
```

Install with:

```bash
pip install -r requirements.txt
```

## Group

ISEP | MEI | APRAU | 2026/2027 — Group 18
