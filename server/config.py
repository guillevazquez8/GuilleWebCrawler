import os


basedir = os.path.abspath(os.path.dirname(__file__))
db = "postgresql://guille:celta@localhost:5432/guille_web_crawler"

class Config:
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = db
    SQLALCHEMY_TRACK_MODIFICATIONS = False
