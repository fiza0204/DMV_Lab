import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("cleaned_dataset.csv")

# Convert Price to numeric (VERY IMPORTANT)
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Remove missing values
data = data.dropna(subset=['Price'])

# Check if data exists
print(data['Price'].head())
print("Total valid values:", len(data))

# Plot
plt.boxplot(data['Price'])

plt.xlabel('Price')
plt.title('Box Plot of Prices')

plt.show()
