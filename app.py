import uvicorn
from api import app  # Importer ton app FastAPI depuis api.py

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
