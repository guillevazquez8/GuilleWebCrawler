from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from server.routes import app_web_crawler
from server.db import db

app = Flask(__name__)
app.config.from_pyfile('config/config.py')
db.init_app(app)
Migrate(app, db)
api = Api(app,
          title="Guille Web Crawler",
          version="1.0",
          description="Welcome to the best web crawler")

# blueprints registering
app.register_blueprint(app_web_crawler)

with app.app_context():
    db.create_all()
