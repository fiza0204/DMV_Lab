import pandas as pd
import numpy as np

df = pd.read_csv("synthetic_dataset.csv")

df = df.head(30)

df['Sales'] = np.random.randint(10, 500, size=30)
df['Profit'] = np.random.randint(5, 200, size=30)
df['Customer_Age'] = np.random.randint(18, 60, size=30)
df['Region'] = np.random.choice(['North', 'South', 'East', 'West'], size=30)
df['Order_Status'] = np.random.choice(['Delivered', 'Pending', 'Cancelled'], size=30)

df.to_csv("cleaned_dataset.csv", index=False)

print("Dataset is now 30 rows and 10 columns ready!")