import os 
import secrets
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = secrets.token_hex(16) 
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'expenses.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False