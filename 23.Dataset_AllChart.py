import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")


# 1. BAR CHART
df['Category'].value_counts().plot(kind='bar')
plt.title("Bar Chart - Category Count")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()


# 2. LINE CHART
df['Price'].plot(kind='line')
plt.title("Line Chart - Price Trend")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()


# 3. PIE CHART
df['Stock'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Pie Chart - Stock Distribution")
plt.show()


# 4. STAIR CHART
plt.step(range(len(df)), df['Price'])
plt.title("Stair Chart - Price")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()


# 5. HISTOGRAM
df['Price'].plot(kind='hist')
plt.title("Histogram - Price Distribution")
plt.xlabel("Price")
plt.show()