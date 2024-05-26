import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n = 100

# Generate random numerical data with feature names
num_data = {
    'feature1': np.random.randint(18, 65, n),
    'feature2': np.random.randint(20000, 100000, n),
    'feature3': np.random.uniform(1, 100, n)
}

# Generate random categorical data with feature names
cat_data = {
    'feature4': [random.choice(['low', 'medium', 'high']) for _ in range(n)],
    'feature5': [random.choice(['male', 'female']) for _ in range(n)],
    'feature6': [random.choice(['high school', 'bachelor', 'master', 'phd']) for _ in range(n)]
}

# Combine numerical and categorical data
data = {**num_data, **cat_data}

# Create DataFrame
df = pd.DataFrame(data)

# Display first few rows of the DataFrame
print(df.head())

# Save DataFrame to CSV file
df.to_csv('synthetic_data.csv', index=False)
