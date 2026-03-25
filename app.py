import streamlit as st
import pandas as pd
import joblib

# Load model & columns
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title("🚗 Car Price Prediction")

# Inputs
year = st.number_input("Year", 2000, 2025)
km_driven = st.number_input("KM Driven", 0, 500000)
fuel = st.selectbox("Fuel", ["Petrol", "Diesel", "CNG", "LPG"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
seller_type = st.selectbox("Seller Type", ["Individual", "Dealer"])
owner = st.selectbox("Owner", ["First Owner", "Second Owner", "Third Owner"])

# Create empty dataframe with all columns
input_df = pd.DataFrame(columns=columns)
input_df.loc[0] = 0

# Fill basic values
input_df["year"] = year
input_df["km_driven"] = km_driven

# Encoding categorical inputs
if f"fuel_{fuel}" in input_df.columns:
    input_df[f"fuel_{fuel}"] = 1

if f"transmission_{transmission}" in input_df.columns:
    input_df[f"transmission_{transmission}"] = 1

if f"seller_type_{seller_type}" in input_df.columns:
    input_df[f"seller_type_{seller_type}"] = 1

if f"owner_{owner}" in input_df.columns:
    input_df[f"owner_{owner}"] = 1

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {int(prediction[0])}")