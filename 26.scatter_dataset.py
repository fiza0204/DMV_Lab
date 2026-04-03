# scatter_dataset.py

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("cleaned_dataset.csv")

# Convert columns to numeric (IMPORTANT)
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')

# Remove rows with missing values
data = data.dropna(subset=['Price', 'Sales'])

# Check data
print("Valid rows:", len(data))

# Create scatter plot
plt.scatter(data['Price'], data['Sales'])

plt.xlabel('Price')
plt.ylabel('Sales')
plt.title('Scatter Plot of Price vs Sales')

plt.show()