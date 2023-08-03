import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from utils import debug_utils as debug_utils

class ModelUtils:
    
    def __init__(self, dataset, predict):
        self.logger = debug_utils.logger
        # Get the features
        self.features = self.get_features(dataset, predict)
        # Get the labels
        self.labels = self.get_labels(dataset, predict)
        # Split the data
        (
            self.features_train,
            self.features_evaluation,
            self.labels_train,
            self.labels_evaluation,
        ) = self.split_data(self.features, self.labels)
        # Define the model
        self.model = self.define_model()
        # Train the model
        self.model = self.train_model(self.features_train, self.labels_train)
        # Evaluate the model
        self.evaluate_model(self.features_evaluation, self.labels_evaluation)

    # Get the features from the dataset and drop the predict columns
    def get_features(self, dataset, predict):
        try:
            self.logger.debug("Getting the features...", extra={'color': '93'})
            features = np.array(dataset.drop(predict, axis=1))
            self.logger.info("Success!", extra={'color': '92'})
            return features
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
            return None
        
    # Get the labels from the dataset
    def get_labels(self, dataset, predict):
        try:
            self.logger.debug("Getting the labels...", extra={'color': '93'})
            labels = np.array(dataset[predict])
            self.logger.info("Success!", extra={'color': '92'})
            return labels
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
            return None
        
    # Split the data into training and testing sets
    def split_data(self, features, labels, test_size=0.3):
        try:
            self.logger.debug("Splitting the data...", extra={'color': '93'})
            features_train, features_evaluation, labels_train, labels_evaluation = train_test_split(features, labels, test_size=test_size)
            self.logger.info("Data split successfully!", extra={'color': '92'})        
            return features_train, features_evaluation, labels_train, labels_evaluation
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
            return None, None, None, None
        
    # Define a model    
    def define_model(self):
        try:
            self.logger.debug("Defining the model...", extra={'color': '93'})
            model = DecisionTreeClassifier()
            self.logger.info("Model defined successfully!", extra={'color': '92'})
            return model
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
            return None
        
    # Train the model
    def train_model(self, features_train, labels_train):
        try:
            self.logger.debug("Training the model...", extra={'color': '93'})
            self.model = self.model.fit(features_train, labels_train)
            self.logger.info("Model trained successfully!", extra={'color': '92'})
            return self.model
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
            return None
        
    def save_model(self, path):
        pass

    def load_model(self, path):
        pass
    def evaluate_model(self, features_evaluation, labels_evaluation):
        try:
            self.logger.debug("Evaluating model...", extra={'color': '93'})
            # Get the accuracy score as a percentage
            score = self.model.score(features_evaluation, labels_evaluation) * 100
            # if score < 40 color red if score > 40 and < 70 color yellow if score > 70 color green
            self.logger.info(f"Model accuracy: {score}", extra={'color': '92'})
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
    
