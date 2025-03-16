# 🚗 Getaround Car Rental Pricing Optimization

## Ce projet prédit le prix de location quotidien des voitures en fonction de plusieurs facteurs (modèle, kilométrage, puissance moteur, type de carburant, etc.).

L’objectif est d’optimiser les prix de location pour les propriétaires de voitures grâce à un modèle de Machine Learning exposé via une API FastAPI et un tableau de bord Streamlit.
## 📌 Fonctionnalités :

✔ Modèle de Machine Learning : Prédiction du prix de location quotidien en fonction des caractéristiques du véhicule.
✔ API FastAPI : Permet aux utilisateurs de soumettre les détails d'une voiture et d'obtenir une estimation du prix de location.
✔ Tableau de bord Streamlit : Interface ergonomique pour soumettre les détails d'un véhicule et afficher les prédictions.
✔ Déploiement : Hébergé sur Hugging Face Spaces pour un accès en ligne simple et rapide.
[![Hugging Face Space](https://img.shields.io/badge/Hugging%20Face-API%20Online-blue?logo=huggingface)](https://dbzv-fastapigetaround.hf.space)
## 📂 Structure du Projet :
```
├── 1-streamlit.py            # Dashboard Streamlit d'analyse des seuils
├── 2-Training.ipynb          # Notebook d'entraînement des modèles
├── 3-streamlit_predi.py      # Dashboard Streamlit de prédiction des prix de location
├── Z-EDA.ipynb               # Exploration et analyse des données
├── dockerfile                # Dockerfile pour le déploiement
├── app.py                    # API FastAPI exposant l'endpoint /predict
├── models/
│   │
│   └── preprocessor.joblib   # Préprocesseur des données
│
├── requirements.txt          # Dépendances Python
└── README.md                 # Ce fichier
```

## 🛠 Installation et Exécution en Local
📌 Prérequis

    ✅ Python 3.9+
    ✅ Docker installé
    ✅ pip pour gérer les dépendances

📌 Installation des dépendances

Cloner le dépôt et installer les dépendances :
```
git clone https://github.com/DBZ-V/Bloc-5-Getaround.git
cd Bloc-5-Getaround
pip install -r requirements.txt
```
## 🚀 Exécuter l'API FastAPI en Local
📌 Avec Docker
```
  docker build -t getaround-api .
  docker run -p 7860:7860 getaround-api
```
  
## ✅ Une fois l'API lancée, accédez à Swagger (documentation automatique) : 
👉 http://localhost:7860/docs
```
[
  {
    "model_key": "string",
    "mileage": 0,
    "engine_power": 0,
    "fuel": "string",
    "paint_color": "string",
    "car_type": "string",
    "private_parking_available": true,
    "has_gps": true,
    "has_air_conditioning": true,
    "automatic_car": true,
    "has_getaround_connect": true,
    "has_speed_regulator": true,
    "winter_tires": true
  }
] ```
```
## 📊 Lancer le Dashboard Streamlit en local
### 📌 Pour visualiser les analyses :
```
streamlit run 1-streamlit.py
```
👉 Accès au tableau de bord des analyses et figures

### 📌 Pour tester les prédictions :
```
streamlit run 3-streamlit_predi.py
```
👉 Accès au dashboard ergonomique de prédiction de prix de location

## 📡 Formatage des Appels API
### 📌 Test API en local avec Python
```
import requests

# Exemple générique de données à envoyer à l'API
data = {
    "data": [
        {
            "model_key": "string",
            "mileage": int,
            "engine_power": int,
            "fuel": "string",
            "paint_color": "string",
            "car_type": "string",
            "private_parking_available": True,
            "has_gps": False,
            "has_air_conditioning": True,
            "automatic_car": False,
            "has_getaround_connect": True,
            "has_speed_regulator": False,
            "winter_tires": False
        }
    ]
}

# Envoi de la requête à l'API
response = requests.post("http://localhost:7860/predict", json=data)

# Affichage de la réponse JSON
print(response.status_code)
print(response.json())

```
exemple
```
import requests

data = {
    "data": [ 
        {
            "model_key": "Citroen",
            "mileage": 20000,
            "engine_power": 120,
            "fuel": "diesel",
            "paint_color": "black",
            "car_type": "sedan",
            "private_parking_available": True,
            "has_gps": True,
            "has_air_conditioning": False,
            "automatic_car": False,
            "has_getaround_connect": True,
            "has_speed_regulator": True,
            "winter_tires": False
        }
    ]
}

# Maintenant, envoie la requête corrigée
response = requests.post("http://localhost:7860/predict", json=data)

# Affiche clairement la réponse
print(response.status_code)
print(response.json())


```
## 📡 Tester l'API avec curl (Terminal)
### 📌 Requête générique :
```
curl -X POST "http://127.0.0.1:7860/predict" -H "Content-Type: application/json" -d "{\"data\":[{\"model_key\":\"string\",\"mileage\":int,\"engine_power\":int,\"fuel\":\"string\",\"paint_color\":\"string\",\"car_type\":\"string\",\"private_parking_available\":true,\"has_gps\":false,\"has_air_conditioning\":true,\"automatic_car\":false,\"has_getaround_connect\":true,\"has_speed_regulator\":false,\"winter_tires\":false}]}"


```
### 📌 Exemple avec des valeurs réelles :
```
curl -X POST "http://127.0.0.1:7860/predict" -H "Content-Type: application/json" -d "{\"data\":[{\"model_key\":\"BMW\",\"mileage\":20000,\"engine_power\":120,\"fuel\":\"diesel\",\"paint_color\":\"black\",\"car_type\":\"sedan\",\"private_parking_available\":true,\"has_gps\":true,\"has_air_conditioning\":true,\"automatic_car\":false,\"has_getaround_connect\":true,\"has_speed_regulator\":true,\"winter_tires\":false}]}"
```
# 🌍 API en ligne sur Hugging Face 🤗
## L’API est déployée sur Hugging Face Spaces pour être accessible partout.
📌  Lien du Hugging Face Space
Le repository de HuggingFace contient les deux joblib, le model étant trop lourd pour git hub
    ### Liens du Hugging Face
    📍 https://huggingface.co/spaces/Dbzv/FastApiGetaround
    ### Lien API à utilisé
    📍 https://dbzv-fastapigetaround.hf.space
    ### Lien pour Swagger
    📍 https://dbzv-fastapigetaround.hf.space/docs#/

### 📌 Appel API en ligne avec Python
```
import requests

url = "https://dbzv-fastapigetaround.hf.space/predict"
data = {
    "data": [
        {
            "model_key": "string",
            "mileage": 12345,
            "engine_power": 100,
            "fuel": "string",
            "paint_color": "string",
            "car_type": "string",
            "private_parking_available": True,
            "has_gps": False,
            "has_air_conditioning": True,
            "automatic_car": False,
            "has_getaround_connect": True,
            "has_speed_regulator": False,
            "winter_tires": False
        }
    ]
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```
