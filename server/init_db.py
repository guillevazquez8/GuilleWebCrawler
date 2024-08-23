from flask import abort
from server.model import News
import requests
from bs4 import BeautifulSoup
import re


def init_db():
    # send request to hacker news and save response in news object
    news = requests.get("https://news.ycombinator.com/news")
    if news.status_code != 200:
        abort(500, "Server Error: There was an issue calling Hacking News server")
    # convert html response in string
    html_str = BeautifulSoup(news.text, 'html.parser').text
    # separate html string in lines
    lines = html_str.split('\n')
    entries = []
    # iterate over all lines to fuse each entry in 1 line, as they are separated in 2
    for i in range(len(lines) - 1):
        current_line = lines[i].strip()
        next_line = lines[i + 1].strip()
        # Check if current line starts with a number (i.e., entry line), if it does, fuse with next line
        if re.match(r'^\d+\.', current_line):
            combined_entry = f"{current_line} {next_line}"
            entries.append(combined_entry)
    # iterate over entries and find each number, title, points, and number of comments, through regex
    for entry in entries:
        number_match = re.match(r'^\d+', entry)
        title_match = re.search(r'^(?:\d+\.\s)(.*?)(?:\s\([^)]+\.[^)]+\))?(?=\s\d+ points|$)', entry)
        points_match = re.search(r'(\d+) points', entry)
        comments_match = re.search(r'(\d+)\scomments', entry)
        # assign values to data, some entries dont have points and/or comments, in case they don't assign value 0
        data = {
            'number': int(number_match.group()),
            'title': title_match.group(1).strip(),
            'points': int(points_match.group(1)) if points_match else 0,
            'number_of_comments': int(comments_match.group(1)) if comments_match else 0
        }
        new = News(data)
        new.save()
    return entries
