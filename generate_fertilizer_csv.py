import pandas as pd

data = {
    "Crop": ["rice", "maize", "chickpea", "kidneybeans", "pigeonpeas", "mothbeans", "mungbean", "blackgram", "lentil", "pomegranate", "banana", "mango", "grapes", "watermelon", "muskmelon", "apple", "orange", "papaya", "coconut", "cotton", "jute", "coffee"],
    "N": [90, 80, 70, 70, 70, 60, 60, 60, 60, 80, 100, 100, 80, 90, 60, 80, 90, 100, 80, 100, 60, 80],
    "P": [40, 35, 25, 30, 25, 20, 25, 25, 25, 40, 30, 40, 40, 60, 40, 40, 50, 40, 50, 50, 40, 30],
    "K": [40, 40, 25, 30, 30, 20, 25, 25, 25, 40, 200, 50, 60, 60, 40, 80, 50, 100, 300, 50, 40, 80],
    "Fertilizer_Name": [
        "Urea", "Compost + NPK", "RDF-based NPK (12-32-16)", "DAP (Diammonium Phosphate)", "Organic Manure",
        "Compost + Urea", "RDF-based NPK", "DAP + Vermicompost", "Organic Manure", "NPK 8-8-8", "Muriate of Potash",
        "Compost + NPK Slow Release", "NPK 19-19-19", "DAP + Potash + Compost", "Compost + DAP", "NPK 17-17-17",
        "Citrus-specific NPK", "NPK 20-10-20", "Muriate of Potash + Organic", "Super Phosphate + Urea + Potash",
        "NPK 12-32-16", "NPK 19-19-19 + Organic"
    ],
    "Description": [
        "Urea (46% N) for nitrogen replenishment", "Organic compost + balanced NPK blend",
        "Recommended dose for pulses", "High phosphorus requirement", "Farmyard manure for slow nutrient release",
        "Compost base with supplemental urea", "Balanced for legumes", "Phosphorus boost + organic matter",
        "Neutral NPK suit for pulses", "Nutrient balance for fruiting crops", "Potassium-focused for fruit quality",
        "Nutrient-supportive mix", "Balanced blend", "Heavy feeder needs all three", "Organic with moderate phosphorus",
        "Mature fruit tree maintenance", "Fertilizer for citrus nutrition", "Fruit yield support", "Palm high K requirement",
        "High N-P-K blend", "Leafy fiber crop fertilizer", "Blend suitable for shade trees"
    ]
}

df = pd.DataFrame(data)
df.to_csv("fertilizer.csv", index=False)
print("✅ fertilizer.csv file created successfully!")
