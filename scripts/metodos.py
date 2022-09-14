from scripts import database

def criptografar_senha(senha):
    return 

def criar_usuario(nome, email, senha, tipo):
    with database.obter_conexao() as conn:
        usuario = database.Usuario(nome=nome, email=email, senha=senha, tipo)
