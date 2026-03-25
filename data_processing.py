import pandas as pd

# Load dataset
df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")

# Drop missing values
df = df.dropna()

# ❗ IMPORTANT: Drop 'name' column (too many categories)
df = df.drop(["name"], axis=1)

# Convert categorical to numeric
df = pd.get_dummies(df, drop_first=True)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("✅ Data Preprocessing Done")