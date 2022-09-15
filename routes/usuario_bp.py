from crypt import methods
from flask import Blueprint

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuario')

@usuario_bp.route('/', methods=['POST'])
def usuario():
    return "testeee"