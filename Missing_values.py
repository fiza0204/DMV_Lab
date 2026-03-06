import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Sara", "John", "Atif"
    ""],
    "Age": [20, np.nan, 22, np.nan],
    "Marks": [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull())

# Fill missing values with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nData after handling missing values:")
print(df)



