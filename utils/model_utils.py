
import joblib
import os
from bson.binary import Binary
from io import BytesIO
from sklearn.tree import DecisionTreeClassifier
from utils import debug_utils as debug_utils
from utils.data_utils import Data

class Model:
        
    def __init__(self,data : Data):
        self.logger = debug_utils.logger
        self.data = data        
        self.model = self.load(data.user_id)

    # Define a model    
    def define(self):
        try:
            model = DecisionTreeClassifier()
            return model
        except Exception as e:
            self.logger.error(f"Error occurred while defining the model: {e}", extra={'color': '91'})
            return None
        
    # Train the model
    def train(self):
        try:     
            self.model = self.model.fit(self.data.features_train, self.data.labels_train)
            return self.model
        except Exception as e:
            self.logger.error(f"Error occurred while training the model: {e}", extra={'color': '91'})
            return None
        
    # Save the model
    def save(self, user_id):
        try:
            # Serialize the model to a byte stream
            buffer = BytesIO()
            joblib.dump(self.model, buffer)
            buffer.seek(0)
            binary_data = Binary(buffer.read())

            # Use existing connection method
            database = self.data.mongodb_connection()

            # Add a 'model' field to the user's document containing the serialized model
            database.data.update_one({"user_id": user_id}, {"$set": {"model": binary_data}})
        except Exception as e:
            self.logger.error(f"Error occurred while saving: {e}", extra={'color': '91'})
            return None



    # Load the model from the path if it exists, else define a new model
    def load(self,user_id):
        # Use existing connection method
        database = self.data.mongodb_connection()

        user_data = database.data.find_one({"user_id": user_id})

        # Check if the model exists
        if user_data and "model" in user_data:
            # Load model from binary data
            buffer = BytesIO(user_data["model"])
            self.model = joblib.load(buffer)
        else:
            # Define and train a new model
            self.model = self.define()      
            self.train()
            self.save(user_id)
        return self.model

    def output(self):
        # output the next meal prediction
        try:
            # Get the features from the last row of the features
            features = self.data.features[-1].reshape(1,-1)
            prediction = self.model.predict(features)[0]
            # Get the label from the label encoder
            prediction = self.data.encoder.inverse_transform([prediction])[0]
            self.logger.info(f"Next meal prediction: {prediction}", extra={'color': '92'})
            return prediction
        except Exception as e:
            self.logger.error(f"Error occurred: {e}", extra={'color': '91'})
            return None

