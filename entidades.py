class Jogador:
    def __init__(self, id_jogador, nome):
        self.id = id_jogador
        self.nome = nome
        self.gols = 0
        self.assist = 0

    def atualizar_estatisticas(self, gols, assist):
        self.gols += gols
        self.assist += assist

    def __repr__(self):
        return f"{self.id} - {self.nome} | Gols: {self.gols}, Assistencias: {self.assist}"


class Partida:
    def __init__(self, id_partida, adversario, placar, resultado):
        self.id = id_partida
        self.adversario = adversario
        self.placar = placar
        self.resultado = resultado

    def __repr__(self):
        return f"{self.id} x {self.adversario} | Placar: {self.placar} | Resultado: {self.resultado}"


class WL:
    def __init__(self, id_wl):
        self.id = id_wl
        self.partidas = []

    def adicionar_partida(self, partida):
        self.partidas.append(partida)

    def __repr__(self):
        return f"WL {self.id} | Partidas: {len(self.partidas)}"
