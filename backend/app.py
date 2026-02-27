from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from preprocessing import prepare_features

app = FastAPI()

model = joblib.load("model.pkl")

class RiderInput(BaseModel):
    recency: int
    frequency: int
    monetary: float
    surge_exposure: float
    loyalty_status: str
    churn_prob: float
    rider_active_days: int
    rating_by_rider: float

@app.post("/predict")
def predict(data: RiderInput):
    df = pd.DataFrame([data.dict()])
    X = prepare_features(df)
    proba = model.predict_proba(X)[0, 1]
    return {
        "churn_probability": float(proba),
        "is_churning": bool(proba >= 0.5)
    }
