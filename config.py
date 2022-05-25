import os

class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.get_env('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    