import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    X_AUTH_SECRET = os.getenv('X_AUTH_SECRET')
    AUTHORIZATION_TOKEN = os.getenv('AUTHORIZATION_TOKEN')

    @classmethod
    def validate(cls):
        """Ensure that required environment variables are set."""
        if not cls.X_AUTH_SECRET or not cls.AUTHORIZATION_TOKEN:
            raise ValueError("Missing X_AUTH_SECRET or AUTHORIZATION_TOKEN in environment variables")
