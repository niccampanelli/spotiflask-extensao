from flask import Blueprint, session, request, render_template, redirect
from ..services.playlist_service import detalhes_playlist

playlist_bp = Blueprint('playlist_bp', __name__, url_prefix='/playlist')

@playlist_bp.route('/<id>', methods=['GET'])
def dados_playlist(id):
    playlist = detalhes_playlist(id)
    return render_template('/principal/playlist.html', p=playlist)
