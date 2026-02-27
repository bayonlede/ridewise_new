import pandas as pd

def prepare_features(df):
    df["monthly_trips"] = (df["frequency"] / df["rider_active_days"]) * 30

    loyalty_map = {"Bronze": 0, "Silver": 1, "Gold": 2, "Platinum": 3}
    df["loyalty_status_encoded"] = df["loyalty_status"].map(loyalty_map)

    features = [
        "recency", "frequency", "monetary", "surge_exposure",
        "rider_active_days", "rating_by_rider", "monthly_trips",
        "loyalty_status_encoded"
    ]

    return df[features]
