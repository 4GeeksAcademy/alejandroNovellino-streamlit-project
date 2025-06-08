import streamlit as st

from packages.dtos import OnePredictionInputDto
from packages.wrapper import LogisticRegressionModelWrapper

# load the ML model
model_wrapper = LogisticRegressionModelWrapper(
    model_path="./models/model.pkl",
    label_encoder_path="./models/encoder.pkl"
)

st.set_page_config(page_title="Crop prediction", layout="centered")

st.title("🌾 Prediction of the ideal crop for your land")

st.markdown("Enter the characteristics of the terrain to predict the most suitable crop.")

# Formulario
with st.form("prediction_form"):
    N = st.number_input("N (mg/kg)", min_value=0.0)
    P = st.number_input("P (mg/kg)", min_value=0.0)
    K = st.number_input("K (mg/kg)", min_value=0.0)
    temperature = st.number_input("temperature (°C)")
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
    ph = st.number_input("pH", min_value=0.0, max_value=14.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

    submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        # prepare the input features for prediction
        features = {
            "N": N,
            "P": P,
            "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }
        # make the prediction
        prediction = model_wrapper.predict_one(features).prediction

        st.success(f"🌱 Recommended crop: **{prediction}**")
