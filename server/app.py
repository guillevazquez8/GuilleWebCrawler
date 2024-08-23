from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from server.routes import app_web_crawler
from server.db import db
from server.init_db import init_db


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config is None:
        app.config.from_pyfile("config/config.py", silent=True)
    else:
        app.config.update(test_config)
    db.init_app(app)
    Migrate(app, db)
    api = Api(app,
              title="Guille Web Crawler",
              version="1.0",
              description="Welcome to the best web crawler")
    # blueprints registering
    app.register_blueprint(app_web_crawler)
    with app.app_context():
        db.drop_all()
        db.create_all()
        # initialize db with 30 first news every time the app is executed
        init_db()
    return app
