from flask import Flask, request
from flask_restx import Api
from flask_migrate import Migrate
from server.routes.news import api_ns
from server.routes.history import history_ns
from server.db import db
from server.init_db import init_db
from server.model import History
import datetime


app = Flask(__name__)
app.config.from_pyfile("config/config.py", silent=True)
db.init_app(app)
Migrate(app, db)
api = Api(app,
          title="Guille's Web Crawler",
          version="1.0",
          description="Interact with the best News Crawler!")
# namespaces registering
api.add_namespace(api_ns)
api.add_namespace(history_ns)

with app.app_context():
    db.drop_all()
    db.create_all()
    # initialize db with 30 first news every time the app is executed
    init_db()


@app.after_request
def after_request(response):
    if request.path in ['/api/title_more_5_words', '/api/title_less_5_words']:
        data = {
            "timestamp": datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
            "endpoint": request.path
        }
        new_history = History(data)
        new_history.save()
    return response
