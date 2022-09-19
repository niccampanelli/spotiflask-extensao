from ..models.usuario import Usuario
from ..extensions import db

def obter_artistas():
    artistas = Usuario.query.all()
    return artistas