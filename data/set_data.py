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

data = []
# insert data in holochef_data collection
def insert_meals(type_list):
    # create a switch to insert time of the day (breakfast, lunch, dinner, snack)
    time_h = 0
    time_m = random.randint(0, 59)
    food = ''
    match type_list:
        case 'breakfasts':
                time_h = random.randint(6, 10)
                food = random.choice(breakfast_list)
        case 'lunches':
                time_h = random.randint(11, 14)
                food = random.choice(lunch_list)
        case 'dinners':
                time_h = random.randint(18, 22)
                food = random.choice(dinner_list)
        case 'snacks':
                time_h = random.randint(15, 17)
                food = random.choice(snack_list)
                
    meal_data = {
        'date': start_date + timedelta(days=i, hours=time_h, minutes=time_m),
        'food': food,
        'weather': random.choice(weather_list),
        'location': random.choice(location_list),
    }
    return meal_data

for i in range(1, 365):
        data.append({
               'user_id': '00000000',
               'meal': insert_meals('breakfasts'),
               'output': {
                    'predicted_meal': 'predicted_meal',
               }
            })      

holocheff_data_collection.insert_many(data)
