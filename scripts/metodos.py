import string
import bcrypt
from . import database

def criptografar_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

def criar_usuario(nome, email, senha, tipo):
    with database.obter_conexao() as conn:
        usuario = database.Usuario(nome=nome, email=email, senha=criptografar_senha(senha), tipo=tipo)
        conn.add(usuario)
        conn.commit()
