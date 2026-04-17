import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("company_dataset.csv")

# -------- Data Cleaning --------
df['years'] = df['years'].str.extract(r'(\d+)').astype(float)
df['ratings'] = df['ratings'].astype(float)
df['employees'] = df['employees'].str.extract(r'(\d+)')

# Clean review_count (convert "59.9k" → 59900)
df['review_count'] = df['review_count'].str.replace('[(), Reviews]', '', regex=True)
df['review_count'] = df['review_count'].str.replace('k', '000')
df['review_count'] = df['review_count'].astype(float)

# -------- 1. Pie Chart --------
emp_counts = df['employees'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(emp_counts, labels=emp_counts.index, autopct='%1.1f%%')
plt.title("Employee Distribution")
plt.show()

# -------- 2. Ratings Distribution --------
rating_counts = df['ratings'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(rating_counts.index, rating_counts.values)
plt.title("Ratings Distribution")
plt.show()

# -------- 3. Bar Chart --------
plt.figure(figsize=(10,5))
plt.bar(df['name'][:10], df['years'][:10])
plt.xticks(rotation=90)
plt.title("Company vs Years")
plt.show()

# -------- 4. Line Chart --------
ctype_count = df['ctype'].value_counts()

plt.figure(figsize=(8,5))
plt.plot(ctype_count.index, ctype_count.values, marker='o')
plt.xticks(rotation=45)
plt.title("Company Type Distribution")
plt.show()

# -------- 5. Histogram (Review Count) --------
plt.figure(figsize=(8,5))
plt.hist(df['review_count'], bins=10, edgecolor='black')
plt.title("Histogram of Review Counts")
plt.xlabel("Review Count")
plt.ylabel("Number of Companies")
plt.show()