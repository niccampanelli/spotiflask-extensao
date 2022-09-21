from flask import Blueprint, session, request, render_template, redirect
from ..services.musica_service import cadastrar_genero, adicionar_album, adicionar_musica

musica_bp = Blueprint('musica_bp', __name__, url_prefix='/musica')

@musica_bp.route('/', methods=['POST'])
def musica():
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
        if (genero != -1) and (album != -1):
            musica = adicionar_musica(nome=nome, duracao=duracao, genero_id=genero, artista_id=artista, album_id=album)
            return f'Id Musica = {musica}'
        return f'Genero = {genero} -> {genero != -1} - Album {album != -1}'
    return render_template('/principal/inicio.html'), 403
