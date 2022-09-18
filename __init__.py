from flask import Flask, render_template, redirect, url_for, session, request
from .models.usuario import Usuario
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
        return render_template('principal/inicio.html')

    return app
