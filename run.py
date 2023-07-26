import sys
from utils import data as data_utils, model as model_utils, debug as debug_utils

logger = debug_utils.logger


# Get the data
data = data_utils.get_data()

# Get the users
users = data['user_id'].unique()

# Format the data
dataset = data_utils.format_data(data)

# Get the predict columns
predict = ['food_id']

# Convert data to numpy array and drop the predict columns
features = model_utils.get_features(dataset, predict)
labels = model_utils.get_labels(dataset, predict)

# Split the data into training and testing sets
features_train, features_evaluation, labels_train, labels_evaluation = model_utils.split_data(features, labels)

for user_id in users:
    # Check if the user has a model
    if model_utils.check_model(user_id):
        # Load the model
        model = model_utils.load_model(f'models/{user_id}_holocheff.pkl')
        # Predict the next meal
        prediction = model_utils.predict_next_meal(model, features_evaluation)
        # Print the next meal
        logger.info(prediction[-1][0])
        # Continue to the next user
        continue

    # Create a model
    model = model_utils.create_model()

    # Initial training
    model = model_utils.train_model(model, features_train, labels_train)

    # Save the model
    model_utils.save_model(model, f'models/{user_id}_holocheff.pkl')

    # Predict the next meal
    prediction = model_utils.predict_next_meal(model, features_evaluation)
    logger.info(prediction[-1][0])

