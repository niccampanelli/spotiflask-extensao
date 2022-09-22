from flask import Blueprint, render_template
from ..extensions import db
from ..services.playlist_service import albuns_artistas, playlists_usuario
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

@usuario_bp.route('/<id>', methods=['GET'])
def conta_usuario(id: int):
    u: Usuario = Usuario.query.get_or_404(id)
    playlists = filter(lambda playlist: playlist.album == 0, u.biblioteca[0].playlists)
    if u.tipo == 1:
        albuns = filter(lambda playlist: playlist.album == 1, u.biblioteca[0].playlists)
        return render_template('principal/usuario.html', u=u, playlists=playlists, albuns=albuns), 200
    return render_template('principal/usuario.html', u=u, playlists=playlists), 200

@usuario_bp.route('/desc/<id>', methods=['GET'])
def dados_usuario(id: int):
    u: Usuario = Usuario.query.get_or_404(id)
    return u.__repr__()

@usuario_bp.route('/<id>/playlists', methods=['GET'])
def listar_playlists(id: int):
    playlists = playlists_usuario(id)
    return playlists

@usuario_bp.route('/artista/<id>/albuns', methods=['GET'])
def listar_albuns(id: int):
    playlists = albuns_artistas(id)
    return playlists