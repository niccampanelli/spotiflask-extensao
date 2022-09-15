from ..extensions import db

usuario_musicas = db.Table(
    "usuario_musicas",
    db.metadata,
    db.Column("usuario_id", db.Integer, db.ForeignKey("usuario.id"), primary_key = True),
    db.Column("musica_id", db.Integer, db.ForeignKey("musica.id"), primary_key = True)
)

biblioteca_playlists = db.Table(
    "biblioteca_playlists",
    db.metadata,
    db.Column("biblioteca_id", db.Integer, db.ForeignKey("biblioteca.id"), primary_key = True),
    db.Column("playlist_id", db.Integer, db.ForeignKey("playlist.id"), primary_key = True)
)

playlist_musicas = db.Table(
    "playlist_musicas",
    db.metadata,
    db.Column("playlist_id", db.Integer, db.ForeignKey("playlist.id")),
    db.Column("musica_id", db.Integer, db.ForeignKey("musica.id"))
)