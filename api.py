from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from typing import List
import os

# Créer l'application FastAPI D'ABORD !
app = FastAPI(title="GERAROUND API", description="Like the Airbnb for cars.")

# Charger les modèles après
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'rental_price_model.joblib')
PREPROCESSOR_PATH = os.path.join(BASE_DIR, 'models', 'preprocessor.joblib')

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

# Définir un modèle Pydantic clair
class RentalData(BaseModel):
    model_key: str
    mileage: int
    engine_power: int
    fuel: str
    paint_color: str
    car_type: str
    private_parking_available: bool
    has_gps: bool
    has_air_conditioning: bool
    automatic_car: bool
    has_getaround_connect: bool
    has_speed_regulator: bool
    winter_tires: bool

class RentalDataList(BaseModel):
    data: List[RentalData]

expected_columns = [
    "model_key", "mileage", "engine_power", "fuel", "paint_color", "car_type",
    "private_parking_available", "has_gps", "has_air_conditioning", "automatic_car",
    "has_getaround_connect", "has_speed_regulator", "winter_tires"
]

# Endpoint racine pour tester facilement
@app.get("/")
async def root():
    return {"message": "Bienvenue sur GERAROUND API."}

# Endpoint clair et robuste
@app.post("/predict")
async def predict(rental_data_list: RentalDataList):
    # Conversion propre en DataFrame
    input_data = pd.DataFrame(
        [item.dict() for item in rental_data_list.data],
        columns=expected_columns
    )

    # Pré-traitement et prédiction
    processed_data = preprocessor.transform(input_data)
    prediction = model.predict(processed_data)

    return {"prediction": prediction.tolist()}
