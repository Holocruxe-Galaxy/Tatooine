import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



# Get the predict columns
def get_features(dataset, predict):
    return np.array(dataset.drop(predict, axis=1))

def get_labels(dataset, predict):
    return np.array(dataset[predict])

# Split the data into training and testing sets
def split_data(features, labels, test_size=0.3):
    return train_test_split(features, labels, test_size=test_size)

# Create a model
def create_model():
    return LinearRegression()

# Train the model
def train_model(model, features_train, labels_train):
    return model.fit(features_train, labels_train)

# Predict the next meal
def predict_next_meal(model, features_evaluation):
    return model.predict(features_evaluation)

# Save the model
def save_model(model, path):
    with open(path, 'wb') as f:
        pickle.dump(model, f)

# Check if the user has a model
def check_model(user):
    try:
        with open(f'models/{user}_holocheff.pkl', 'rb') as f:
            return True
    except:
        return False

# Load the model
def load_model(path):
    with open(path, 'rb') as f:
        return pickle.load(f)