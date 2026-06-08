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
Session = sessionmaker(bind=engine)
session = Session()

def iniciar_banco():
    Base.metadata.create_all(engine)

def cadastrar_jogador(id_jogador, nome):
    try:
        novo_jogador = Jogador(id=id_jogador, nome=nome)
        session.add(novo_jogador)
        session.commit()
        return True
    except:
        session.rollback()
        return False

def buscar_jogador_por_nome(nome):
    return session.query(Jogador).filter(Jogador.nome.ilike(nome)).first()

def remover_jogador_por_nome(nome):
    jogador = buscar_jogador_por_nome(nome)
    if jogador:
        nome_removido = jogador.nome
        session.delete(jogador)
        session.commit()
        return nome_removido
    return None

def listar_todos_jogadores():
    return session.query(Jogador).all()

def listar_todas_wls():
    return session.query(WL).all()

def cadastrar_wl(id_semana):
    nova_wl = WL(id=id_semana)
    try:
        session.add(nova_wl)
        session.commit()
        return True
    except:
        session.rollback()
        return False