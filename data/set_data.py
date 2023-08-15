from datetime import datetime, timedelta
import random
import pymongo

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://fierrof47:qR4didvGr1qWJ9YK@testcluster.m7ynzx9.mongodb.net/")
db = client["holocheff_db"]

# MongoDB collections
holocheff_data_collection = client["holocheff_db"]["data"]

start_date = datetime(2022, 1, 1)

meal_list = [f'{meal_type}{n}' for meal_type in ['breakfast', 'lunch', 'dinner', 'snack'] for n in range(1, 100)]
weather_list = ['sunny', 'cloudy', 'rainy', 'snowy']
location_list = ['home', 'restaurant', 'work']

meals = [{
    'date': start_date + timedelta(days=i, hours=random.randint(1,24), minutes=random.randint(0,59)),
    'food': random.choice(meal_list),
    'weather': random.choice(weather_list),
    'location': random.choice(location_list),
} for i in range(1, 365*4)]  # 365 days times 4 meals per day

data = {
    '_id': '00000000',
    'meals': meals,  
    'output': {
        'predicted_meal': 'predicted_meal',
    },
    'model': 'model_name_or_id'
}

holocheff_data_collection.insert_one(data)

print('Data inserted successfully')
