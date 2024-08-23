from flask import abort, make_response
from server.model import News
from server.init_db import init_db
from sqlalchemy import desc
from flask_restx import Resource, Namespace


api_ns = Namespace("api",
                   description="Interact with the best News Crawler!")


@api_ns.route("/news")
class AllNews(Resource):
    @api_ns.doc("Get all news")
    def get(self):
        all_news = News.get_all()
        all_news_json = [new.to_dict() for new in all_news]
        return make_response(all_news_json)


@api_ns.route("/refresh")
class Refresh(Resource):
    @api_ns.doc("Refresh first 30 news")
    def get(self):
        News.delete_all()
        entries = init_db()
        return make_response(entries)


@api_ns.route("/title_more_5_words")
class MoreFiveWords(Resource):
    @api_ns.doc("Filter all news with more than 5 words in their title")
    def get(self):
        all_news_ordered = News.query.order_by(desc(News.number_of_comments)).all()
        news_json = [
            new.to_dict()
            for new in all_news_ordered
            if sum(1 for word in new.title.split() if any(c.isalpha() for c in word)) > 5
        ]
        return make_response(news_json)


@api_ns.route("/title_less_5_words")
class LessFiveWords(Resource):
    @api_ns.doc("Filter all news with less than 5 words in their title")
    def get(self):
        all_news_ordered = News.query.order_by(desc(News.points)).all()
        news_json = [
            new.to_dict()
            for new in all_news_ordered
            if sum(1 for word in new.title.split() if any(c.isalpha() for c in word)) <= 5
        ]
        return make_response(news_json)
