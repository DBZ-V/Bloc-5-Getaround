# Utiliser une image Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY models models
COPY api.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par FastAPI
EXPOSE 7860

# Lancer l’API avec Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]
