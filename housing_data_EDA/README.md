# 🏡 Housing Prices – Exploratory Data Analysis

## 📌 Project Overview

This project is based on the Ames Housing dataset, which contains detailed information about residential homes. The goal of this project is to explore the data, identify key patterns, and prepare it for predictive modeling (such as house price prediction).

So far, I have completed **Exploratory Data Analysis (EDA)** and visualizations. The next steps will involve **data cleaning**.

---

## 📊 Dataset

* **Source**: Ames Housing dataset (Kaggle / OpenML)
* **File used**: `train.csv`
* **Shape**: 1460 rows × 81 columns
* **Target variable**: `SalePrice`

---

## 🔎 Exploratory Data Analysis (EDA)

Key steps covered in the notebook (`housing.ipynb`):

1. Data overview (shape, columns, datatypes)
2. Missing values check
3. Distribution of numerical features
4. Categorical variable analysis
5. Relationship between features and `SalePrice`
6. Correlation analysis
7. Outlier inspection
8. Key insights summary

---

## 📈 Visualizations

All plots generated during EDA are saved in the **`plots/`** folder. Examples include:

* Distribution of house prices
* Heatmap of correlations
* Scatter plots for numerical variables vs. `SalePrice`
* Count plots for categorical variables

---

## 🧹 Data Cleaning

The following data cleaning and preprocessing steps were performed in `02_data_cleaning.ipynb`:

* **Missing Values**: Handled by imputing `LotFrontage` and other numerical values with the median. Missing categorical values were also addressed, and the `Electrical` variable was imputed using the mode.
* **Data Types**: Ensured year-related data types were kept as integers.
* **Outliers**: Treated outliers by clipping using z-scores with custom thresholds.
* **Feature Transformation**: Skewed numeric features were transformed using `log1p`.
* **Duplicates**: Any duplicate rows found were removed.

The cleaned dataset is exported to `../dataset/cleaned_train.csv`.
