import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\MANEESHA\skillcraft.py\data.csv")

# -------------------------------
# Basic Info
# -------------------------------
print("First 5 rows:\n", df.head())
print("\nDataset Info:\n")
print(df.info())

# -------------------------------
# Data Cleaning
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# EDA
# -------------------------------

# 1. Purchased count
df['Purchased'].value_counts().plot(kind='bar')
plt.title("Purchased (0 = No, 1 = Yes)")
plt.xlabel("Purchased")
plt.ylabel("Count")
plt.show()

# 2. Age Distribution
plt.hist(df['Age'], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 3. Salary Distribution
plt.hist(df['Salary'], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# 4. Age vs Salary
plt.scatter(df['Age'], df['Salary'])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# Observations
# -------------------------------
print("\nObservations:")
print("1. Younger people tend not to purchase.")
print("2. Higher salary people are more likely to purchase.")