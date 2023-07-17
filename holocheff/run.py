from utils import data_utils
import pandas as pd
import datetime

# Preprocess the data using the format_data function
preprocessed_data = data_utils.get_dataframe()
preprocessed_data = data_utils.format_data(preprocessed_data)

if preprocessed_data is not None:
    # Encode the datetime feature
    preprocessed_data['day_of_week'] = pd.to_datetime(preprocessed_data['date']).dt.dayofweek

    # Get the current local time
    current_time = datetime.datetime.now()
    current_day_of_week = current_time.weekday()

    # Filter the data based on the current day of the week and select the most recent entry
    filtered_data = preprocessed_data[preprocessed_data['day_of_week'] == current_day_of_week]
    filtered_data = filtered_data.iloc[[-1]]

    # Get the name of the next foods
    foods = filtered_data['foods'].values[0]

    # Print the next foods
    print("Next Foods:")
    for food in foods:
        print(food)
else:
    print("No data found.")
