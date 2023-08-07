from faker import Faker
from datetime import datetime, timedelta
import random
import pymongo

# Create an instance of the Faker class
fake = Faker()

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://fierrof47:qR4didvGr1qWJ9YK@testcluster.m7ynzx9.mongodb.net/")
db = client["holocheff_db"]

# MongoDB collections
holocheff_data_collection = db["data"]

start_date = datetime(2022, 1, 1)

breakfast_list = [f'breakfast{n}' for n in range(1, 100)]
lunch_list = [f'lunch{n}' for n in range(1, 100)]
dinner_list = [f'dinner{n}' for n in range(1, 100)]
snack_list = [f'snack{n}' for n in range(1, 100)]

weather_list = ['sunny', 'cloudy', 'rainy', 'snowy']
location_list = ['home', 'restaurant', 'work']

meals = []
for i in range(1, 365):  
    meals.append({
        'date': start_date + timedelta(days=i, hours=random.randint(6,11), minutes=random.randint(0,59)),
        'food': random.choice(breakfast_list),
        'weather': random.choice(weather_list),
        'location': random.choice(location_list),
    })
    meals.append({
        'date': start_date + timedelta(days=i, hours=random.randint(12,14), minutes=random.randint(0,59)),
        'food': random.choice(lunch_list),
        'weather': random.choice(weather_list),
        'location': random.choice(location_list),
    })
    meals.append({
        'date': start_date + timedelta(days=i, hours=random.randint(18,22), minutes=random.randint(0,59)),
        'food': random.choice(dinner_list),
        'weather': random.choice(weather_list),
        'location': random.choice(location_list),
    })
    meals.append({
        'date': start_date + timedelta(days=i, hours=random.randint(6,24), minutes=random.randint(0,59)),
        'food': random.choice(snack_list),
        'weather': random.choice(weather_list),
        'location': random.choice(location_list),
    })

data = {
    'user_id': '00000000',
    'meals': meals,  
    'output': {
        'predicted_meal': 'predicted_meal',
    },
    'model': 'model_name_or_id'
}

holocheff_data_collection.insert_one(data)

print('Data inserted successfully')
