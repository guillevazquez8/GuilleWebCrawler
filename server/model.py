from server.db import db, BaseModelMixin
from sqlalchemy import Column, String, Integer, DateTime


class News(db.Model, BaseModelMixin):
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)
    title = Column(String, nullable=False)
    points = Column(Integer)
    number_of_comments = Column(Integer)

    def __init__(self, data):
        self.number = data['number']
        self.title = data['title']
        self.points = data['points']
        self.number_of_comments = data['number_of_comments']

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "number": self.number,
            "title": self.title,
            "points": self.points,
            "number_of_comments": self.number_of_comments
        }


class History(db.Model, BaseModelMixin):
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    endpoint = Column(String, nullable=False)

    def __init__(self, data):
        self.timestamp = data['timestamp']
        self.endpoint = data['endpoint']

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "endpoint": self.endpoint
        }
