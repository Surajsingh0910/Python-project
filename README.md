UCI Heart Disease Data Analytics – Exploratory Data Analysis


Project Overview

This project performs Exploratory Data Analysis (EDA) on the UCI Heart Disease dataset using Python, Pandas, NumPy, Matplotlib, and Seaborn.
The main objective is to analyze patient profiles, risk factors, and clinical measurements through data cleaning and visualization. It is an academic exercise and does not provide medical advice or diagnosis.

Dataset

Source: Heart Disease Data – Kaggle (from the UCI Machine Learning Repository)
The dataset combines about 900 patient records from four centres (Cleveland, Hungary, Switzerland, VA Long Beach). Key attributes:
• id, age, sex, dataset: patient ID, demographics, and medical centre.
• cp, exang: chest pain type and exercise-induced angina.
• trestbps, chol, fbs, restecg: resting blood pressure, cholesterol, fasting blood sugar, and resting ECG.
• thalch, oldpeak, slope, ca, thal: maximum heart rate, ST depression, ST slope, major vessels, and thalassemia.
• num: target value, where 0 means no heart disease and 1–4 mean increasing severity.

Objectives

1. Understand the dataset.
2. Handle missing values (ca, thal, slope, chol) and impossible values (zero cholesterol or blood pressure).
3. Create a heart disease flag (num = 0 vs num > 0).
4. Analyze the age and sex profile across medical centres.
5. Compare disease presence across sex, chest pain type, and angina.
6. Compare cholesterol, blood pressure, and heart rate by disease status.
7. Study relationships between the key measurements.
8. Create seven visualizations and interpret the patterns.

Graphs Included

1. Patient Age Distribution: histogram.
2. Heart Disease Presence: count plot / pie chart.
3. Heart Disease by Sex: grouped bar chart.
4. Chest Pain Type vs Heart Disease: grouped bar chart.
5. Age vs Maximum Heart Rate: scatter plot.
6. Cholesterol and Max Heart Rate by Disease Status: box plot.
7. Correlation Heatmap: age, blood pressure, cholesterol, heart rate, ST depression, and severity.

Technologies Used

• Python, Pandas, NumPy
• Matplotlib, Seaborn
• Google Colab / Jupyter Notebook
• Git & GitHub (both members contribute commits)

Analysis and Expected Outcomes

• What are the most common patient ages?
• What share of patients have heart disease?
• How does disease presence vary by sex and chest pain type?
• How do cholesterol, blood pressure, and heart rate differ by disease status?
• How are the clinical measurements related to each other?
The actual findings will be determined after running the analysis, and they describe this dataset only.

Conclusion

This project demonstrates how Python, Pandas, and Seaborn can turn raw clinical data into clear insights through cleaning, EDA, and visualization on a real-world healthcare dataset.

Dataset Credit

Redwan Karim Sony, Heart Disease Data (from the UCI Machine Learning Repository), Kaggle.
