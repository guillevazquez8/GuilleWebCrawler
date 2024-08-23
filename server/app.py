from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from server.routes import AllNews, Refresh, MoreFiveWords, LessFiveWords
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
              title="Guille's Web Crawler",
              version="1.0",
              description="Interact with the best News Crawler!")
    # namespaces registering
    api.add_resource(AllNews, "/news")
    api.add_resource(Refresh, "/refresh")
    api.add_resource(MoreFiveWords, "/title_more_5_words")
    api.add_resource(LessFiveWords, "/title_less_5_words")

    with app.app_context():
        db.drop_all()
        db.create_all()
        # initialize db with 30 first news every time the app is executed
        init_db()

    return app
