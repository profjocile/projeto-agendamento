import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-apenas-local")
    SQLALCHEMY_DATABASE_URI = "sqlite:///barbearia.db"  # vai para instance/
    SQLALCHEMY_TRACK_MODIFICATIONS = False