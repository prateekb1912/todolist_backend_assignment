import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

class Config:
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'very-secret-key')

