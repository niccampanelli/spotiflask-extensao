from ..extensions import db
from . import relations

class Playlist(db.Model):
    __tablename__ = "playlist"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    musicas = db.relationship("Musica", secondary=relations.playlist_musicas)

    def __repr__(self):
        return '<Playlist %r>' % self.nome