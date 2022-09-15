from ..extensions import db
from . import relations

class Genero(db.Model):
    __tablename__ = "genero"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

    def __repr__(self):
        return '<Genero %r>' % self.nome