import streamlit as st
import joblib
import pandas as pd
import numpy as np
import requests

# Charger le modèle et le préprocesseur avec joblib
model = joblib.load('models/rental_price_model.joblib')
preprocessor = joblib.load('models/preprocessor.joblib')

# Créer l'application Streamlit
st.title("Getaround Car Rental Pricing Optimization")
st.write("Enter the details below to get the predicted rental price for a car.")

# Créer un formulaire pour l'utilisateur
model_key = st.selectbox("Select Car Model", ["Citroën", "PGO", "Toyota", "BMW", "Mercedes", "Renault", "Volkswagen"])
mileage = st.number_input("Mileage", min_value=0, value=1000)
engine_power = st.number_input("Engine Power (HP)", min_value=0, value=100)
fuel = st.selectbox("Fuel", ["diesel", "petrol", "electric"])
paint_color = st.selectbox("Paint Color", ["black", "grey", "white", "blue", "red", "green"])
car_type = st.selectbox("Car Type", ["convertible", "sedan", "SUV", "hatchback", "coupe"])
private_parking_available = st.checkbox("Private Parking Available")
has_gps = st.checkbox("Has GPS")
has_air_conditioning = st.checkbox("Has Air Conditioning")
automatic_car = st.checkbox("Automatic Car")
has_getaround_connect = st.checkbox("Has Getaround Connect")
has_speed_regulator = st.checkbox("Has Speed Regulator")
winter_tires = st.checkbox("Winter Tires")

# Créer un bouton pour prédire
if st.button("Predict Rental Price"):
    # Collecter les données dans une liste, avec l'ordre correct des colonnes
    input_data = [
        [model_key, mileage, engine_power, fuel, paint_color, car_type, 
         private_parking_available, has_gps, has_air_conditioning, automatic_car, 
         has_getaround_connect, has_speed_regulator, winter_tires]
    ]
    
    # Convertir les données en DataFrame
    input_data_df = pd.DataFrame(input_data, columns=["model_key", "mileage", "engine_power", "fuel", "paint_color", "car_type",
                                                     "private_parking_available", "has_gps", "has_air_conditioning", "automatic_car", 
                                                     "has_getaround_connect", "has_speed_regulator", "winter_tires"])

    # Appliquer le préprocesseur sur les données d'entrée
    processed_data = preprocessor.transform(input_data_df)

    # Faire la prédiction avec le modèle
    prediction = model.predict(processed_data)

    # Afficher la prédiction
    st.write(f"The predicted rental price per day is: ${prediction[0]:.2f}")