from ..models.playlist import Playlist
from ..extensions import db

def obter_albuns(id_artista):
    albuns = Playlist.query.filter_by(proprietario_id=id_artista)
    return albuns