from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from typing import List

# Charger le modèle et le préprocesseur enregistrés avec joblib
model = joblib.load('models/rental_price_model.joblib')  # Charger le modèle avec joblib
preprocessor = joblib.load('models/preprocessor.joblib')  # Charger le préprocesseur avec joblib

# Créer l'application FastAPI
app = FastAPI(title="GERAROUND API", description="Like the Airbnb for cars.")

# Définir un modèle Pydantic pour la validation des données d'entrée
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

# L'ordre des colonnes attendu par le préprocesseur
expected_columns = [
    "model_key", "mileage", "engine_power", "fuel", "paint_color", "car_type",
    "private_parking_available", "has_gps", "has_air_conditioning", "automatic_car",
    "has_getaround_connect", "has_speed_regulator", "winter_tires"
]

# Endpoint pour les prédictions
@app.post("/predict")
async def predict(data: List[RentalData]):
    # Convertir les données reçues en DataFrame en respectant l'ordre des colonnes attendu
    data_dict = [item.dict() for item in data]  # Convertir les données en dictionnaires
    input_data = pd.DataFrame(data_dict, columns=expected_columns)  # Créer le DataFrame avec l'ordre des colonnes

    # Appliquer le préprocesseur sur les données d'entrée
    processed_data = preprocessor.transform(input_data)

    # Faire la prédiction avec le modèle
    prediction = model.predict(processed_data)

    # Retourner la prédiction sous forme de JSON
    return {"prediction": prediction.tolist()}
