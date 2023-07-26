from faker import Faker
from datetime import datetime, timedelta
import random
import pymongo

# Create an instance of the Faker class
fake = Faker()

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["holocheff_db"]

# MongoDB collections
users_collection = db["users"]
meals_collection = db["meals"]
foods_collection = db["foods"]

# Number of synthetic data points to generate
num_data_points = 1000

breakfast_list = [{'name': f'breakfast{n}'} for n in range(1, 100)]
lunch_list = [{'name': f'lunch{n}'} for n in range(1, 100)]
dinner_list = [{'name': f'dinner{n}'} for n in range(1, 100)]
snack_list = [{'name': f'snack{n}'} for n in range(1, 500)]

wheather_list = ['sunny', 'cloudy', 'rainy', 'snowy']
location_list = ['home', 'restaurant', 'work']
# Generate synthetic user data
def generate_users(num_users):
    users = []
    for _ in range(num_users):
        name = fake.name()
        users.append({"name": name})
    users_collection.insert_many(users)    
    print("Users inserted into MongoDB.")

# Generate synthetic food data
def generate_foods():
    foods = breakfast_list + \
            lunch_list + \
            dinner_list + \
            snack_list
    foods_collection.insert_many(foods) 
    print("Foods inserted into MongoDB.")

# Generate synthetic meal data
# Generate synthetic meal data
def generate_meals(num_days):
    data = []
    # Get all user ids
    user_ids = [user['_id'] for user in users_collection.find({}, {'_id': 1})]

    start_date = datetime(2023, 1, 1)

    # Get all food items
    breakfast_items = list(foods_collection.find({'name': {'$regex': 'breakfast\d+'}}))
    lunch_items = list(foods_collection.find({'name': {'$regex': 'lunch\d+'}}))
    dinner_items = list(foods_collection.find({'name': {'$regex': 'dinner\d+'}}))
    snack_items = list(foods_collection.find({'name': {'$regex': 'snack\d+'}}))

    # for each user_id in user_ids add it to the data list
    for user_id in user_ids:
        # For each day since the start date and for the number of days
        for day in range(num_days):
            # Generate breakfast data
            breakfast_food = random.choice(breakfast_items)
            data.append({
                'user_id': user_id,
                'date': start_date + timedelta(days=day, hours=random.randint(8, 11)),
                'food_id': breakfast_food['_id'],
                'weather': random.choice(wheather_list),
                'location': random.choice(location_list)
            })

            # Generate lunch data
            lunch_food = random.choice(lunch_items)
            data.append({
                'user_id': user_id,
                'date': start_date + timedelta(days=day, hours=random.randint(12, 15)),
                'food_id': lunch_food['_id'],
                'weather': random.choice(wheather_list),
                'location': random.choice(location_list)
            })

            # Generate dinner data
            dinner_food = random.choice(dinner_items)
            data.append({
                'user_id': user_id,
                'date': start_date + timedelta(days=day, hours=random.randint(18, 22)),
                'food_id': dinner_food['_id'],
                'weather': random.choice(wheather_list),
                'location': random.choice(location_list)
            })

            # Add between 0 and 5 snacks between 8 am and 10 pm
            for _ in range(random.randint(0, 5)):
                snack_food = random.choice(snack_items)
                data.append({
                    'user_id': user_id,
                    'date': start_date + timedelta(days=day, hours=random.randint(8, 22)),
                    'food_id': snack_food['_id'],
                    'weather': random.choice(wheather_list),
                    'location': random.choice(location_list)
                })

    # Bulk insert the data
    meals_collection.insert_many(data)
    print("Meals inserted into MongoDB.")

# The rest of the code remains unchanged

generate_users(num_data_points)
generate_foods()
generate_meals(365)






