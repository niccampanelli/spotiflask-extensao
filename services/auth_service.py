import string
import bcrypt
from ..models.usuario import Usuario
from ..models.biblioteca import Biblioteca
from ..extensions import db

def criptografar_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

def realizar_login(email, senha: string):
    u: Usuario = Usuario.query.filter_by(email=email).first()
    if u:
        if bcrypt.checkpw(senha.encode('utf-8'), u.senha):
            return [u.id, u.nome]
        else:
            return -1
    else:
        return -1

def realizar_cadastro(nome, email, senha, tipo):
    u: Usuario = Usuario.query.filter_by(email=email).first()
    if not u:
        usuario = Usuario(nome=nome, email=email, senha=criptografar_senha(senha), tipo=tipo)
        db.session.add(usuario)
        db.session.commit()
        biblioteca = Biblioteca(usuario_id=usuario.id)
        biblioteca.usuario = usuario
        db.session.add(biblioteca)
        db.session.commit()
        return [usuario.id, usuario.nome]
    else:
        return -1