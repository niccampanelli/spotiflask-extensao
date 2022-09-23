from flask import Flask, render_template, redirect, url_for, session, request

from .services.playlist_service import obter_playlists
from .models.usuario import Usuario
from .extensions import db, migrate
from .routes.usuario_bp import usuario_bp
from .routes.musica_bp import musica_bp
from .routes.playlist_bp import playlist_bp
from .routes.auth_bp import auth_bp
from .services.musica_service import obter_generos, obter_musicas
from .services.usuario_service import obter_artistas

def create_app():
    app = Flask(__name__)

    app.secret_key = 'chave_teste'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotiflask.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(usuario_bp)
    app.register_blueprint(musica_bp)
    app.register_blueprint(playlist_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def inicio():
        playlists_recentes = obter_playlists(incluir_albuns=True)
        return render_template('principal/inicio.html', playlists_recentes=playlists_recentes)

    @app.route('/adicionar_musica')
    def adicionar_musica():
        lista_artistas = obter_artistas()
        lista_generos = obter_generos()
        return render_template('principal/inicio.html', adicionar_musica=True, lista_artistas=lista_artistas, lista_generos=lista_generos)

    return app
