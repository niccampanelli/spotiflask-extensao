from ..services.musica_service import excluir_musica
from ..models.biblioteca import Biblioteca
from ..models.usuario import Usuario
from ..models.musica import Musica
from ..models.playlist import Playlist
from ..extensions import db

def adicionar_playlist(nome, usuario_id):
    playlist = Playlist(nome=nome, album=0, proprietario_id=usuario_id)
    biblioteca = Biblioteca.query.filter(Biblioteca.usuario_id == usuario_id).first()
    biblioteca.playlists.append(playlist)
    db.session.add(playlist)
    db.session.add(biblioteca)
    db.session.commit()
    return playlist.id

def detalhes_playlist(id_playlist):
    playlist = Playlist.query.get(id_playlist)
    return playlist

def obter_playlists(incluir_albuns=False, usuario_id=0):
    if usuario_id != 0:
        if incluir_albuns:
            playlists = Playlist.query.filter(Playlist.proprietario_id == usuario_id).all()
            return playlists
        playlists = Playlist.query.filter(Playlist.proprietario_id == usuario_id, Playlist.album == 0).all()
        return playlists
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

def adicionar_musica(id_playlist, id_musica):
    playlist: Playlist = Playlist.query.get(id_playlist)
    musica: Musica = Musica.query.get(id_musica)
    if playlist and musica:
        if playlist.album != 1:
            musica.playlists.append(playlist)
            playlist.musicas.append(musica)
            db.session.commit()

def remover_musica(id_playlist, id_musica):
    playlist: Playlist = Playlist.query.get(id_playlist)
    musica: Musica = Musica.query.get(id_musica)
    if playlist and musica:
        if playlist.album != 1:
            playlist.musicas.remove(musica)
            db.session.commit()