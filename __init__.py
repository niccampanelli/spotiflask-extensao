from flask import Flask, render_template, redirect, url_for, session, request
from .models.usuario import Usuario
from .extensions import db, migrate
from .routes.usuario_bp import usuario_bp
from .routes.musica_bp import musica_bp
from .routes.auth_bp import auth_bp
from .services.musica_service import obter_generos
from .services.playlist_service import obter_albuns
from .services.usuario_service import obter_artistas

def create_app():
    app = Flask(__name__)

    app.secret_key = 'chave_teste'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotiflask.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(usuario_bp)
    app.register_blueprint(musica_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def inicio():
        return render_template('principal/inicio.html')

    @app.route('/adicionar_musica/<artista>')
    def adicionar_musica_artistas(artista):
        lista_artistas = obter_artistas()
        lista_generos = obter_generos()
        lista_albuns = obter_albuns(artista)
        return render_template('principal/inicio.html', adicionar_musica=True, lista_artistas=lista_artistas, lista_generos=lista_generos, lista_albuns=lista_albuns)

    return app
