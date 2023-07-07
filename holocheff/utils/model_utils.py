import data_utils
import tensorflow as tf

#Create input function for training + evaluating
def make_input(data_df, label_df, num_epochs=500, shuffle=True, batch_size=32):
    def input_function():  # inner function, this will be returned
        # create tf.data.Dataset object with data and its label
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        # split dataset into batches of 32 and repeat process for number of epochs
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds  # return a batch of the dataset
    return input_function  # return a function object for use

#Create the model using Logistic Regression
def create_model(my_learning_rate, feature_layer):
    # Most simple tf.keras models are sequential.
    model = tf.keras.models.Sequential()
    # Add the layer containing the feature columns to the model.
    model.add(feature_layer)
    # Add one linear layer to the model to yield a simple linear regressor.
    model.add(tf.keras.layers.Dense(units=1, input_shape=(1,),
                                    activation=tf.sigmoid),)
    # Construct the layers into a model that TensorFlow can execute.
    model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=my_learning_rate),
                    loss="binary_crossentropy",
                    metrics=[tf.keras.metrics.BinaryAccuracy()])
    return model


