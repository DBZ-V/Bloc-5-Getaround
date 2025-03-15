import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
delay_analysis = pd.read_excel("data/get_around_delay_analysis.xlsx")

# Nettoyer les données (retirer les "canceled")
delay_analysis_cleaned = delay_analysis[delay_analysis['state'] != 'canceled']

# Calculer les statistiques de base
median_delay = delay_analysis_cleaned['delay_at_checkout_in_minutes'].median()
q25 = delay_analysis_cleaned['delay_at_checkout_in_minutes'].quantile(0.25)
q75 = delay_analysis_cleaned['delay_at_checkout_in_minutes'].quantile(0.75)
iqr = q75 - q25

# Calcul du temps entre les locations successives
median_time_delta = delay_analysis['time_delta_with_previous_rental_in_minutes'].median()
q1_time_delta = delay_analysis['time_delta_with_previous_rental_in_minutes'].quantile(0.25)
q3_time_delta = delay_analysis['time_delta_with_previous_rental_in_minutes'].quantile(0.75)

# Calcul du pourcentage de locations avec un temps d'attente inférieur à 60 minutes
less_than_1_hour = delay_analysis[delay_analysis['time_delta_with_previous_rental_in_minutes'] <= 60]
percentage_less_than_1_hour = (len(less_than_1_hour) / len(delay_analysis)) * 100

# Afficher les résultats des statistiques
st.title("Analyse des Retards et des Délai Entre Locations")

# Affichage des statistiques de retard
st.write("### Statistiques des Retards à la Remise du Véhicule")
st.write(f"Médiane : {median_delay} minutes")
st.write(f"Premier quartile (Q1) : {q25} minutes")
st.write(f"Troisième quartile (Q3) : {q75} minutes")
st.write(f"Écart interquartile (IQR) : {iqr} minutes")

# Affichage des statistiques du temps entre les locations successives
st.write("### Statistiques du Temps Entre Deux Locations Successives")
st.write(f"Médiane du temps : {median_time_delta} minutes")
st.write(f"Premier quartile (Q1) : {q1_time_delta} minutes")
st.write(f"Troisième quartile (Q3) : {q3_time_delta} minutes")
st.write(f"Pourcentage des locations avec un temps d'attente inférieur à 60 minutes : {percentage_less_than_1_hour:.2f}%")

# Graphique : Boîte à moustaches des retards
st.write("### Distribution des Retards à la Remise du Véhicule")
plt.figure(figsize=(10,6))
sns.boxplot(data=delay_analysis_cleaned, x='delay_at_checkout_in_minutes')
plt.title('Boîte à Moustaches des Retards à la Remise du Véhicule')
plt.xlabel('Temps de Retard à la Remise du Véhicule (en minutes)')
st.pyplot()

# Graphique : Histogramme des temps entre deux locations successives
st.write("### Distribution du Temps Entre Deux Locations Successives")
plt.figure(figsize=(10,6))
plt.hist(delay_analysis['time_delta_with_previous_rental_in_minutes'], bins=30, edgecolor='black')
plt.title('Distribution du Temps Entre Deux Locations Successives')
plt.xlabel('Temps entre deux locations successives (en minutes)')
plt.ylabel('Fréquence')
st.pyplot()

# Calcul du seuil de 60 minutes
threshold = 60
affected_rentals_by_threshold = delay_analysis[delay_analysis['time_delta_with_previous_rental_in_minutes'] <= threshold]

# Affichage des résultats de l'impact du seuil
st.write(f"### Nombre de locations affectées par le seuil de {threshold} minutes")
st.write(f"Nombre de locations affectées : {len(affected_rentals_by_threshold)}")
st.write(f"Pourcentage des locations affectées : {percentage_less_than_1_hour:.2f}%")

# Calcul du pourcentage de retards sur la prochaine prise en charge
late_checkins = delay_analysis[delay_analysis['delay_at_checkout_in_minutes'] > 0]
late_percentage = (len(late_checkins) / len(delay_analysis)) * 100
st.write(f"### Pourcentage de retards sur la prochaine prise en charge")
st.write(f"Pourcentage de retards : {late_percentage:.2f}%")

# Nombre de cas problématiques avant et après l'application du seuil
problematic_cases_before = delay_analysis[delay_analysis['delay_at_checkout_in_minutes'] > 60]  # Exemples de retards > 1h
problematic_cases_after = affected_rentals_by_threshold[affected_rentals_by_threshold['delay_at_checkout_in_minutes'] > 60]
st.write(f"### Nombre de cas problématiques avant et après le seuil")
st.write(f"Nombre de cas problématiques avant le seuil : {len(problematic_cases_before)}")
st.write(f"Nombre de cas problématiques après le seuil : {len(problematic_cases_after)}")

