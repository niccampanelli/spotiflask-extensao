from ..extensions import db
from . import relations

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(255), unique = True)
    senha = db.Column(db.String(512))
    tipo = db.Column(db.Integer)
    biblioteca = db.relationship("Biblioteca", back_populates="usuario")
    musicas = db.relationship("Musica", secondary=relations.usuario_musicas, back_populates="artistas")

    def __repr__(self):
        return '<Usuario %r>' % self.email