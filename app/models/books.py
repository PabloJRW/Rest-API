from flask_sqlalchemy import SQLAlchemy
from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    isbn = db.Column(db.String, unique=True)
    published = db.Column(db.Integer)


    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'published': self.published
        }
    
