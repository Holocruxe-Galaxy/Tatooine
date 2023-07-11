import tensorflow as tf

def test():
    print("model_utils is working.")

# Create input functions for training and evaluation
def generate_input(data, labels, num_epochs=100, shuffle=True, batch_size=32):
    try:
        input_fn = tf.data.Dataset.from_tensor_slices((data, labels))
        if shuffle:
            input_fn = input_fn.shuffle(buffer_size=len(data))
        input_fn = input_fn.repeat(num_epochs)
        input_fn = input_fn.batch(batch_size)
        return input_fn
    except Exception as e:
        print("Error in generate_input:", str(e))
        return None

# Create the model using a linear estimator algorithm
def create_linear_estimator(feature_columns, n_classes):
    try:
        linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns, n_classes=n_classes)
        return linear_est
    except Exception as e:
        print("Error in create_linear_estimator:", str(e))
        return None
    
# Train and evaluate the model using the input functions
def train(model, train_input, eval_input):
    try:
        # Train the model
        model.train(input_fn=train_input)

        # Evaluate the model
        result = model.evaluate(input_fn=eval_input)

        return result
    except Exception as e:
        print("Error in train:", str(e))
        return None
    
# Get predictions from the model
def predict(model, eval_input):
    try:
        # Get predictions from the model
        predictions = list(model.predict(input_fn=eval_input))

        return predictions
    except Exception as e:
        print("Error in predict:", str(e))
        return None
