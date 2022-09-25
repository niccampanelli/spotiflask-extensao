from flask import session
from ..models.playlist import Playlist
from ..services.musica_service import excluir_musica
from ..models.usuario import Usuario
from ..extensions import db

def obter_artistas():
    artistas = Usuario.query.filter(Usuario.tipo == 1).all()
    return artistas

def detalhes_usuario(id):
    usuario = Usuario.query.get(id)
    return usuario

def editar_usuario(id, nome, tipo):
    usuario: Usuario = Usuario.query.get(id)
    usuario.nome = nome
    usuario.tipo = tipo
    db.session.commit()

def excluir_usuario(id_usuario):
    usuario: Usuario = Usuario.query.get(id_usuario)
    if usuario:
        if(usuario.tipo == 1):
            for m in usuario.musicas:
                for p in m.playlists:
                    excluir_musica(m.id, p.id)
        for p in usuario.biblioteca[0].playlists:
            p.musicas.clear()
            db.session.delete(p)
        usuario.biblioteca[0].playlists.clear()
        db.session.delete(usuario.biblioteca[0])
        db.session.delete(usuario)
        db.session.commit()
        session['logado'] = False
        session.pop('logado_id')
        session.pop('logado_nome')