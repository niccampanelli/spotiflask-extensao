from flask import Flask, render_template, redirect, url_for, session, request
from .scripts import metodos

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def inicio():
        return render_template('inicio.html'), 200

    @app.route('/login')
    def login():
        return render_template('login.html'), 200

    @app.route('/cadastro')
    def cadastro():
        return render_template('cadastro.html'), 200

    @app.route('/realizar-cadastro', methods=['POST'])
    def realizar_cadastro():
        nome = request.form['nome'].lower()
        email = request.form['email'].lower()
        senha = request.form['senha']
        confirma_senha = request.form['confirma_senha']

        if confirma_senha == senha:
            metodos.criar_usuario(nome, email, senha, 0)
        
        return "Sucesso", 200

    return app
