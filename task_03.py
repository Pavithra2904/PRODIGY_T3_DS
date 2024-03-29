# -*- coding: utf-8 -*-
"""task_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gKEBuqM8L9LkZT__FMaGmqJgC_qv_4ke
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load the dataset
retail_df = pd.read_csv('/content/task_03_ds.csv')

# Display the first few rows of the dataset
print(retail_df.head())

# Create the target variable based on Total Amount
#retail_df['Purchase'] = retail_df['Total Amount'] > 0

# Prepare the features and target variable
X = retail_df[['job', 'age', 'marital', 'loan', 'education', 'poutcome']]
y = retail_df['deposit']

# Convert categorical variables to dummy/indicator variables
X = pd.get_dummies(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Decision Tree Classifier
max_depth = 5
dt_classifier = DecisionTreeClassifier(max_depth=max_depth, random_state=42)

# Train the classifier
dt_classifier.fit(X_train, y_train)
# Plot decision tree
plt.figure(figsize=(20,10))
plot_tree(dt_classifier, filled=True, feature_names=X.columns, class_names=['No Deposit', 'Deposit'])
plt.show()

# Predict the response for test dataset
y_pred = dt_classifier.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(conf_matrix)