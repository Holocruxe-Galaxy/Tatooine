import data_utils
import tensorflow as tf

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

# entrenar el modelo trayendo el dataframe.csv
def train_model():
    pass
# guardar el modelo en un archivo .h5
def save_model():
    pass
# # crear checkpoint para el modelo



