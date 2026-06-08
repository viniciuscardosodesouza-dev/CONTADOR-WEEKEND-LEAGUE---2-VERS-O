from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Jogador(Base):
    __tablename__ = 'jogadores'

    id = Column(String, primary_key=True)
    nome = Column(String, unique=True, nullable=False)
    gols = Column(Integer, default=0)
    assist = Column(Integer, default=0)

class WL(Base):
    __tablename__ = 'wls'

    id = Column(Integer, primary_key=True)
    partidas = relationship("Partida", back_populates="wl")

class Partida(Base):
    __tablename__ = 'partidas'

    id_partida = Column(Integer, primary_key=True)
    wl_id = Column(Integer, ForeignKey('wls.id'), primary_key=True)
    adversario = Column(String)
    placar = Column(String)
    resultado = Column(String)

    wl = relationship("WL", back_populates="partidas")

engine = create_engine('sqlite:///sistema_wl_orm.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
