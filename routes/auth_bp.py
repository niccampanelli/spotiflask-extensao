from flask import Blueprint, request, render_template, redirect, session
from ..services.auth_service import realizar_login, realizar_cadastro

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if not session.get('logado'):
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            logado = realizar_login(email, senha)
            if not logado == -1:
                session['logado'] = True
                session['logado_id'] = logado
                return redirect('/')
            return render_template('auth/login.html'), 400
        return render_template('auth/login.html'), 200
    return redirect('/')

@auth_bp.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if not session.get('logado'):
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            confirma_senha = request.form['confirma_senha']
            tipo = 0
            if senha == confirma_senha:
                id = realizar_cadastro(nome, email, senha, tipo)
                session['logado'] = True
                session['logado_id'] = id
                return redirect('/')
            return render_template('auth/cadastro.html'), 400
        return render_template('auth/cadastro.html'), 200
    return redirect('/')

@auth_bp.route('/sair', methods=['GET'])
def sair():
    session['logado'] = False
    session.pop('logado_id')
    return redirect('/')