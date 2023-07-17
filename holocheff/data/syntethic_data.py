from faker import Faker
from datetime import datetime, timedelta
import pymongo

# Create an instance of the Faker class
fake = Faker()

# Generate synthetic data
num_data_points = 1000  # Number of synthetic data points to generate

data = []
start_date = datetime(2023, 1, 1)  # Start date for generating dates
for _ in range(num_data_points):
    current_date = start_date.strftime("%Y-%m-%d")
    weather = fake.random_element(elements=("sunny", "rainy", "cloudy"))
    location = fake.random_element(elements=("home", "office", "restaurant"))

    # Generate breakfast, lunch, and dinner
    breakfast = fake.random_element(elements=("cereal", "toast", "oatmeal", "pancakes", "smoothie"))
    lunch = fake.random_element(elements=("sandwich", "pizza", "salad"))
    dinner = fake.random_element(elements=("soup", "steak", "sushi", "pasta"))

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
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["holocheff_db"]
collection = db["meals"]

# Insert the synthetic data into the MongoDB collection
collection.insert_many(data)

# Print success message
print("Data inserted into MongoDB.")
