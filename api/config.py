from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
