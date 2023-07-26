import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from utils import debug as debug_utils

logger = debug_utils.logger

# Get the features from the dataset and drop the predict columns
def get_features(dataset, predict):
    try:
        logger.debug("Getting the features...", extra={'color': '93'})
        features = np.array(dataset.drop(predict, axis=1))
        logger.info("Task successfully done!", extra={'color': '92'})
        return features
    except Exception as e:
        logger.error(f"Error occurred: {e}", extra={'color': '91'})
        return None

# Get the labels from the dataset
def get_labels(dataset, predict):
    try:
        logger.debug("get_labels: Getting the labels...", extra={'color': '93'})
        labels = np.array(dataset[predict])
        logger.info("get_labels: Task successfully done!", extra={'color': '92'})
        return labels
    except Exception as e:
        logger.error(f"get_labels: Error occurred: {e}", extra={'color': '91'})
        return None

# Split the data into training and testing sets
def split_data(features, labels, test_size=0.3):
    try:
        logger.debug("split_data: Splitting the data...", extra={'color': '93'})
        features_train, features_evaluation, labels_train, labels_evaluation = train_test_split(features, labels, test_size=test_size)
        logger.info("split_data: Data split successfully!", extra={'color': '92'})        
        return features_train, features_evaluation, labels_train, labels_evaluation
    except Exception as e:
        logger.error(f"split_data: Error occurred: {e}", extra={'color': '91'})
        return None, None, None, None

# Create a model
def create_model():
    try:
        logger.debug("create_model: Creating a model...", extra={'color': '93'})
        model = LinearRegression()
        logger.info("create_model: Model created successfully!", extra={'color': '92'})
        return model
    except Exception as e:
        logger.error(f"create_model: Error occurred: {e}", extra={'color': '91'})
        return None

# Train the model
def train_model(model, features_train, labels_train):
    try:
        logger.debug("train_model: Training the model...", extra={'color': '93'})
        model = model.fit(features_train, labels_train)
        logger.info("train_model: Model trained successfully!", extra={'color': '92'})
        return model
    except Exception as e:
        logger.error(f"train_model: Error occurred: {e}", extra={'color': '91'})
        return None

# Evaluate two models and return the best one
def evaluate_accuracy(model1, model2, features_evaluation, labels_evaluation):
    try:
        logger.debug("evaluate_models: Evaluating models...", extra={'color': '93'})
        score1 = model1.score(features_evaluation, labels_evaluation)
        score2 = model2.score(features_evaluation, labels_evaluation)
        if score1 > score2:
            logger.info("evaluate_models: Model 1 is better!", extra={'color': '92'})
            return model1
        else:
            logger.info("evaluate_models: Model 2 is better!", extra={'color': '92'})
            return model2
    except Exception as e:
        logger.error(f"evaluate_models: Error occurred: {e}", extra={'color': '91'})
        return None

# Predict the next meal
def predict_next_meal(model, features_evaluation):
    try:
        logger.debug("predict_next_meal: Predicting the next meal...", extra={'color': '93'})
        prediction = model.predict(features_evaluation)
        logger.info("predict_next_meal: Prediction done successfully!", extra={'color': '92'})
        return prediction
    except Exception as e:
        logger.error(f"predict_next_meal: Error occurred: {e}", extra={'color': '91'})
        return None

# Save the model
def save_model(model, path):
    try:
        logger.debug("save_model: Saving model...", extra={'color': '93'})
        with open(path, 'wb') as f:
            pickle.dump(model, f)
        logger.info("save_model: Model saved successfully!", extra={'color': '92'})
    except Exception as e:
        logger.error(f"save_model: Error occurred: {e}", extra={'color': '91'})

# Load the model
def load_model(path):
    try:
        logger.debug("load_model: Loading model...", extra={'color': '93'})
        with open(path, 'rb') as f:
            model = pickle.load(f)
        logger.info("load_model: Model loaded successfully!", extra={'color': '92'})
        return model
    except Exception as e:
        logger.error(f"load_model: Error occurred: {e}", extra={'color': '91'})
        return None

# Check if the user has a model
def check_model(user):
    try:
        logger.debug("check_model: Checking if the user has a model...", extra={'color': '93'})
        with open(f'models/{user}_holocheff.pkl', 'rb'):
            logger.info("check_model: Model found!", extra={'color': '92'})
            return True
    except FileNotFoundError:
        logger.error("check_model: Model not found!", extra={'color': '91'})
        return False
    except Exception as e:
        logger.error(f"check_model: Error occurred: {e}", extra={'color': '91'})
        return False
