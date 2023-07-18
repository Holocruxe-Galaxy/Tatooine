from faker import Faker
from datetime import datetime, timedelta
import pymongo

# Create an instance of the Faker class
fake = Faker()

# Generate synthetic user data
num_users = 1000  # Number of synthetic users to generate

users = []
for _ in range(num_users):
    name = fake.name()
    users.append({"name": name})

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["holocheff_db"]
users_collection = db["users"]

# Insert the synthetic user data into the 'users' collection
result = users_collection.insert_many(users)
print("Users inserted into MongoDB.")

# Generate synthetic meal data
num_data_points = 1000  # Number of synthetic data points to generate

data = []
start_date = datetime(2023, 1, 1)  # Start date for generating dates
for _ in range(num_data_points):
    current_date = start_date.strftime("%Y-%m-%d")
    weather = fake.random_element(elements=("sunny", "rainy", "cloudy"))
    location = fake.random_element(elements=("home", "office", "restaurant"))

    # Generate breakfast, lunch, and dinner meals
    breakfast = fake.random_element(elements=("cereal", "toast", "oatmeal", "pancakes", "smoothie"))
    lunch = fake.random_element(elements=("sandwich", "pizza", "salad", "soup", "steak", "sushi", "pasta"))
    dinner = fake.random_element(elements=("sandwich", "pizza", "salad", "soup", "steak", "sushi", "pasta"))

    data.append({
        "date": current_date,
        "weather": weather,
        "location": location,
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner
    })

    # Increment the date for the next iteration
    start_date += timedelta(days=1)

# MongoDB connection
meals_collection = db["meals"]

# Fetch the inserted user data
inserted_users = list(users_collection.find({}, {"_id": 1}))

# Assign meal data to each user
for i, user in enumerate(inserted_users):
    meal = data[i]
    meal["user_id"] = user["_id"]
    meals_collection.insert_one(meal)
    # print(f"Added meal for user ID: {user['_id']}")

# Print success message
print("Meals inserted into MongoDB.")
