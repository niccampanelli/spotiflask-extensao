from flask import Blueprint, session, request, render_template, redirect

from ..services.musica_service import detalhes_musica, excluir_musica
from ..services.playlist_service import detalhes_playlist, editar_playlist, excluir_playlist

playlist_bp = Blueprint('playlist_bp', __name__, url_prefix='/playlist')

@playlist_bp.route('/<id>', methods=['GET'])
def dados_playlist(id):
    playlist = detalhes_playlist(id)
    return render_template('/principal/playlist.html', p=playlist)

@playlist_bp.route('/<id>/editar', methods=['GET', 'POST'])
def editar_dado_playlist(id):
    playlist = detalhes_playlist(id)
    if request.method == 'GET':
        if session['logado_id'] == playlist.proprietario_id:
            return render_template('/principal/playlist.html', p=playlist, editando=True)
        return redirect(f'/playlist/{id}')
    elif request.method == 'POST':
        if session['logado_id'] == playlist.proprietario_id:
            nome = request.form.get('nome', '')
            editar_playlist(id, nome)
            return redirect(f'/playlist/{id}')
        else:
            return redirect('/') 

@playlist_bp.route('/<id>/excluir', methods=['GET', 'POST'])
def deletar_playlist(id):
    playlist = detalhes_playlist(id)
    if request.method == 'GET':
        if session['logado_id'] == playlist.proprietario_id:
            return render_template('/principal/playlist.html', p=playlist, excluindo=True)
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
    musica = detalhes_musica(id_musica)
    if request.method == 'GET':
        for a in musica.artistas:
            if session['logado_id'] == a.id:
                return render_template('/principal/playlist.html', p=playlist, musica=musica, excluindoMusica=True)
        return redirect(f'/playlist/{id_playlist}')
    elif request.method == 'POST':
        for a in musica.artistas:
            if session['logado_id'] == a.id:
                nome = request.form.get('nome', '')
                if nome == musica.nome:
                    excluir_musica(id_musica=id_musica, id_playlist=id_playlist)
                    return redirect(f'/playlist/{id_playlist}')
                return nome + ' = ' + id_musica
        else:
            return redirect('/') 