from fastapi import FastAPI
import joblib
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.constants import OUT_MODEL
random_forest = joblib.load(OUT_MODEL)

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World!"}

# make a prediction based on the input features, where you get the features in the request body
@app.post("/predict/")
async def predict(features: dict):
  features = [features['feature']]
  prediction = random_forest.predict(features)
  return {"prediction": prediction[0]}
