# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
train_data = pd.read_csv('train.csv')

# Feature Selection
print("Feature Selection:")

# Correlation Analysis
# Calculate the correlation matrix
correlation_matrix = train_data.corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Select features highly correlated with the well-being index
# Filter features based on a threshold (e.g., correlation coefficient > 0.5)
selected_features = correlation_matrix['Well-Being Index'][abs(correlation_matrix['Well-Being Index']) > 0.5].index.tolist()

# Print selected features
print("Selected features based on correlation analysis:")
print(selected_features)

# Feature Importance
# Example: If using a tree-based model (e.g., Random Forest), calculate feature importance
# Import the necessary libraries for Random Forest
from sklearn.ensemble import RandomForestRegressor

# Separate features and target variable
X = train_data.drop(['Well-Being Index'], axis=1)
y = train_data['Well-Being Index']

# Initialize Random Forest model
rf_model = RandomForestRegressor()

# Fit the model to the data
rf_model.fit(X, y)

# Get feature importances
feature_importances = rf_model.feature_importances_

# Create a DataFrame to store feature importances
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})

# Sort features based on importance in descending order
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Visualize feature importances
plt.figure(figsize=(10, 8))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df[:10])  # Top 10 features
plt.title('Top 10 Feature Importances')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()

# Select top features based on importance
top_features = feature_importance_df['Feature'][:5].tolist()

# Print selected top features
print("\nTop features based on feature importance:")
print(top_features)
