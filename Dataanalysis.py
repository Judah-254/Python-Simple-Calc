# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set Seaborn style
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("Dataset loaded successfully.\n")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Show first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
print("\nStatistical Summary:")
print(df.describe())

# Grouping by species and calculating mean
print("\nMean values grouped by species:")
print(df.groupby("species").mean())

# Task 3: Data Visualization

# 1. Line Chart – Average petal length per species
df_grouped = df.groupby("species").mean().reset_index()

plt.figure(figsize=(8, 5))
plt.plot(df_grouped["species"], df_grouped["petal length (cm)"], marker='o')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart – Average sepal width per species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="sepal width (cm)", data=df_grouped)
plt.title("Average Sepal Width per Species")
plt.xlabel("Species")
plt.ylabel("Sepal Width (cm)")
plt.tight_layout()
plt.show()

# 3. Histogram – Distribution of petal length
plt.figure(figsize=(8, 5))
plt.hist(df["petal length (cm)"], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot – Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()

# Findings
print("\n📌 Observations:")
print("- Setosa generally has smaller petal length and width compared to Versicolor and Virginica.")
print("- Virginica tends to have the largest sepal and petal dimensions.")
print("- Petal length is a strong differentiator between the three species.")
