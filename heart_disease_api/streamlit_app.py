import streamlit as st
import requests

# Title
st.title("Heart Disease Prediction App")

# Input Form
st.write("Enter patient data below:")

# Feature Input Fields (One by One)
log_age = st.number_input("Log Age", min_value=0.0, step=0.1)
log_resting_bp_s = st.number_input("Log Resting BP (Systolic)", min_value=0.0, step=0.1)
log_cholesterol = st.number_input("Log Cholesterol", min_value=0.0, step=0.1)
log_max_heart_rate = st.number_input("Log Max Heart Rate", min_value=0.0, step=0.1)
log_oldpeak = st.number_input("Log Oldpeak", min_value=0.0, step=0.1)

scale_age = st.number_input("Scale Age", min_value=0.0, step=0.1)
scale_resting_bp_s = st.number_input("Scale Resting BP (Systolic)", min_value=0.0, step=0.1)
scale_cholesterol = st.number_input("Scale Cholesterol", min_value=0.0, step=0.1)
scale_max_heart_rate = st.number_input("Scale Max Heart Rate", min_value=0.0, step=0.1)
scale_oldpeak = st.number_input("Scale Oldpeak", min_value=0.0, step=0.1)

minmax_age = st.number_input("MinMax Age", min_value=0.0, step=0.1)
minmax_resting_bp_s = st.number_input("MinMax Resting BP (Systolic)", min_value=0.0, step=0.1)
minmax_cholesterol = st.number_input("MinMax Cholesterol", min_value=0.0, step=0.1)
minmax_max_heart_rate = st.number_input("MinMax Max Heart Rate", min_value=0.0, step=0.1)
minmax_oldpeak = st.number_input("MinMax Oldpeak", min_value=0.0, step=0.1)

sex_1 = st.selectbox("Sex (1 for Male, 0 for Female)", [0, 1])
fasting_blood_sugar_1 = st.selectbox("Fasting Blood Sugar (1 for True, 0 for False)", [0, 1])
exercise_angina_1 = st.selectbox("Exercise Induced Angina (1 for Yes, 0 for No)", [0, 1])

chest_pain_type_2 = st.selectbox("Chest Pain Type 2 (1 for Yes, 0 for No)", [0, 1])
chest_pain_type_3 = st.selectbox("Chest Pain Type 3 (1 for Yes, 0 for No)", [0, 1])
chest_pain_type_4 = st.selectbox("Chest Pain Type 4 (1 for Yes, 0 for No)", [0, 1])

resting_ecg_1 = st.selectbox("Resting ECG 1 (1 for Yes, 0 for No)", [0, 1])
resting_ecg_2 = st.selectbox("Resting ECG 2 (1 for Yes, 0 for No)", [0, 1])

st_slope_1 = st.selectbox("ST Slope 1 (1 for Yes, 0 for No)", [0, 1])
st_slope_2 = st.selectbox("ST Slope 2 (1 for Yes, 0 for No)", [0, 1])
st_slope_3 = st.selectbox("ST Slope 3 (1 for Yes, 0 for No)", [0, 1])

# Collect Input Data
input_data = {
    "log_age": log_age,
    "log_resting_bp_s": log_resting_bp_s,
    "log_cholesterol": log_cholesterol,
    "log_max_heart_rate": log_max_heart_rate,
    "log_oldpeak": log_oldpeak,
    "scale_age": scale_age,
    "scale_resting_bp_s": scale_resting_bp_s,
    "scale_cholesterol": scale_cholesterol,
    "scale_max_heart_rate": scale_max_heart_rate,
    "scale_oldpeak": scale_oldpeak,
    "minmax_age": minmax_age,
    "minmax_resting_bp_s": minmax_resting_bp_s,
    "minmax_cholesterol": minmax_cholesterol,
    "minmax_max_heart_rate": minmax_max_heart_rate,
    "minmax_oldpeak": minmax_oldpeak,
    "sex_1": sex_1,
    "fasting_blood_sugar_1": fasting_blood_sugar_1,
    "exercise_angina_1": exercise_angina_1,
    "chest_pain_type_2": chest_pain_type_2,
    "chest_pain_type_3": chest_pain_type_3,
    "chest_pain_type_4": chest_pain_type_4,
    "resting_ecg_1": resting_ecg_1,
    "resting_ecg_2": resting_ecg_2,
    "st_slope_1": st_slope_1,
    "st_slope_2": st_slope_2,
    "st_slope_3": st_slope_3
}

# Submit Button
if st.button("Predict"):
    response = requests.post(
        "https://heart-disease-api-latest.onrender.com/predict",
        json=input_data
    )
    
    if response.status_code == 200:
        st.success("Prediction: " + str(response.json()))
    else:
        st.error("Error: " + str(response.json()))

