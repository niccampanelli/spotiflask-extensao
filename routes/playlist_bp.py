from flask import Blueprint, session, request, render_template, redirect

from ..services.musica_service import detalhes_musica, editar_musica, excluir_musica, obter_generos
from ..services.playlist_service import adicionar_musica, adicionar_playlist, detalhes_playlist, editar_playlist, excluir_playlist, obter_playlists, remover_musica

playlist_bp = Blueprint('playlist_bp', __name__, url_prefix='/playlist')

@playlist_bp.route('/<id>', methods=['GET'])
def dados_playlist(id):
    playlist = detalhes_playlist(id)
    lista_playlist = obter_playlists(incluir_albuns=False, usuario_id=session['logado_id'])
    return render_template('/principal/playlist.html', p=playlist, lista_playlist=lista_playlist)

@playlist_bp.route('/criar', methods=['GET'])
def criar_nova_playlist():
    if session['logado']:
        id = adicionar_playlist('Nova playlist', session['logado_id'])
        return redirect(f'/playlist/{id}')
    else:
        return redirect('/') 

@playlist_bp.route('/<id>/editar', methods=['GET', 'POST'])
def editar_dado_playlist(id):
    playlist = detalhes_playlist(id)
    lista_playlist = obter_playlists(incluir_albuns=False, usuario_id=session['logado_id'])
    if request.method == 'GET':
        if session['logado_id'] == playlist.proprietario_id:
            return render_template('/principal/playlist.html', p=playlist, lista_playlist=lista_playlist, editando=True)
        return redirect(f'/playlist/{id}')
    elif request.method == 'POST':
        if session['logado_id'] == playlist.proprietario_id:
            cor = request.form.get('cor', '')
            nome = request.form.get('nome', '')
            editar_playlist(id, cor, nome)
            return redirect(f'/playlist/{id}')
        else:
            return redirect('/') 

@playlist_bp.route('/<id>/excluir', methods=['GET', 'POST'])
def deletar_playlist(id):
    playlist = detalhes_playlist(id)
    lista_playlist = obter_playlists(incluir_albuns=False, usuario_id=session['logado_id'])
    if request.method == 'GET':
        if session['logado_id'] == playlist.proprietario_id:
            return render_template('/principal/playlist.html', p=playlist, lista_playlist=lista_playlist, excluindo=True)
        return redirect(f'/playlist/{id}')
    elif request.method == 'POST':
        if session['logado_id'] == playlist.proprietario_id:
            nome = request.form.get('nome', '')
            if nome == playlist.nome:
                excluir_playlist(id)
                return redirect('/')
            return redirect(f'/playlist/{id}/excluir')
        else:
            return redirect('/') 

@playlist_bp.route('/<id_playlist>/musica/<id_musica>/excluir', methods=['GET', 'POST'])
def deletar_musica(id_playlist, id_musica):
    playlist = detalhes_playlist(id_playlist)
    lista_playlist = obter_playlists(incluir_albuns=False, usuario_id=session['logado_id'])
    musica = detalhes_musica(id_musica)
    if request.method == 'GET':
        if playlist.album == 1:
            for a in musica.artistas:
                if session['logado_id'] == a.id:
                    return render_template('/principal/playlist.html', p=playlist, lista_playlist=lista_playlist, musica=musica, excluindoMusica=True)
        remover_musica(id_playlist=id_playlist, id_musica=id_musica)
        return redirect(f'/playlist/{id_playlist}')
    elif request.method == 'POST':
        for a in musica.artistas:
            if session['logado_id'] == a.id:
                nome = request.form.get('nome', '')
                if nome == musica.nome:
                    excluir_musica(id_musica=id_musica, id_playlist=id_playlist)
                    return redirect(f'/playlist/{id_playlist}')
            return redirect('/') 
        else:
            return redirect('/') 

@playlist_bp.route('/<id_playlist>/musica/<id_musica>/editar', methods=['GET', 'POST'])
def editar_dado_musica(id_playlist, id_musica):
    playlist = detalhes_playlist(id_playlist)
    lista_playlist = obter_playlists(incluir_albuns=False, usuario_id=session['logado_id'])
    musica = detalhes_musica(id_musica)
    generos = obter_generos()
    if request.method == 'GET':
        for a in musica.artistas:
            if session['logado_id'] == a.id:
                return render_template('/principal/playlist.html', p=playlist, lista_playlist=lista_playlist, musica=musica, generos=generos, editandoMusica=True)
        return redirect(f'/playlist/{id_playlist}')
    elif request.method == 'POST':
        for a in musica.artistas:
            if session['logado_id'] == a.id:
                nome = request.form.get('nome', '')
                genero = request.form.get('genero', '')
                duracao = request.form.get('duracao', '')
                editar_musica(id_musica=id_musica, nome=nome, genero=genero, duracao=duracao)
                return redirect(f'/playlist/{id_playlist}')
        else:
            return redirect('/') 

@playlist_bp.route('/<id_playlist>/musica/<id_musica>/adicionar', methods=['GET'])
def adicionar_musica_playlist(id_playlist, id_musica):
    if session['logado']:
        adicionar_musica(id_playlist, id_musica)
        return redirect(f'/playlist/{id_playlist}')
    return redirect('/')