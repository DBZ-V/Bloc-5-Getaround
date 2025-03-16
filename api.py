# from fastapi import FastAPI
# import joblib
# import numpy as np
# from pydantic import BaseModel
# from typing import List

# # Charger le modèle et le préprocesseur enregistrés avec joblib
# model = joblib.load('models/rental_price_model.joblib')  # Charger le modèle avec joblib
# preprocessor = joblib.load('models/preprocessor.joblib')  # Charger le préprocesseur avec joblib

# # Créer l'application FastAPI
# app = FastAPI(title="GERAROUND API", description="Like the Airbnb for cars.")

# # Définir un modèle Pydantic pour la validation des données d'entrée
# class RentalData(BaseModel):
#     model_key: str
#     mileage: int
#     engine_power: int
#     fuel: str
#     paint_color: str
#     car_type: str
#     private_parking_available: bool
#     has_gps: bool
#     has_air_conditioning: bool
#     automatic_car: bool
#     has_getaround_connect: bool
#     has_speed_regulator: bool
#     winter_tires: bool

# # Endpoint pour les prédictions
# @app.post("/predict")
# async def predict(data: List[RentalData]):
#     # Extraire les valeurs des données reçues
#     input_data = []
#     for item in data:
#         input_data.append([
#             item.mileage,
#             item.engine_power,
#             item.fuel,
#             item.paint_color,
#             item.car_type,
#             item.private_parking_available,
#             item.has_gps,
#             item.has_air_conditioning,
#             item.automatic_car,
#             item.has_getaround_connect,
#             item.has_speed_regulator,
#             item.winter_tires
#         ])
    
#     # Appliquer le préprocesseur sur les variables catégorielles
#     processed_data = preprocessor.transform(input_data)
    
#     # Faire la prédiction avec le modèle joblib
#     prediction = model.predict(processed_data)
    
#     # Retourner la prédiction sous forme de JSON
#     return {"prediction": prediction.tolist()}
# -----------------------------------------------
# from fastapi import FastAPI
# import joblib
# import pandas as pd
# from pydantic import BaseModel
# from typing import List
# import os

# # Créer l'application FastAPI D'ABORD !
# app = FastAPI(title="GERAROUND API", description="Like the Airbnb for cars.")

# # Charger les modèles après
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MODEL_PATH = os.path.join(BASE_DIR, 'models', 'rental_price_model.joblib')
# PREPROCESSOR_PATH = os.path.join(BASE_DIR, 'models', 'preprocessor.joblib')

# model = joblib.load(MODEL_PATH)
# preprocessor = joblib.load(PREPROCESSOR_PATH)

# # Définir un modèle Pydantic clair
# class RentalData(BaseModel):
#     model_key: str
#     mileage: int
#     engine_power: int
#     fuel: str
#     paint_color: str
#     car_type: str
#     private_parking_available: bool
#     has_gps: bool
#     has_air_conditioning: bool
#     automatic_car: bool
#     has_getaround_connect: bool
#     has_speed_regulator: bool
#     winter_tires: bool

# class RentalDataList(BaseModel):
#     data: List[RentalData]

# expected_columns = [
#     "model_key", "mileage", "engine_power", "fuel", "paint_color", "car_type",
#     "private_parking_available", "has_gps", "has_air_conditioning", "automatic_car",
#     "has_getaround_connect", "has_speed_regulator", "winter_tires"
# ]

# # Endpoint racine pour tester facilement
# @app.get("/")
# async def root():
#     return {"message": "Bienvenue sur GERAROUND API. Visitez /docs pour la documentation."}

# # Endpoint clair et robuste
# @app.post("/predict")
# async def predict(rental_data_list: RentalDataList):
#     # Conversion propre en DataFrame
#     input_data = pd.DataFrame(
#         [item.dict() for item in rental_data_list.data],
#         columns=expected_columns
#     )

#     # Pré-traitement et prédiction
#     processed_data = preprocessor.transform(input_data)
#     prediction = model.predict(processed_data)

#     return {"prediction": prediction.tolist()}

# -------------------------
from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from typing import List
import requests
import tempfile

# Créer l'application FastAPI D'ABORD !
app = FastAPI(title="GERAROUND API", description="Like the Airbnb for cars.")

# URLs publiques des modèles hébergés sur S3
MODEL_URL = "https://mon-seau-825.s3.eu-west-3.amazonaws.com/models_getaround/rental_price_model.joblib"
PREPROCESSOR_URL = "https://mon-seau-825.s3.eu-west-3.amazonaws.com/models_getaround/preprocessor.joblib"

# Fonction pour charger un modèle depuis une URL publique
def load_joblib_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(suffix=".joblib") as tmp_file:
        tmp_file.write(response.content)
        tmp_file.flush()
        return joblib.load(tmp_file.name)

model = load_joblib_from_url(MODEL_URL)
preprocessor = load_joblib_from_url(PREPROCESSOR_URL)

# Modèles Pydantic
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

@app.get("/")
async def root():
    return {"message": "Bienvenue sur GERAROUND API."}

@app.post("/predict")
async def predict(rental_data_list: RentalDataList):
    input_data = pd.DataFrame(
        [item.dict() for item in rental_data_list.data],
        columns=expected_columns
    )
    processed_data = preprocessor.transform(input_data)
    prediction = model.predict(processed_data)
    return {"prediction": prediction.tolist()}

