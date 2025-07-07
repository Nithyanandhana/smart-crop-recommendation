# smart-crop-recommendation
 AI-powered Crop &amp; Fertilizer Recommendation using Weather Data
 
An intelligent crop recommendation system using Machine Learning and real-time weather integration. This application helps farmers select the most suitable crop for cultivation based on soil nutrients and current weather conditions.

---

## 🚀 Features

- 🔍 Predicts the most suitable crop using real-time weather (via OpenWeatherMap API)
- 🧪 Recommends fertilizers based on crop-specific NPK requirements
- 🌦 Live input for temperature, humidity, and rainfall using city name
- 📊 Visualizations for crop distribution and nutrient requirements
- 🧠 Trained ML model with 99% accuracy (RandomForestClassifier)
- 💡 Simple, interactive UI using Streamlit
- 💾 Local CSV-based fertilizer database

---

## 🧠 Tech Stack

- **Language:** Python
- **ML Libraries:** Scikit-learn, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Web UI:** Streamlit
- **API:** OpenWeatherMap API for live weather data
- **Model:** RandomForestClassifier (trained on 2200+ labeled samples)

---

## 📂 Dataset Info

Features used:

- **N** - Nitrogen
- **P** - Phosphorus
- **K** - Potassium
- **Temperature** (°C)
- **Humidity** (%)
- **pH** - Soil pH
- **Rainfall** (mm)
- **Label** - Crop Name (e.g., rice, maize, apple, mango, etc.)

---

## ⚙️ How to Run Locally

1. **Clone the repository**
 
git clone https://github.com/Nithyanandhana/smart-crop-recommendation.git

cd smart-crop-recommendation

Install dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

---

## 🙌 Acknowledgments

- Dataset from [Kaggle or source]
- Weather API by [OpenWeatherMap](https://openweathermap.org/)
