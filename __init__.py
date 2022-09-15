from flask import Flask, render_template, redirect, url_for, session, request
from .extensions import db, migrate
from .routes.usuario_bp import usuario_bp
from .routes.auth_bp import auth_bp

def create_app():
    app = Flask(__name__)

    app.secret_key = 'chave_teste'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotiflask.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(usuario_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def inicio():
        return render_template('inicio.html'), 200

    # @app.route('/login')
    # def login():
    #     return render_template('login.html'), 200

    # @app.route('/cadastro')
    # def cadastro():
    #     return render_template('cadastro.html'), 200

    # @app.route('/realizar-cadastro', methods=['POST'])
    # def realizar_cadastro():
    #     nome = request.form['nome'].lower()
    #     email = request.form['email'].lower()
    #     senha = request.form['senha']
    #     confirma_senha = request.form['confirma_senha']

    #     if confirma_senha == senha:
    #         metodos.criar_usuario(nome, email, senha, 0)
        
    #     return "Sucesso", 200

    return app
