"""Root constant define."""
import os

from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.getenv("APP_HOST")
APP_PORT = os.getenv("APP_PORT")

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 43200

ADMIN_USER = -1
SUPER_USERNAME = os.getenv('SUPER_USERNAME')
SUPER_PASSWORD = os.getenv('SUPER_PASSWORD')
