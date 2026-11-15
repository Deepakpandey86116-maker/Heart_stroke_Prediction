
import streamlit as st

st.set_page_config(
    page_title="Heart Stroke Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("HEART STROKE PREDICTION MODEL ❤️")

st.write("Provide the following details--")

age = st.slider("Age", 1, 100, 40)

sex = st.selectbox("SEX", ["M", "F"])

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "ASY", "TA"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=0, value=120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dl)",
    min_value=0, value=200
)

fasting_bs = st.selectbox(
    "Fasting Blood sugar > 120 mg/dl",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.slider("MAX heart RATE", 60, 220, 150)

exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)

oldpeak = st.slider(
    "Oldpeak (ST depression)",
    0.0, 6.0, 1.0, 0.1
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

if st.button("Predict"):
    st.info(
        "Input received successfully. "
        "Machine Learning model integration is pending."
    )
