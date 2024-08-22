from server.app import db
from sqlalchemy import Column, String, Integer


class News(db.Model):
    number = Column(Integer, nullable=False, unique=True)
    title = Column(String, nullable=False)
    points = Column(Integer, nullable=False)
    number_of_comments = Column(Integer, nullable=False)

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
