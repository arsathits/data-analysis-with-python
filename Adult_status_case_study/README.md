# Adult Status Case Study

## 📌 Overview
This project performs **data cleaning, exploration, and analysis** on the Adult Income dataset to understand demographic and work-related factors affecting income levels.  
The dataset is sourced from the UCI Machine Learning Repository and contains census information.

## 📊 Key Steps in the Notebook
1. **Data Loading**
   - Reads `adult.csv` dataset into Pandas.

2. **Initial Exploration**
   - Shape, data types, null value checks.
   - Random sampling preview.

3. **Data Cleaning**
   - Replaces `'?'` placeholders with `NaN`.
   - Drops rows with missing values.
   - Removes duplicates.
   - Drops irrelevant columns (`educational-num`, `capital-gain`, `capital-loss`).

4. **Exploratory Data Analysis (EDA)**
   - Distribution plots (Age, Workclass, Education, Occupation, etc.).
   - Filtering and counting specific categories (e.g., Bachelor's & Master's holders).
   - Categorical vs. target (`income`) visualizations.

5. **Insights**
   - Identifies trends in education, workclass, age groups, and their correlation with income.
