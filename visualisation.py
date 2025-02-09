import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('model.joblib')

# Title of the app
st.title("Amazon Delivery Time Prediction")

# User input fields
agent_age = st.number_input("Agent Age", min_value=18, max_value=65, value=30)
agent_rating = st.number_input("Agent Rating", min_value=1.0, max_value=5.0, value=4.2, step=0.1)
distance = st.number_input("Distance (km)", min_value=0.1, value=17.23)
weather = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy", "Stormy"])
area = st.selectbox("Area Type", ["Urban", "Suburban", "Rural"])
traffic = st.selectbox("Traffic Condition", ["Low", "Medium", "High", "Jam"])
vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car", "Van"])
category = st.selectbox("Delivery Category", ["Food", "Grocery", "Medicine", "Electronics"])

# Encoding categorical inputs
weather_mapping = {"Sunny": 0, "Cloudy": 1, "Rainy": 2, "Stormy": 3}
area_mapping = {"Urban": 0, "Suburban": 1, "Rural": 2}
traffic_mapping = {"Low": 0, "Medium": 1, "High": 2, "Jam": 3}
vehicle_mapping = {"Bike": 0, "Scooter": 1, "Car": 2, "Van": 3}
category_mapping = {"Food": 0, "Grocery": 1, "Medicine": 2, "Electronics": 3}

# Convert categorical inputs to numerical values
weather_encoded = weather_mapping[weather]
area_encoded = area_mapping[area]
traffic_encoded = traffic_mapping[traffic]
vehicle_encoded = vehicle_mapping[vehicle]
category_encoded = category_mapping[category]

# Predict delivery time
if st.button("Predict Delivery Time"):
    features = np.array([[agent_age, agent_rating, distance, weather_encoded, area_encoded, traffic_encoded, vehicle_encoded, category_encoded]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Delivery Time: {prediction:.2f} minutes")

