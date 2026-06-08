import sqlite3


def iniciar_banco():
    conn = sqlite3.connect("sistema_wl.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
            id TEXT PRIMARY KEY,
            nome TEXT UNIQUE,
            gols INTEGER,
            assist INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS partidas (
            id_partida INTEGER,
            wl_id INTEGER,
            adversario TEXT,
            placar TEXT,
            resultado TEXT,
            PRIMARY KEY (id_partida, wl_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wls (
            id INTEGER PRIMARY KEY
        )
    """)
    conn.commit()
    conn.close()


def cadastrar_jogador(id_jogador, nome):
    conn = sqlite3.connect("sistema_wl.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO jogadores (id, nome, gols, assist) VALUES (?, ?, 0, 0)", (id_jogador, nome))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def buscar_jogador_por_nome(nome):
    conn = sqlite3.connect("sistema_wl.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, gols, assist FROM jogadores WHERE LOWER(nome) = LOWER(?)", (nome,))
    jogador = cursor.fetchone()
    conn.close()
    return jogador


def remover_jogador_por_nome(nome):
    conn = sqlite3.connect("sistema_wl.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nome FROM jogadores WHERE LOWER(nome) = LOWER(?)", (nome,))
    jogador = cursor.fetchone()
    if jogador:
        cursor.execute(
            "DELETE FROM jogadores WHERE LOWER(nome) = LOWER(?)", (nome,))
        conn.commit()
        conn.close()
        return jogador[0]
    conn.close()
    return None


def listar_todos_jogadores():
    conn = sqlite3.connect("sistema_wl.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, gols, assist FROM jogadores")
    jogadores = cursor.fetchall()
    conn.close()
    return jogadores
