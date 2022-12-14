from flask import Blueprint, session, request, render_template, redirect
from ..services.musica_service import cadastrar_genero, adicionar_album, adicionar_musica, detalhes_musica, obter_musicas

musica_bp = Blueprint('musica_bp', __name__, url_prefix='/musica')

@musica_bp.route('/', methods=['POST', 'GET'])
def musica():
    if request.method == 'POST':
        if session['logado']:
            nome = request.form['nome']
            artista = request.form['artista']
            album = request.form['album']
            genero = request.form['genero']
            duracao = request.form['duracao']

            if not genero.isdigit():
                genero = cadastrar_genero(genero)
            if not album.isdigit():
                album = adicionar_album(album, artista=artista)

            musica = adicionar_musica(nome=nome, duracao=duracao, genero_id=genero, artista_id=artista, album_id=album)
            return redirect(f'/playlist/{album}')
        return redirect('/')
    return obter_musicas()
