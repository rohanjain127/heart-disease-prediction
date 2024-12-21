from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load("heart_disease_best_model.joblib")

# Define request model for input data (matching the transformed feature names)
class HeartDiseaseFeatures(BaseModel):
    log_age: float
    log_resting_bp_s: float  
    log_cholesterol: float
    log_max_heart_rate: float
    log_oldpeak: float
    scale_age: float
    scale_resting_bp_s: float
    scale_cholesterol: float
    scale_max_heart_rate: float
    scale_oldpeak: float  
    minmax_age: float 
    minmax_resting_bp_s: float
    minmax_cholesterol: float
    minmax_max_heart_rate: float
    minmax_oldpeak: float
    sex_1: int
    fasting_blood_sugar_1: int
    exercise_angina_1: int 
    chest_pain_type_2: int
    chest_pain_type_3: int
    chest_pain_type_4: int
    resting_ecg_1: int
    resting_ecg_2: int
    st_slope_1: int  
    st_slope_2: int
    st_slope_3: int

# Root route (health check)
@app.get("/")
def root():
    return {"message": "Heart Disease Prediction API is up and running"}

# Prediction endpoint
@app.post("/predict")
def predict(request: HeartDiseaseFeatures):
    try:
        # Convert input to numpy array in the correct order
        input_data = np.array([[
            request.log_age, request.log_resting_bp_s, request.log_cholesterol,
            request.log_max_heart_rate, request.log_oldpeak,
            request.scale_age, request.scale_resting_bp_s, request.scale_cholesterol,
            request.scale_max_heart_rate, request.scale_oldpeak,
            request.minmax_age, request.minmax_resting_bp_s, request.minmax_cholesterol,
            request.minmax_max_heart_rate, request.minmax_oldpeak,
            request.sex_1, request.fasting_blood_sugar_1, request.exercise_angina_1,
            request.chest_pain_type_2, request.chest_pain_type_3, request.chest_pain_type_4,
            request.resting_ecg_1, request.resting_ecg_2,
            request.st_slope_1, request.st_slope_2, request.st_slope_3
        ]])

        # Make prediction
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)[:, 1]

        # Convert numpy types to native Python types
        prediction = int(prediction[0])
        prediction_proba = float(prediction_proba[0])

        # Return result
        return {
            "prediction": prediction,
            "probability": round(prediction_proba, 3)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)

