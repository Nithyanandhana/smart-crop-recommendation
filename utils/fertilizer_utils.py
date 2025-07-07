import pandas as pd

def recommend_fertilizer(predicted_crop, user_N, user_P, user_K):
    df = pd.read_csv("data/fertilizer.csv")
    crop_data = df[df["Crop"] == predicted_crop]

    if crop_data.empty:
        return None, "No fertilizer info available."

    rec_N = crop_data["N"].values[0]
    rec_P = crop_data["P"].values[0]
    rec_K = crop_data["K"].values[0]
    fert_name = crop_data["Fertilizer_Name"].values[0]
    desc = crop_data["Description"].values[0]

    return fert_name, desc
