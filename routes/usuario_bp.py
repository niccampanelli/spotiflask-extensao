from flask import Blueprint, render_template
from ..extensions import db
from ..models.biblioteca import Biblioteca
from ..models.genero import Genero
from ..models.musica import Musica
from ..models.playlist import Playlist
from ..models.relations import biblioteca_playlists, playlist_musicas, usuario_musicas
from ..models.usuario import Usuario

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuario')

@usuario_bp.route('/cria', methods=['GET'])
def usuario():
    db.create_all()
    return "testeee"

# @usuario_bp.route('/<id>', methods=['GET'])
# def dados_usuario(id: int):
#     u: Usuario = Usuario.query.get_or_404(id)
#     return render_template('principal/usuario.html', u=u), 200