from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Load the dataset
file_path = '/Users/zoobiasyed/Downloads/AQUASTAT Dissemination System.csv'
data = pd.read_csv(file_path)

# Data preprocessing
data.drop(['Symbol', 'IsAggregate'], axis=1, inplace=True)

# OneHotEncoding for categorical variables
categorical_columns = ['VariableGroup', 'Subgroup', 'Variable', 'Area', 'Unit']
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_categorical = encoder.fit_transform(data[categorical_columns])

# Convert to DataFrame
encoded_df = pd.DataFrame(encoded_categorical, columns=encoder.get_feature_names_out(categorical_columns))
data_encoded = pd.concat([encoded_df, data[['Year', 'Value']]], axis=1)

# Split features and target
X = data_encoded.drop('Value', axis=1)
y = data_encoded['Value']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the RandomForestRegressor
rf_model = RandomForestRegressor(random_state=42)

# Define hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_features': ['auto', 'sqrt'],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize RandomizedSearchCV
rf_random = RandomizedSearchCV(estimator=rf_model, param_distributions=param_grid, 
                               n_iter=100, cv=3, verbose=2, random_state=42, n_jobs=-1)

# Perform hyperparameter tuning
rf_random.fit(X_train, y_train)

# Output the best parameters
print("Best parameters found for Random Forest: ", rf_random.best_params_)
