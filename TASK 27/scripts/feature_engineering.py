from sklearn.preprocessing import StandardScaler

# Assuming X_train and X_test are already defined after splitting the data
# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler on the training data and transform it
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test data using the same scaler 
X_test_scaled = scaler.transform(X_test)

