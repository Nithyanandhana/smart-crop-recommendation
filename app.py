import streamlit as st
import pickle
import numpy as np
from utils.weather_utils import get_weather
from utils.fertilizer_utils import recommend_fertilizer

# Load model and label encoder
with open("model/crop_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

st.set_page_config(page_title="Smart Crop Recommendation", layout="centered")

st.markdown(
    """
    <style>
        /* Set black background */
        .stApp {
            background-color: #000000;
            color: #ffffff;
        }

        /* Style for the heading */
        h1 {
            font-size: 40px !important;
            color: #00FF99;  /* Neon green */
            text-align: center;
            margin-top: 0;
        }

        /* Button styling */
        .stButton > button {
            background-color: #39FF14;
            color: #000000;
            border: none;
            padding: 5px 10px;
            font-size: 12px;
            font-weight: bold;
            border-radius: 4px;
        }

        /* Reduce top empty space */
        .block-container {
            padding-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>🌾 Smart Crop Recommendation System</h1>", unsafe_allow_html=True)




st.markdown("Get crop & fertilizer recommendations using soil nutrients and real-time weather.")

city = st.text_input("📍 Enter your city name")
N = st.number_input("🌱 Nitrogen (N)", min_value=0, max_value=200, step=1)
P = st.number_input("🌿 Phosphorus (P)", min_value=0, max_value=200, step=1)
K = st.number_input("🌾 Potassium (K)", min_value=0, max_value=200, step=1)
pH = st.number_input("🧪 pH Value", min_value=0.0, max_value=14.0, step=0.1)

if st.button("🔍 Predict Crop"):
    if city:
        temperature, humidity, rainfall = get_weather(city)
        
        if temperature is not None:
            st.markdown(f"### 📊 Weather in {city.title()}")
            st.write(f"🌡️ Temperature: {temperature:.2f} °C")
            st.write(f"💧 Humidity: {humidity:.2f} %")
            st.write(f"🌧️ Rainfall: {rainfall:.2f} mm")

            sample_input = np.array([[N, P, K, temperature, humidity, pH, rainfall]])
            prediction = model.predict(sample_input)
            predicted_crop = le.inverse_transform(prediction)[0]

            st.success(f"🌱 Recommended Crop: **{predicted_crop.capitalize()}**")

            fertilizer, reason = recommend_fertilizer(predicted_crop, N, P, K)
            st.info(f"🧪 Recommended Fertilizer: **{fertilizer}**")
            st.markdown(f"📌 _Why_: {reason}")
        else:
            st.warning("⚠️ Weather data not available. Try again.")
    else:
        st.warning("Please enter a city name.")
