from ..models.usuario import Usuario
from ..extensions import db

def obter_artistas():
    artistas = Usuario.query.filter(Usuario.tipo == 1).all()
    return artistas