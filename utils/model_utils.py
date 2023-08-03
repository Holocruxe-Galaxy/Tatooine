# model_utils.py
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from utils import debug_utils as debug_utils

logger = debug_utils.logger

# Get the features from the dataset and drop the predict columns
def get_features(dataset, predict):
    try:
        logger.debug("Getting the features...", extra={'color': '93'})
        features = np.array(dataset.drop(predict, axis=1))
        logger.info("Success!", extra={'color': '92'})
        return features
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None

# Get the labels from the dataset
def get_labels(dataset, predict):
    try:
        logger.debug("Getting the labels...", extra={'color': '93'})
        labels = np.array(dataset[predict])
        logger.info("Success!", extra={'color': '92'})
        return labels
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None

# Split the data into training and testing sets
def split_data(features, labels, test_size=0.3):
    try:
        logger.debug("Splitting the data...", extra={'color': '93'})
        features_train, features_evaluation, labels_train, labels_evaluation = train_test_split(features, labels, test_size=test_size)
        logger.info("Data split successfully!", extra={'color': '92'})        
        return features_train, features_evaluation, labels_train, labels_evaluation
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None, None, None, None

# Create a model
def create_model():
    try:
        model = DecisionTreeClassifier()
        return model
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None


# Train the model
def train_model(model, features_train, labels_train):
    try:
        model = model.fit(features_train, labels_train)
        return model
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None

# Evaluate two models and return the best one
def evaluate_accuracy(model1, model2, features_evaluation, labels_evaluation):
    try:
        logger.debug("Evaluating models...", extra={'color': '93'})
        score1 = model1.score(features_evaluation, labels_evaluation)
        score2 = model2.score(features_evaluation, labels_evaluation)
        if score1 > score2:
            logger.info("Model 1 is better!", extra={'color': '92'})
            return model1
        else:
            logger.info("Model 2 is better!", extra={'color': '92'})
            return model2
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None

# Predict the next meal
def predict_next_meal(model, features_evaluation):
    try:
        logger.debug("Predicting the next meal...", extra={'color': '93'})
        prediction = model.predict(features_evaluation)
        logger.info("Prediction done successfully!", extra={'color': '92'})
        return prediction
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None

# Save the model
def save_model(model, path):
    try:
        logger.debug("Saving model...", extra={'color': '93'})
        with open(path, 'wb') as f:
            pickle.dump(model, f)
        logger.info("Model saved!", extra={'color': '92'})
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})

# Load the model
def load_model(path):
    try:
        with open(path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None

# Check if the user has a model
def check_model(user):
    try:        
        with open(f"models/{user}_holocheff.pkl", 'rb') as f:
            return True
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return False