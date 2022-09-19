import string
import bcrypt
from ..models.usuario import Usuario
from ..models.genero import Genero
from ..models.musica import Musica
from ..models.playlist import Playlist
from ..extensions import db

def cadastrar_genero(nome):
    g: Genero = Genero.query.filter_by(nome=nome).first()
    if not g:
        genero = Genero(nome=nome)
        db.session.add(genero)
        db.session.commit()
        return genero.id
    else:
        return -1

def obter_generos():
    generos = Genero.query.all()
    return generos

def adicionar_album(nome, artista):
    album = Playlist(nome=nome, album=1, proprietario_id=artista)
    db.session.add(album)
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
