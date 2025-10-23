from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# Enable CORS for your frontend
origins = [
    "http://localhost:3000",  # your frontend URL
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow your frontend
    allow_credentials=True,
    allow_methods=["*"],    # allow POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

# Load your models (optional)
# heart_model = joblib.load("heart_model.pkl")
# liver_model = joblib.load("liver_model.pkl")

# Input data model
class InputData(BaseModel):
    age: int
    cholesterol: float
    blood_pressure: float

# Heart prediction endpoint
@app.post("/predict/heart")
def predict_heart(data: InputData):
    # Replace with real model prediction
    return {"prediction": 0}  # 0 = healthy, 1 = disease

# Liver prediction endpoint
@app.post("/predict/liver")
def predict_liver(data: InputData):
    # Replace with real model prediction
    return {"prediction": 0}  # 0 = healthy, 1 = disease
