from buscas import busca_sequencial, busca_binaria
from basededados import jogadores


def registrar_estatisticas(id_jogador, gols, assist, metodo="sequencial"):
    if metodo == "sequencial":
        jogador = busca_sequencial(jogadores, id_jogador)
    elif metodo == "binaria":
        jogadores.sort(key=lambda j: j.id)
        jogador = busca_binaria(jogadores, id_jogador)
    else:
        print("Método de busca inválido!")
        return

    if jogador:
        jogador.atualizar_estatisticas(gols, assist)
        print(f"Estatísticas atualizadas: {jogador}")
    else:
        print("Jogador não encontrado.")
