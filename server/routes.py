from flask import Blueprint, abort, make_response, jsonify
from server.model import News


app_web_crawler = Blueprint('guille_web_crawler_v1_0_bp', __name__)


@app_web_crawler.get("/news")
def get_all_news():
    all_news = News.get_all()
    all_news_json = [new.to_dict() for new in all_news]
    return make_response(jsonify(all_news_json))
