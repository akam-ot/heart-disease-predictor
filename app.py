import streamlit as st
import joblib
import pandas as pd

# Load trained model and preprocessor
model = joblib.load("svm_heart_disease_model.joblib")
preprocessor = joblib.load("preprocessor.joblib")

st.title("❤️ Heart Disease Predictor")

# Input form
age = st.slider("Age", 28, 77, 50)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ASY", "NAP", "ATA", "TA"])
resting_bp = st.number_input("Resting Blood Pressure", min_value=50, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120?", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.number_input("Max Heart Rate", min_value=60, max_value=202, value=140)
exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"])
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=-2.0, max_value=6.2, value=0.0, step=0.1)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Format input
input_dict = {
    "Age": age,
    "Sex": sex,
    "ChestPainType": chest_pain,
    "RestingBP": resting_bp,
    "Cholesterol": cholesterol,
    "FastingBS": fasting_bs,
    "RestingECG": resting_ecg,
    "MaxHR": max_hr,
    "ExerciseAngina": exercise_angina,
    "Oldpeak": oldpeak,
    "ST_Slope": st_slope
}
input_df = pd.DataFrame([input_dict])

# Prediction
if st.button("Predict"):
    X_transformed = preprocessor.transform(input_df)
    prediction = model.predict(X_transformed)[0]

    if prediction == 1:
        st.error("⚠️ High Risk: Likely has heart disease.")
    else:
        st.success("✅ Low Risk: Likely healthy.")
