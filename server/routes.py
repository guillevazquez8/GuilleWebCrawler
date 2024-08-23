from flask import Blueprint, abort, make_response, jsonify
from server.model import News
from server.init_db import init_db
from sqlalchemy import func, desc


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


@app_web_crawler.get("/more_5_words")
def get_news_with_more_than_5_words_in_title():
    all_news_ordered = News.query.order_by(desc(News.number_of_comments)).all()
    # improve it to avoid counting symbols
    news = [new for new in all_news_ordered if len(new.title.split()) > 5]
    news_json = [new.to_dict() for new in news]
    return make_response(news_json)

@app_web_crawler.get("/less_5_words")
def get_news_with_lte_5_words_in_title():
    all_news_ordered = News.query.order_by(desc(News.points)).all()
    news = [new for new in all_news_ordered if len(new.title.split()) <= 5]
    news_json = [new.to_dict() for new in news]
    return make_response(news_json)
