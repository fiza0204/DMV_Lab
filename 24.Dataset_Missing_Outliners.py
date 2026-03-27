import pandas as pd

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")


# ----------- MISSING VALUES COUNT -----------

print("Missing Values Count:\n")
missing_count = df.isnull().sum()
print(missing_count)


# ----------- OUTLIERS COUNT -----------

print("\nOutliers Count:\n")

num_cols = df.select_dtypes(include=['int64', 'float64'])

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"{col}: {len(outliers)} outliers")