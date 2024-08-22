from flask import Flask
from flask_restx import Api
from server.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    Migrate(app, db)
    api = Api(app,
              title="Guille Web Crawler",
              version="1.0",
              description="Welcome to the best web crawler")

    # blueprints registering
    with app.app_context():
        db.create_all()

    return app
