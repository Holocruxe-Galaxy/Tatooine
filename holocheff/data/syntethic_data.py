from pymongo import MongoClient
import random
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db_name = 'holocheff_db_test'
db = client[db_name]
users_collection = db["users"]
meals_collection = db["meals"]
foods_collection = db["foods"]

# Insert John's user document
user = {
    "email": "john@mail.com",
    "name": "John",
}
user_id = users_collection.insert_one(user).inserted_id

# Foods
foods = [
    {
        "name": "Scrambled Egg Toast",
        "type": "breakfast"
    },
    {
        "name": "Yogurt Parfait",
        "type": "breakfast"
    },
    {
        "name": "Veggie Omelette",
        "type": "breakfast"
    },
    {
        "name": "Smoothie Bowl",
        "type": "breakfast"
    },
    {
        "name": "Pancakes with Maple Syrup",
        "type": "breakfast"
    },
    {
        "name": "Avocado Toast",
        "type": "breakfast"
    },
    {
        "name": "Cereal with Milk",
        "type": "breakfast"
    },
    {
        "name": "Breakfast Burrito",
        "type": "breakfast"
    },
    {
        "name": "French Toast",
        "type": "breakfast"
    },
    {
        "name": "Fruit Salad",
        "type": "breakfast"
    },
    {
        "name": "Chicken Caesar Salad",
        "type": "lunch"
    },
    {
        "name": "Margherita Pizza",
        "type": "lunch"
    },
    {
        "name": "Tuna Salad Sandwich",
        "type": "lunch"
    },
    {
        "name": "Grilled Chicken Wrap",
        "type": "lunch"
    },
    {
        "name": "Caprese Salad",
        "type": "lunch"
    },
    {
        "name": "Mushroom Risotto",
        "type": "lunch"
    },
    {
        "name": "Beef Stir-Fry",
        "type": "lunch"
    },
    {
        "name": "Vegetable Curry",
        "type": "lunch"
    },
    {
        "name": "Pasta Primavera",
        "type": "lunch"
    },
    {
        "name": "Quinoa Salad",
        "type": "lunch"
    },
    {
        "name": "Grilled Salmon with Roasted Vegetables",
        "type": "dinner"
    },
    {
        "name": "Spaghetti Bolognese",
        "type": "dinner"
    },
    {
        "name": "Stir-Fried Beef with Broccoli",
        "type": "dinner"
    },
    {
        "name": "Baked Chicken with Sweet Potato",
        "type": "dinner"
    },
    {
        "name": "Vegetable Lasagna",
        "type": "dinner"
    },
    {
        "name": "Beef Tacos with Salsa and Guacamole",
        "type": "dinner"
    },
    {
        "name": "Lemon Herb Roasted Chicken with Quinoa",
        "type": "dinner"
    },
    {
        "name": "Shrimp Scampi with Garlic Bread",
        "type": "dinner"
    },
    {
        "name": "Vegetarian Stir-Fry with Tofu",
        "type": "dinner"
    },
    {
        "name": "Mushroom and Spinach Stuffed Bell Peppers",
        "type": "dinner"
    }
]

# Insert food documents into the "foods" collection
foods_collection.insert_many(foods)

# Generate meals for John
breakfasts = [food["name"] for food in foods if food["type"] == "breakfast"]
lunches = [food["name"] for food in foods if food["type"] == "lunch"]
dinners = [food["name"] for food in foods if food["type"] == "dinner"]

# for each day this year generate a random meal
start_date = datetime(2022, 1, 1)
for day in range(1, 366):
    current_date = start_date + timedelta(days=day-1)  # Calculate the current date
    breakfast = random.choice(breakfasts)
    lunch = random.choice(lunches)
    dinner = random.choice(dinners)   

    meal = {
        "date": current_date.strftime("%Y-%m-%d"),
        "user_id": user_id,
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner
    }

    meals_collection.insert_one(meal)

print("Data inserted successfully.")
