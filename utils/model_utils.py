import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from utils import debug_utils as debug_utils

class Model:
        
    def __init__(self, data, predict):
        self.logger = debug_utils.logger
  # Split the data
        (
            self.features_train,
            self.features_evaluation,
            self.labels_train,
            self.labels_evaluation,
        ) = self.split_data(data, predict)      
        # Define the model
        self.model = self.define_model()
        # Train the model
        self.model = self.train_model(self.features_train, self.labels_train)
        

    # Get the features from the dataset and drop the predict columns
    def get_features(self, data, predict):
        try:
            self.logger.debug("Getting the features...", extra={'color': '93'})
            features = np.array(data.drop(predict, axis=1))
            self.logger.info("Success!", extra={'color': '92'})
            return features
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
            return None
        
    # Get the labels from the dataset
    def get_labels(self, data, predict):
        try:
            self.logger.debug("Getting the labels...", extra={'color': '93'})
            labels = np.array(data[predict])
            self.logger.info("Success!", extra={'color': '92'})
            return labels
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
            return None
        
    # Split the data into training and testing sets
    def split_data(self, data, predict, test_size=0.3):
        try:
            self.logger.debug("Splitting the data...", extra={'color': '93'})
            features_train, features_evaluation, labels_train, labels_evaluation = train_test_split(self.get_features(data, predict), self.get_labels(data,predict), test_size=test_size)
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
        try:
            joblib.dump(self.model, path)
            self.logger.info(f"Model saved successfully to {path}!", extra={'color': '92'})
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})

    def load_model(self, path):
        try:
            self.model = joblib.load(path)
            self.logger.info(f"Model loaded successfully from {path}!", extra={'color': '92'})
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})

    def evaluate_model(self, features_evaluation, labels_evaluation):
        try:
            self.logger.debug("Evaluating model...", extra={'color': '93'})
            # Get the accuracy score as a percentage
            score = self.model.score(features_evaluation, labels_evaluation) * 100
            
            self.logger.info(f"Model accuracy: {score:.2f}%", extra={'color': '92'})
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})

    
