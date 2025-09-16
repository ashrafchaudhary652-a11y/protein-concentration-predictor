
# protein_predictor.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# --- Step 1: Sample Data ---
data = {
    "protein_grams": [100, 200, 300, 400, 500, 600, 700, 800],
    "eluate_volume_L": [10, 20, 30, 35, 40, 44, 50, 55],
    "protein_concentration": [10, 10, 10, 11, 12, 11, 14, 15],  # target
}

df = pd.DataFrame(data)

# --- Step 2: Split features and target ---
X = df[["protein_grams", "eluate_volume_L"]]
y = df["protein_concentration"]

# --- Step 3: Train model ---
model = LinearRegression()
model.fit(X, y)

# --- Step 4: Streamlit UI ---
st.title("Protein Concentration Predictor")
st.write("Enter protein amount and eluate volume (you can include decimals):")

protein_input = st.number_input(
    "Protein amount (grams)",
    value=600.0,
    min_value=0.0,
    step=0.1,
    format="%.2f",
)
volume_input = st.number_input(
    "Eluate volume (L)",
    value=44.0,
    min_value=0.0,
    step=0.1,
    format="%.2f",
)

if st.button("Predict"):
    input_features = pd.DataFrame(
        [[protein_input, volume_input]],
        columns=["protein_grams", "eluate_volume_L"],
    )
    prediction = model.predict(input_features)
    st.success(f"Predicted Protein Concentration: {prediction[0]:.2f} g/L")
