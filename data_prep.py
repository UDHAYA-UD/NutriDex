# ===========================
# NutriDex - ML Model Builder
# ===========================
# This script reads foods.csv, trains a KNN model,
# and saves it as a pickle (.pkl) file.

# Step 1: Import libraries
import pandas as pd                          # For reading CSV data
from sklearn.neighbors import NearestNeighbors  # Our ML algorithm
from sklearn.preprocessing import StandardScaler # To normalize the data
import pickle                                # To save our trained model

# Step 2: Load the dataset
print("Loading foods.csv...")
df = pd.read_csv('foods.csv')
df = df.fillna(0)  # Replace any missing values with 0
print(f"Loaded {len(df)} foods!")

# Step 3: Select the features (columns) we want the model to learn from
features = ['calories', 'protein', 'carbs', 'fat']
X = df[features]

# Step 4: Scale the data (makes all numbers comparable)
# Without this, calories (130) would dominate over protein (2.7)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Train the KNN model
# KNN = K-Nearest Neighbors - it finds the closest matching foods
model = NearestNeighbors(n_neighbors=5, metric='euclidean')
model.fit(X_scaled)
print("Model trained successfully!")

# Step 6: Save everything into a pickle file
# We save: the model, the scaler, and the dataframe
model_data = {
    'model': model,
    'scaler': scaler,
    'dataframe': df
}

with open('food_model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

print("Saved as 'food_model.pkl' - Done!")
