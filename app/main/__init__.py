from flask import Blueprint

main_bp = Blueprint('books', __name__, url_prefix='/books')


from . import routes