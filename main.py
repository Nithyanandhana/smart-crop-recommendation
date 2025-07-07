import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from utils.weather_utils import get_weather
from utils.fertilizer_utils import recommend_fertilizer
import pickle
import pandas as pd

# Load model + label encoder
with open("model/crop_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("model/label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

city = input("Enter your city name: ")
temperature, humidity, rainfall = get_weather(city)

if temperature is not None:
    print(f"\n📍 Weather in {city.title()}:")
    print(f"🌡️ Temperature: {temperature:.2f} °C")
    print(f"💧 Humidity: {humidity} %")
    print(f"🌧️ Rainfall (last 1hr): {rainfall} mm")

    # Take soil inputs
    N = int(input("Enter Nitrogen (N) value: "))
    P = int(input("Enter Phosphorus (P) value: "))
    K = int(input("Enter Potassium (K) value: "))
    pH = float(input("Enter soil pH value: "))

    sample_input = [[N, P, K, temperature, humidity, pH, rainfall]]
    prediction = model.predict(sample_input)
    predicted_crop = le.inverse_transform(prediction)[0]

    print(f"\n🌱 Based on your inputs, the recommended crop is: {predicted_crop}")

    # Recommend fertilizer
    fertilizer, reason = recommend_fertilizer(predicted_crop, N, P, K)
    if fertilizer:
        print(f"🧪 Recommended Fertilizer: {fertilizer}")
        print(f"📌 Why: {reason}")
    else:
        print("❌ Fertilizer recommendation not found for this crop.")
else:
    print("⚠️ Weather data not available. Please try again.")
