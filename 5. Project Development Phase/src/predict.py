import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/crop_model.pkl")

# Get input from the user
N = float(input("Enter Nitrogen (N): "))
P = float(input("Enter Phosphorus (P): "))
K = float(input("Enter Potassium (K): "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
ph = float(input("Enter pH: "))
rainfall = float(input("Enter Rainfall: "))

# Create a DataFrame with the input
data = pd.DataFrame([{
    "N": N,
    "P": P,
    "K": K,
    "temperature": temperature,
    "humidity": humidity,
    "ph": ph,
    "rainfall": rainfall
}])

# Predict the crop
prediction = model.predict(data)

print(f"\nRecommended Crop: {prediction[0]}")