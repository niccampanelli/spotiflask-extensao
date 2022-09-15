from flask import Blueprint

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/')
def usuario():
    return "testeee"