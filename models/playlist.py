from ..extensions import db
from . import relations

class Playlist(db.Model):
    __tablename__ = "playlist"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    album = db.Column(db.Integer)
    musicas = db.relationship("Musica", secondary=relations.playlist_musicas)
    proprietario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    proprietario = db.relationship("Usuario")
    bibliotecas = db.relationship("Biblioteca", secondary=relations.biblioteca_playlists)

    def __repr__(self):
        return '<Playlist %r>' % self.nome