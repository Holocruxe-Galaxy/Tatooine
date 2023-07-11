import tensorflow as tf

# Create input functions for training and evaluation
def generate_input(dataframe, labels, batch_size=32, num_epochs=None, shuffle=True):
    def input_function():  # inner function, this will be returned
        feature_columns = []
        # Define your feature columns using tf.feature_column API
        for feature_name in dataframe.columns:
            feature_columns.append(tf.feature_column.numeric_column(feature_name))
        # create tf.data.Dataset object with data and its label
        ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
        if shuffle:
            ds = ds.shuffle(1000)
        # split dataset into batches of 32 and repeat process for number of epochs
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds  # return a batch of the dataset
    
    return input_function  # return a function object for use


# Create the model using a linear estimator algorithm
def create_linear_estimator(feature_columns, n_classes):
    try:        
        print("\033[93m" + "Creating linear estimator..." + "\033[0m")
        linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns, n_classes=n_classes)
        print("\033[92m" + "Linear estimator successfully created!" + "\033[0m")
        return linear_est
    except Exception as e:
        print("\033[91m" + "An error occurred while creating the linear estimator:", str(e) + "\033[0m")
        return None
    
# Train and evaluate the model using the input functions
def train(model, train_input, eval_input):
    try:
        print("\033[93m" + "Training the model..." + "\033[0m")
        # Train the model
        model.train(input_fn=train_input)
        print("\033[92m" + "Model successfully trained!" + "\033[0m")
        try:
            print("\033[93m" + "Evaluating the model..." + "\033[0m")
            # Evaluate the model
            result = model.evaluate(input_fn=eval_input)
            print("\033[92m" + "Model successfully evaluated!" + "\033[0m")
        except Exception as e:
            print("\033[91m" + "An error occurred while evaluating the model:", str(e) + "\033[0m")
            return None
        return result
    except Exception as e:
        print("\033[91m" + "An error occurred while training the model:", str(e) + "\033[0m")
        return None

    
# Get predictions from the model
def predict(model, eval_input):
    try:
        #print in yellow 
        print("\033[93m" + "Getting predictions from the model..." + "\033[0m")
        # Get predictions from the model
        predictions = list(model.predict(input_fn=eval_input))

        return predictions
    except Exception as e:
        print("\033[91m" + "An error occurred while getting predictions from the model:", str(e) + "\033[0m")
        return None
