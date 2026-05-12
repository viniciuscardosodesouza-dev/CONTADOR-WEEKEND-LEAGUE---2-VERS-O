from entidades import Jogador, Partida, WL
import random

jogadores = []
partidas = []
WLs = []


def criar_base():
    # alterar base de dados quantidade de jogadores
    for i in range(1, 121):
        jogador = Jogador(i, f"Jogador {i}")
        jogador.atualizar_estatisticas(
            gols=random.randint(0, 30),
            assist=random.randint(0, 15)
        )
        jogadores.append(jogador)

    # alterar base de dados da semana
    for semana in range(1, 11):
        wl = WL(semana)
        for p in range(1, 16):
            placar = f"{random.randint(0, 5)}-{random.randint(0, 5)}"
            resultado = random.choice(["Vitória", "Derrota", "Empate"])
            partida = Partida(p + (semana-1)*15,
                              f"Time_{p}", placar, resultado)
            wl.adicionar_partida(partida)
            partidas.append(partida)
        WLs.append(wl)
