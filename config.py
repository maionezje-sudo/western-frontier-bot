import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')

# Redis (PythonAnywhere has Redis)
REDIS_URL = os.getenv('REDIS_URL', '')

# Game settings
STARTING_MONEY = 100
STARTING_HEALTH = 100
MAX_HEALTH = 100

# Locations
LOCATIONS = [
    'deadwood', 'tombstone', 'dodge', 'abilene', 'tulsa', 'el_paso'
]

# Items
WEAPONS = {
    'revolver': {'price': 50, 'damage': 10},
    'rifle': {'price': 150, 'damage': 25},
    'shotgun': {'price': 300, 'damage': 40}
}

HORSES = {
    'mustang': {'price': 100, 'speed': 1.2},
    'appaloosa': {'price': 250, 'speed': 1.5},
    'arabian': {'price': 500, 'speed': 2.0}
}