import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 1: Load the dataset
file_path = '/Users/zoobiasyed/Downloads/AQUASTAT Dissemination System.csv'
data = pd.read_csv(file_path)

# Step 2: Data Exploration and Preprocessing
# Dropping irrelevant columns: 'Symbol', 'IsAggregate' (as they do not contribute to the prediction)
data.drop(['Symbol', 'IsAggregate'], axis=1, inplace=True)

# Check for missing values
print("Missing values:\n", data.isnull().sum())

# Convert categorical variables using OneHotEncoding: 'VariableGroup', 'Subgroup', 'Variable', 'Area', and 'Unit'
categorical_columns = ['VariableGroup', 'Subgroup', 'Variable', 'Area', 'Unit']
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_categorical = encoder.fit_transform(data[categorical_columns])

# Convert the encoded categorical features to a DataFrame
encoded_df = pd.DataFrame(encoded_categorical, columns=encoder.get_feature_names_out(categorical_columns))

# Combine encoded categorical features with the rest of the data
data_encoded = pd.concat([encoded_df, data[['Year', 'Value']]], axis=1)

# Step 3: Feature Scaling
# Separate features and target variable
X = data_encoded.drop('Value', axis=1) 
y = data_encoded['Value']              

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Splitting the Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 5: Model Implementation - RandomForestRegressor for Regression
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Step 6: Model Evaluation - Random Forest
y_pred_rf = rf_model.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
print(f'Random Forest Regression - Mean Squared Error: {mse_rf}, R-Squared: {r2_rf}')

# Step 7: Model Implementation - Neural Network for Regression
nn_model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)  # Single output neuron for regression
])

nn_model.compile(optimizer='adam', loss='mean_squared_error')
nn_model.fit(X_train, y_train, epochs=50, validation_split=0.2)

# Step 8: Model Evaluation - Neural Network
y_pred_nn = nn_model.predict(X_test)
mse_nn = mean_squared_error(y_test, y_pred_nn)
r2_nn = r2_score(y_test, y_pred_nn)
print(f'Neural Network Regression - Mean Squared Error: {mse_nn}, R-Squared: {r2_nn}')

# Step 9: Visualization of Results
# Plot predictions vs actual values for both models
plt.figure(figsize=(12, 6))

# Random Forest Predictions
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred_rf, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.title('Random Forest Predictions vs Actual')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')

# Neural Network Predictions
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_nn, color='green')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.title('Neural Network Predictions vs Actual')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')

plt.tight_layout()
plt.show()

