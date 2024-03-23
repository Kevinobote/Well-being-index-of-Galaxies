# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
train_data = pd.read_csv('train.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(train_data.head())

# Information about the dataset, including missing values and data types
print("\nInformation about the dataset:")
print(train_data.info())

# Summary statistics of numerical features
print("\nSummary statistics of numerical features:")
print(train_data.describe())

# Visualize the distribution of the well-being index
plt.figure(figsize=(8, 6))
sns.histplot(train_data['Well_Being_Index'], kde=True)
plt.title('Distribution of Well-Being Index')
plt.xlabel('Well-Being Index')
plt.ylabel('Frequency')
plt.show()

# Visualize the distribution of other relevant variables
# Example: Age distribution
plt.figure(figsize=(8, 6))
sns.histplot(train_data['Age'], kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between well-being index and other variables
# Example: Scatter plot of Well-Being Index vs. Income
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Income', y='Well_Being_Index', data=train_data)
plt.title('Well-Being Index vs. Income')
plt.xlabel('Income')
plt.ylabel('Well-Being Index')
plt.show()

# Visualize correlations between features using a heatmap
correlation_matrix = train_data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Select features with high correlation to the well-being index
# Example: Select features with correlation coefficient > 0.5
selected_features = correlation_matrix['Well_Being_Index'][abs(correlation_matrix['Well_Being_Index']) > 0.5].index.tolist()
print("Selected features:", selected_features)
