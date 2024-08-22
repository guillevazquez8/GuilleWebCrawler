from flask import Blueprint, abort, make_response, jsonify
from server.model import News
import requests
from bs4 import BeautifulSoup
import re


app_web_crawler = Blueprint('guille_web_crawler_v1_0_bp', __name__)


@app_web_crawler.get('/news')
def get_first_30_news():
    # send request to hacker news and save response in news object
    news = requests.get("https://news.ycombinator.com/news")
    if news.status_code != 200:
        abort(500, "Server Error: There was an issue calling Hacking News server")
    # convert html response in string
    html_str = BeautifulSoup(news.text).text
    html_str.replace(" ", " ")
    # build regular expression to take number, title, points, and number of comments, from each entry
    pattern = re.compile(r'(\d+)\.\s(.+?)\s\(([^)]+)\)\s(?:(\d+)\spoints).*?(\d+[\sNBSP]+comments?)', re.DOTALL)
    matches = pattern.findall(html_str)
    for match in matches:
        number, title, source, points, comments = match
        data = {
            'number': int(match[0]),
            'title': match[1],
            'points': int(points) if points else 0,
            'number_of_comments': int(comments) if comments else 0
        }
        new = News(data)
        new.save()
    return matches


@app_web_crawler.get("/all_news")
def get_all_news():
    all_news = News.get_all()
    all_news_json = [new.to_dict() for new in all_news]
    return make_response(jsonify(all_news_json))
