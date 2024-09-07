import keras_tuner as kt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

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

# Define the model building function
def build_model(hp):
    model = Sequential()
    model.add(Dense(units=hp.Int('units', min_value=32, max_value=512, step=32), activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(1))  # Output layer for regression
    model.compile(optimizer=Adam(learning_rate=hp.Choice('learning_rate', [1e-2, 1e-3, 1e-4])), loss='mean_squared_error')
    return model

# Initialize the Keras Tuner
tuner = kt.RandomSearch(build_model, objective='val_loss', max_trials=5, executions_per_trial=3, overwrite=True)

# Perform the hyperparameter tuning
tuner.search(X_train, y_train, epochs=50, validation_split=0.2)

# Get the best hyperparameters
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

# Output the best hyperparameters
print("Best hyperparameters found for Neural Network: ", best_hps)
