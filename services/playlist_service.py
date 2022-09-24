import time

from ..services.musica_service import excluir_musica
from ..models.usuario import Usuario
from ..models.playlist import Playlist
from ..extensions import db

def detalhes_playlist(id_playlist):
    playlist = Playlist.query.get(id_playlist)
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

def editar_playlist(id_playlist, nome):
    playlist: Playlist = Playlist.query.get(id_playlist)
    playlist.nome = nome
    db.session.commit()

def excluir_playlist(id_playlist):
    playlist: Playlist = Playlist.query.get(id_playlist)
    if playlist:
        if(playlist.album == 1):
            for m in playlist.musicas:
                excluir_musica(m.id, id_playlist)
        playlist.musicas.clear()
        playlist.bibliotecas.clear()
        db.session.delete(playlist)
        db.session.commit()

def albuns_artistas(id_artista):
    usuario = Usuario.query.with_entities(Usuario.id, Usuario.tipo).filter(Usuario.id == id_artista).first()
    if usuario.tipo == 1:
        albuns = Playlist.query.with_entities(Playlist.id, Playlist.nome, Playlist.proprietario_id).filter(Playlist.proprietario_id == id_artista, Playlist.album == 1).all()
        resultado = [tuple(a) for a in albuns]
        return resultado
    return []