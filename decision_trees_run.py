import sys
from utils import debug_utils as debug_utils
from utils import data_utils as data_utils
from utils import model_utils as model_utils
logger = debug_utils.logger


# Get the data
data = data_utils.get_data()

# Format the data
data = data_utils.format_data_OneHotEncoder(data)

predict = 'food'
# Get the features
features = model_utils.get_features(data, predict)

# Get the labels
labels = model_utils.get_labels(data, predict)

# Split the data
features_train, features_evaluation, labels_train, labels_evaluation = model_utils.split_data(features, labels)

# Create a model
model = model_utils.create_model()

# Train the model
model = model_utils.train_model(model, features_train, labels_train)

#print model coefficients and accuracy as percentage
print("Model Accuracy: ", model.score(features_train, labels_train)*100)
