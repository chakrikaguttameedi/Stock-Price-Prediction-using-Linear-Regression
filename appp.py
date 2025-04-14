import joblib  # To load the saved model
import streamlit as st  # Streamlit for web app
import numpy as np  # For numerical operations

# Load the trained model
model_filename = "stock_price_model.pkl"
model = joblib.load(model_filename)

# Streamlit App Title
st.title("Stock Price Prediction App")

# User input field
user_input = st.number_input("Enter TL BASED ISE (Opening Price in TL):", min_value=0.0, format="%.2f")

# Predict button
if st.button("Predict"):
    try:
        user_input_array = np.array([[user_input]])  # Convert to 2D array for prediction
        predicted_price = model.predict(user_input_array)[0]
        st.success(f"Predicted USD BASED ISE (Closing Price in USD): {predicted_price:.2f}")
    except Exception as e:
        st.error(f"Error in prediction: {str(e)}")

# Run this script using: streamlit run filename.py
