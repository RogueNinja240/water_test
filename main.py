from fastapi import FastAPI
import pickle
import pandas as pd
import os
from data_model import Water  # ✅ import from same folder

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(
    title="Water Potability Prediction",
    description="API to predict water potability",
    version="1.0.0"
)

# -----------------------------
# Absolute model path
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
model_path = os.path.join(BASE_DIR, "models", "model.pkl")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model file not found at {model_path}")

with open(model_path, "rb") as f:
    model = pickle.load(f)

# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def index():
    return {"message": "Welcome to Water Potability Prediction API 🚰"}

@app.post("/predict")
def model_predict(water: Water):
    # Convert input to DataFrame with proper column names
    sample = pd.DataFrame({
        "ph": [water.ph],
        "Hardness": [water.Hardness],
        "Solids": [water.Solids],
        "Chloramines": [water.Chloramines],
        "Sulfate": [water.Sulfate],
        "Conductivity": [water.Conductivity],
        "Organic_carbon": [water.Organic_carbon],
        "Trihalomethanes": [water.Trihalomethanes],
        "Turbidity": [water.Turbidity]
    })

    predicted_value = model.predict(sample)[0]

    return {
        "prediction": "Water is Consumable 💧" if predicted_value == 1 else "Water is NOT Consumable 🚫",
        "potability": int(predicted_value)
    }
