from sklearn.metrics import mean_squared_error, r2_score
from model import rf_model, nn_model

# Random Forest Evaluation
rf_predictions = rf_model.predict(X_test_scaled)  
rf_mse = mean_squared_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)
print(f"Random Forest MSE: {rf_mse}")
print(f"Random Forest R²: {rf_r2}")

# Neural Network Evaluation
nn_predictions = nn_model.predict(X_test_scaled)  
nn_mse = mean_squared_error(y_test, nn_predictions)
nn_r2 = r2_score(y_test, nn_predictions)
print(f"Neural Network MSE: {nn_mse}")
print(f"Neural Network R²: {nn_r2}")
