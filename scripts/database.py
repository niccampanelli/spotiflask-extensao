from enum import unique
from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

STRING_CONEXAO = 'sqlite://spotiflask.db'

Base = declarative_base()

usuario_musicas = Table(
    "usuario_musicas",
    Base.metadata,
    Column(Integer, ForeignKey("usuario.id"), primary_key = True),
    Column(Integer, ForeignKey("musica.id"), primary_key = True)
)

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key = True)
    nome = Column(String(100))
    email = Column(String(255), unique = True)
    senha = Column(String(512))
    tipo = Column(Integer)
    biblioteca = relationship("Biblioteca", back_populates="usuario")
    musicas = relationship("Musica", secondary=usuario_musicas, back_populates="artistas")

    def __repr__(self):
        return '<Usuario %r>' % self.email

biblioteca_playlists = Table(
    "biblioteca_playlists",
    Base.metadata,
    Column(Integer, ForeignKey("biblioteca.id"), primary_key = True),
    Column(Integer, ForeignKey("playlist.id"), primary_key = True)
)

class Biblioteca(Base):
    __tablename__ = "biblioteca"

    id = Column(Integer, primary_key = True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates="biblioteca")
    playlists = relationship("Playlist", secondary=biblioteca_playlists)

playlist_musicas = Table(
    "playlist_musicas",
    Base.metadata,
    Column(Integer, ForeignKey("playlist.id")),
    Column(Integer, ForeignKey("musica.id"))
)

class Playlist(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key = True)
    nome = Column(String(50))
    musicas = relationship("Musica", secondary=playlist_musicas)

    def __repr__(self):
        return '<Playlist %r>' % self.nome

class Musica(Base):
    __tablename__ = "musica"

    id = Column(Integer, primary_key = True)
    nome = Column(String(128))
    artistas = relationship("Usuario", secondary=usuario_musicas, back_populates="musicas")
    duracao = Integer(Integer)
    genero_id = Column(Integer, ForeignKey("genero.id"))
    genero = relationship("Genero")

    def __repr__(self):
        return '<Musica %r>' % self.nome

class Genero():
    __tablename__ = "genero"

    id = Column(Integer, primary_key = True)
    nome = Column(String(100))

    def __repr__(self):
        return '<Genero %r>' % self.nome

engine = create_engine(STRING_CONEXAO)
Base.metadata.create_all(engine)

def obter_conexao():
    conn = sessionmaker(engine)()
    conn.expire_on_commit = False
    try:
        yield conn
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()
