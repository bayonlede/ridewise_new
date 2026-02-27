import streamlit as st
import requests

API_URL = "https://your-backend-url.onrender.com/predict"

st.title("RideWise – Churn Prediction")

inputs = {
    "recency": st.number_input("Recency", 0),
    "frequency": st.number_input("Frequency", 0),
    "monetary": st.number_input("Monetary", 0.0),
    "surge_exposure": st.number_input("Surge Exposure", 0.0, 1.0),
    "loyalty_status": st.selectbox("Loyalty Status", ["Bronze", "Silver", "Gold", "Platinum"]),
    "churn_prob": st.number_input("Churn Probability", 0.0, 1.0),
    "rider_active_days": st.number_input("Active Days", -1000),
    "rating_by_rider": st.number_input("Rating by Rider", 1.0, 5.0)
}

if st.button("Predict"):
    response = requests.post(API_URL, json=inputs)
    result = response.json()
    st.metric("Churn Probability", f"{result['churn_probability']:.2%}")
    st.write("Churn Status:", "Churning" if result["is_churning"] else "Not Churning")
