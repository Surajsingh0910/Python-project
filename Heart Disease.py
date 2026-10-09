import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Heart Disease Dataset
csv_data = """age,sex,cp,trestbps,chol,thalach,target
63,1,3,145,233,150,1
37,1,2,130,250,187,1
41,0,1,130,204,172,1
56,1,1,120,236,178,1
57,0,0,120,354,163,1
57,1,0,140,192,148,1
56,0,1,140,294,153,1
44,1,1,120,263,173,1
52,1,2,172,199,162,1
54,1,0,140,239,160,1
48,0,2,130,275,139,1
49,1,1,130,266,171,1
64,1,3,110,211,144,1
58,0,3,150,283,162,1
50,0,2,120,219,158,1
58,1,2,132,224,173,1
65,1,0,150,225,114,0
44,1,0,120,169,144,0
59,1,0,170,326,140,0
61,0,0,130,330,169,0
56,1,0,125,249,144,0
55,1,0,140,217,111,0
59,1,0,140,249,144,0
62,0,0,160,164,145,0
58,1,0,140,211,165,0
51,1,0,140,298,122,0
64,1,0,145,212,132,0
57,1,0,152,274,88,0
54,1,0,140,239,160,0
47,1,0,110,275,118,0
"""

# Create DataFrame
data = pd.read_csv(StringIO(csv_data))

# Display dataset
print("===== HEART DISEASE DATASET =====")
print(data)

# Dataset information
print("\n===== DATASET SHAPE =====")
print(data.shape)

print("\n===== COLUMN NAMES =====")
print(list(data.columns))

# Check missing values
print("\n===== MISSING VALUES =====")
print(data.isnull().sum())

# Statistical information
print("\n===== STATISTICAL SUMMARY =====")
print(data.describe())

# Heart disease count
print("\n===== HEART DISEASE COUNT =====")
print(data["target"].value_counts())

# Average age
print("\nAverage Age:", round(data["age"].mean(), 2))

# Average cholesterol
print("Average Cholesterol:", round(data["chol"].mean(), 2))

# Maximum heart rate
print("Average Maximum Heart Rate:",
      round(data["thalach"].mean(), 2))

# Visualization 1
data["target"].value_counts().plot(kind="bar")

plt.title("Heart Disease Distribution")
plt.xlabel("Heart Disease (0 = No, 1 = Yes)")
plt.ylabel("Number of Patients")
plt.show()

# Visualization 2
data["age"].plot(kind="hist", bins=8)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show()

print("\n===== ANALYSIS COMPLETED =====")
