import requests
import pandas as pd
def get_weather(city, api_key="9a4b062be3ccd30f0abbd5b7947026dd"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("main"):
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            rainfall = data.get("rain", {}).get("1h", 0.0)
            if rainfall == 0:
                print("⚠️ No rainfall data available. Using default value of 50 mm.")
                df = pd.read_csv("data/Crop_recommendation.csv")  # Update path if needed
                avg_rainfall = df['rainfall'].mean()
                rainfall =  avg_rainfall
            return temperature, humidity, rainfall
        else:
            print("⚠️ Weather fetch failed:", data.get("message", "Unknown error"))
            return None, None, None
    except Exception as e:
        print("⚠️ Weather fetch error:", e)
        return None, None, None
