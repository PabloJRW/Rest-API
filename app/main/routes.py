from app.main import main_bp
from flask import request, jsonify
from app.models.books import Book
from app import db


@main_bp.route('/', methods=['GET'])
def get_books():
    books = Book().query.all()
    list_of_books = [book.serialize() for book in books]
    return jsonify({'books':list_of_books})


@main_bp.route('/add-book', methods=['POST'])
def post_book():
    data = request.get_json()
    new_book = Book(title=data['title'], 
                    author=data['author'], 
                    isbn=data['isbn'],
                    published=data['published'])
    db.session.add(new_book)
    db.session.commit()

    return "Añadido!!!."