# This program prints Hello, world!

print('Hello, world!')

import numpy as np
import pandas as pd

# Generate random data
# Let's assume we are generating data for two columns: 'A' and 'B'
np.random.seed(0)  # For reproducibility
data_size = 1000

column_A = np.random.normal(loc=0, scale=1, size=data_size)  # Normally distributed data
column_B = np.random.uniform(low=-3, high=3, size=data_size)  # Uniformly distributed data

# Create a DataFrame
df = pd.DataFrame({'A': column_A, 'B': column_B})

# Explore the dataset
print("First 5 rows of the dataset:")
print(df.head())

print("\nSummary statistics of the dataset:")
print(df.describe())

# Simple analysis - Calculate mean and median of both columns
mean_A = df['A'].mean()
median_A = df['A'].median()
mean_B = df['B'].mean()
median_B = df['B'].median()

print(f"\nMean of column A: {mean_A}")
print(f"Median of column A: {median_A}")
print(f"Mean of column B: {mean_B}")
print(f"Median of column B: {median_B}")
