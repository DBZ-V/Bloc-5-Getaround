# Getaround Car Rental Pricing Optimization

Ce projet est axé sur la prédiction du prix de location quotidien des voitures en fonction de plusieurs facteurs tels que le modèle, le kilométrage, la puissance du moteur, le type de carburant, et bien d'autres. L'objectif est d'optimiser les prix de location pour les propriétaires de voitures à l'aide de l'apprentissage automatique, et d'exposer cette fonctionnalité via une API et un tableau de bord Streamlit.
Fonctionnalités :

    Modèle d'Apprentissage Automatique : Prédire le prix de location quotidien en fonction des détails de la voiture.
    API FastAPI : Exposer le modèle via une API permettant aux utilisateurs de soumettre des détails sur une voiture et de recevoir des prédictions sur le prix de location.
    Tableau de bord Streamlit : Une interface conviviale pour soumettre des détails de voiture et afficher les prédictions.
    Un Streamlit permettant une prediction facile et ergonomique
    Déploiement : Déployé sur Hugging Face Spaces pour un accès facile au tableau de bord et à l'API.
```
Structure du Projet
├── 1-streamlit.py            # Le streamlit Dashboard contenant les figures et analyse des treshold
├── 2-Training.ipynb          # Le notebook permettant l'apprentissage des models
├── 3-streamlit_predi.py      # Tableau de bord Streamlit pour prédire le prix de location
├── Z-EDA.ipynb               # Le notebook ayant permit l'exploration des données d'analyses
├── dockerfile                # Le Dockerfile permettant de deployer en local
├── api.py                    # Application FastAPI avec l'endpoint /predict
├── app.py                    # Démarre l'application FastAPI avec Uvicorn
├── models/
│   ├── rental_price_model.joblib    # Modèle d'apprentissage automatique entraîné
│   └── preprocessor.joblib          # Préprocesseur des données pour le modèle
│
├── requirements.txt           # Dépendances Python
└── README.md                  # Ce fichier
```

# Installation et Exécution en Local
Prérequis

    Python 3.9+
    Docker
    pip pour installer les dépendances

Installer les Dépendances

Pour configurer le projet en local, commencez par cloner ce dépôt et installer les dépendances nécessaires.

https://github.com/DBZ-V/Bloc-5-Getaround.git
cd getaround-api
pip install -r requirements.txt

# Exécuter l'API en Local
Avec Docker```
  docker build -t getaround-api .
  docker run -p 7860:7860 getaround-api```
  
Allez sur http://localhost:7860/docs#/
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
# Streamlit en local
Depuis le terminal
```
streamlit run 1-streamlit.py
```
Accès au dashboard
```
streamlit run 3-streamlit_predi.py
```
Accès au streamlit de prédiction érgonimique

# Formatage des Appel API
## local
Sur python
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
Terminal
```
curl -X POST "http://127.0.0.1:7860/predict" -H "Content-Type: application/json" -d "{\"data\":[{\"model_key\":\"string\",\"mileage\":int,\"engine_power\":int,\"fuel\":\"string\",\"paint_color\":\"string\",\"car_type\":\"string\",\"private_parking_available\":true,\"has_gps\":false,\"has_air_conditioning\":true,\"automatic_car\":false,\"has_getaround_connect\":true,\"has_speed_regulator\":false,\"winter_tires\":false}]}"


```
exemple
```
curl -X POST "http://127.0.0.1:7860/predict" -H "Content-Type: application/json" -d "{\"data\":[{\"model_key\":\"BMW\",\"mileage\":20000,\"engine_power\":120,\"fuel\":\"diesel\",\"paint_color\":\"black\",\"car_type\":\"sedan\",\"private_parking_available\":true,\"has_gps\":true,\"has_air_conditioning\":true,\"automatic_car\":false,\"has_getaround_connect\":true,\"has_speed_regulator\":true,\"winter_tires\":false}]}"


