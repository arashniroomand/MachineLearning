import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


"""
Preprocessing data of IRIS and looking for features and analyzing them
"""

# Load the iris dataset
IRIS = datasets.load_iris()

# Feature matrix and target
X = IRIS.data
Y = IRIS.target

# Convert to pandas DataFrame for better visualization
df = pd.DataFrame(X, columns=IRIS.feature_names)
df['target'] = Y
df['target_name'] = df['target'].apply(lambda i: IRIS.target_names[i])

# Show first 5 rows
print("🔍 Sample data:")
print(df.head())

# Dataset shape
print("\n📐 Shape of X:", X.shape)
print("🎯 Shape of Y:", Y.shape)

# Display feature and target names
print("\n📊 Features:", IRIS.feature_names)
print("🏷️ Target classes:", IRIS.target_names)

# Plot: Pairplot of features colored by class
sns.pairplot(df, hue='target_name', corner=True)
plt.suptitle("🔎 Pairplot of Iris Features", y=1.02)
plt.show()

# Histogram of each feature
df.drop(columns=['target', 'target_name']).hist(bins=20, figsize=(10, 6))
plt.suptitle("📈 Feature Distributions", y=1.02)
plt.show()

# Train/test split
trX, teX, trY, teY = train_test_split(X, Y, train_size=0.8, random_state=1)

# Scaling
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(trX)
trX_scaled = scaler.transform(trX)
teX_scaled = scaler.transform(teX)

print("\n✅ Data preprocessing complete.")
print("🔹 Scaled training sample (first row):")
print("Before:", trX[0])
print("After :", trX_scaled[0])
