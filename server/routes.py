from flask import Blueprint, abort, make_response, jsonify
from server.model import News
from server.init_db import init_db


app_web_crawler = Blueprint('guille_web_crawler_v1_0_bp', __name__)


@app_web_crawler.get("/news")
def get_all_news():
    all_news = News.get_all()
    all_news_json = [new.to_dict() for new in all_news]
    return make_response(all_news_json)

@app_web_crawler.get("/refresh")
def refresh_first_30_news():
    News.delete_all()
    entries = init_db()
    return make_response(entries)
