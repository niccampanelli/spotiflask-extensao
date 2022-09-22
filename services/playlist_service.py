import time
from ..models.usuario import Usuario
from ..models.playlist import Playlist
from ..extensions import db

def detalhes_playlist(id_playlist):
    playlist = Playlist.query.get(id_playlist)
    for m in playlist.musicas:
        if m.duracao < 3600:
            m.duracao = time.strftime('%M:%S', time.gmtime(m.duracao))
        else:
            m.duracao = time.strftime('%H:%M:%S', time.gmtime(m.duracao))
    return playlist

def obter_playlists(incluir_albuns=False):
    if incluir_albuns:
        playlists = Playlist.query.all()
        return playlists
    playlists = Playlist.query.filter(Playlist.album == 0).all()
    return playlists

def playlists_usuario(id_usuario):
    playlists = Playlist.query.with_entities(Playlist.id, Playlist.nome, Playlist.proprietario_id, Playlist.album).filter(Playlist.proprietario_id == id_usuario, Playlist.album == 0).all()
    resultado = [tuple(p) for p in playlists]
    return resultado

def albuns_artistas(id_artista):
    usuario = Usuario.query.with_entities(Usuario.id, Usuario.tipo).filter(Usuario.id == id_artista).first()
    if usuario.tipo == 1:
        albuns = Playlist.query.with_entities(Playlist.id, Playlist.nome, Playlist.proprietario_id).filter(Playlist.proprietario_id == id_artista, Playlist.album == 1).all()
        resultado = [tuple(a) for a in albuns]
        return resultado
    return []