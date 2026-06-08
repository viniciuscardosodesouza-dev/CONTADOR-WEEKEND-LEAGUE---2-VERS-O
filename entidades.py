import uuid


class Jogador:
    def __init__(self, nome):
        self.id = str(uuid.uuid4())[:8]
        self.nome = nome
        self.gols = 0
        self.assist = 0

    def atualizar_estatisticas(self, gols=0, assist=0):
        self.gols += gols
        self.assist += assist

    def __repr__(self):
        return f"{self.id} - {self.nome} | Gols: {self.gols}, Assistências: {self.assist}"


class Partida:
    def __init__(self, id_partida, adversario, placar, resultado):
        self.id = id_partida
        self.adversario = adversario
        self.placar = placar
        self.resultado = resultado

    def __repr__(self):
        return f"Partida {self.id} vs {self.adversario} | Placar: {self.placar} | Resultado: {self.resultado}"


class WL:
    def __init__(self, id_wl):
        self.id = id_wl
        self.partidas = []

    def adicionar_partida(self, partida):
        self.partidas.append(partida)

    def __repr__(self):
        return
