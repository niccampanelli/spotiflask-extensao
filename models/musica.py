from ..extensions import db
from . import relations

class Musica(db.Model):
    __tablename__ = "musica"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(128))
    artistas = db.relationship("Usuario", secondary=relations.usuario_musicas, back_populates="musicas")
    duracao = db.Column(db.Integer)
    playlists = db.relationship("Playlist", secondary=relations.playlist_musicas, back_populates="musicas")
    genero_id = db.Column(db.Integer, db.ForeignKey("genero.id"))
    genero = db.relationship("Genero")

    def __repr__(self):
        return '<Musica %r>' % self.nome