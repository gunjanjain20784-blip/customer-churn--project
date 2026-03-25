import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
df = pd.read_csv("cleaned_data.csv")

# Features & Target
X = df.drop("selling_price", axis=1)
y = df["selling_price"]

# Save columns (important for frontend)
joblib.dump(X.columns, "columns.pkl")

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model & columns saved successfully")