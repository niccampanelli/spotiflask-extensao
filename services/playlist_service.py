from ..models.playlist import Playlist
from ..extensions import db

def playlists_usuario(id_usuario):
    playlists = Playlist.query.with_entities(Playlist.id, Playlist.nome, Playlist.proprietario_id).filter(Playlist.proprietario_id == id_usuario).all()
    resultado = [tuple(p) for p in playlists]
    return resultado