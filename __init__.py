from flask import Flask, render_template, redirect, url_for

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

    return app
