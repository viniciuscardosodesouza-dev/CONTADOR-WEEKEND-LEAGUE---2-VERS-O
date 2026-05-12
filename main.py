from basededados import criar_base, jogadores, WLs
from operacoes import registrar_estatisticas


def main():
    criar_base()

    print("Jogadores:")
    for j in jogadores:
        print(j)

    print("\nWLs:")
    for wl in WLs:
        print(wl)
        for partida in wl.partidas:
            print("  ", partida)

    print("\nAtualizando estatísticas:")
    registrar_estatisticas(10, 2, 1, metodo="sequencial")
    registrar_estatisticas(20, 3, 0, metodo="binaria")


if __name__ == "__main__":
    main()
