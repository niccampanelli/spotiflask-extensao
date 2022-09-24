import string
import bcrypt
from ..models.biblioteca import Biblioteca
from ..models.usuario import Usuario
from ..models.genero import Genero
from ..models.musica import Musica
from ..models.playlist import Playlist
from ..extensions import db

def detalhes_musica(id):
    musica = Musica.query.get(id)
    return musica

def obter_musicas():
    musicas = Musica.query.all()
    return musicas

def cadastrar_genero(nome):
    g: Genero = Genero.query.filter_by(nome=nome).first()
    if not g:
        genero = Genero(nome=nome)
        db.session.add(genero)
        db.session.commit()
        return genero.id
    else:
        return g.id

def obter_generos():
    generos = Genero.query.all()
    return generos

def adicionar_album(nome, artista):
    album = Playlist(nome=nome, album=1, proprietario_id=artista)
    biblioteca = Biblioteca.query.filter(Biblioteca.usuario_id == artista).first()
    biblioteca.playlists.append(album)
    db.session.add(album)
    db.session.add(biblioteca)
    db.session.commit()
    return album.id

def adicionar_musica(nome, duracao, genero_id, artista_id, album_id):
    g: Genero = Genero.query.get(genero_id)
    a: Usuario = Usuario.query.get(artista_id)
    album: Playlist = Playlist.query.get(album_id)
    if g and a and album:
        musica = Musica(nome=nome, duracao=duracao, genero_id=genero_id)
        musica.artistas.append(a)
        album.musicas.append(musica)
        db.session.add(musica)
        db.session.commit()
        return musica.id
    else:
        return -1

def excluir_musica(id_musica, id_playlist):
    musica: Musica = Musica.query.get(id_musica)
    playlist: Playlist = Playlist.query.get(id_playlist)
    if musica and playlist:
        playlist.musicas.remove(musica)
        for a in musica.artistas:
            a.musicas.remove(musica)
        db.session.delete(musica)
        db.session.commit()

def editar_musica(id_musica, nome, genero, duracao):
    musica: Musica = Musica.query.get(id_musica)
    g: Genero = Genero.query.get(genero)
    if g:
        musica.nome = nome
        musica.genero_id = genero
        musica.duracao = duracao
        db.session.commit()