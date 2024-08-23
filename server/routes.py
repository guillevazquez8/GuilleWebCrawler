from flask import abort, make_response
from server.model import News
from server.init_db import init_db
from sqlalchemy import desc
from flask_restx import Resource, Namespace


api_ns = Namespace('guille_web_crawler_v1_0_bp',
                   description="Interact with the best News Crawler!")


class AllNews(Resource):
    def get(self):
        all_news = News.get_all()
        all_news_json = [new.to_dict() for new in all_news]
        return make_response(all_news_json)


class Refresh(Resource):
    def get(self):
        News.delete_all()
        entries = init_db()
        return make_response(entries)


class MoreFiveWords(Resource):
    def get(self):
        all_news_ordered = News.query.order_by(desc(News.number_of_comments)).all()
        news_json = [
            new.to_dict()
            for new in all_news_ordered
            if sum(1 for word in new.title.split() if any(c.isalpha() for c in word)) > 5
        ]
        return make_response(news_json)


class LessFiveWords(Resource):
    def get(self):
        all_news_ordered = News.query.order_by(desc(News.points)).all()
        news_json = [
            new.to_dict()
            for new in all_news_ordered
            if sum(1 for word in new.title.split() if any(c.isalpha() for c in word)) <= 5
        ]
        return make_response(news_json)
