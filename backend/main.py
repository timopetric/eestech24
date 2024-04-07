from fastapi import FastAPI
import joblib
import sys
import os

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.constants import OUT_MODEL
random_forest = joblib.load(OUT_MODEL)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
  return {"message": "Hello World!"}

# make a prediction based on the input features, where you get the features in the request body. Also save the prediction in the database.
@app.post("/predict/")
async def predict(features: schemas.PredictionCreate, db: Session = Depends(get_db)):
  features = [features['feature']]
  prediction = random_forest.predict(features)
  # now save the prediction in the database
  crud.save_prediction(db, features, prediction[0])
  return {"prediction": prediction[0]}
