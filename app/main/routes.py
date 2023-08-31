from app.main import main_bp
from flask import request, jsonify
from app.models.books import Books
from app import db


@main_bp.route('/', methods=['GET'])
def get_books():
    books = Books().query.all()
    list_of_books = [book.serialize() for book in books]
    return jsonify({'books':list_of_books})


@main_bp.route('/add-book', methods=['POST'])
def post_book():
    data = request.get_json()
    new_book = Books(title=data['title'], 
                    author=data['author'], 
                    isbn=data['isbn'],
                    published=data['published'])
    db.session.add(new_book)
    db.session.commit()

    return jsonify({'message':"Libro Añadido!!!."}), 201


@main_bp.route('/by-title/<string:title>', methods=['GET'])
def get_books_by_title(title):
    books = Books().query.filter_by(title=title).all()
    if not books:
        return jsonify({"message": "Título no encontrado."}), 404
    
    list_of_books = [book.serialize() for book in books]
    
    return jsonify({'books':list_of_books}), 200
    

@main_bp.route('/by-author/<string:author>', methods=['GET'])
def get_books_by_author(author):
    books = Books().query.filter_by(author=author).all()
    if not books:
        return jsonify({"message": "Autor no encontrado."}), 404
    
    list_of_books = [book.serialize() for book in books]

    return jsonify({'books':list_of_books}), 200


@main_bp.route('/edit/<int:id>', methods=['PUT'])
def edit_book(id):
    book = Books().query.filter_by(id=id).first()
    if not book:
        return jsonify({"message": f"Libro con el id {id} no fue encontrado."}), 404
    
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    book.isbn = data['isbn']
    book.published = data['published']
    
    db.session.commit()

    return jsonify({'message':"Libro editado correctamente!!!."})


@main_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Books().query.filter_by(id=id).first()
    if not book:
        return jsonify({"message": "ID no encontrado."}), 404
    
    db.session.delete(book)
    db.session.commit()

    return jsonify({'message': f"Libro {book.title} eliminado correctamente"})