# Add any model classes for Flask-SQLAlchemy here
from datetime import datetime
from . import db

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"<Movie {self.id}: {self.title}>"

    # def __init__(self, title, description, poster,created_at):
    #     self.title = title
    #     self.description = description
    #     self.poster = poster
    #     self.created_at = created_at
        