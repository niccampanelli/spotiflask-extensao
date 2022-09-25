from ..extensions import db
from . import relations

class Biblioteca(db.Model):
    __tablename__ = "biblioteca"

    id = db.Column(db.Integer, primary_key = True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    usuario = db.relationship("Usuario", back_populates="biblioteca")
    playlists = db.relationship("Playlist", secondary=relations.biblioteca_playlists, back_populates="bibliotecas")