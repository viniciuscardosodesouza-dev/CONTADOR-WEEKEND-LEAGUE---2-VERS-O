import os
import uuid
from basededados import jogadores, partidas, WLs
from armazenamento import iniciar_banco, cadastrar_jogador, buscar_jogador_por_nome, remover_jogador_por_nome, listar_todos_jogadores
from entidades import Jogador, Partida, WL


def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Criar nova semana da WL")
        print("2 - Cadastrar jogador")
        print("3 - Registrar partida")
        print("4 - Listar jogadores")
        print("5 - Listar semanas e partidas")
        print("6 - Relatório por semana (Vitórias/Derrotas)")
        print("7 - Remover jogador")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            semana = int(input("Digite o número da semana da WL: "))
            wl = WL(semana)
            WLs.append(wl)
            print(f"Semana {semana} criada com sucesso!")

            vitorias = sum(
                1 for p in wl.partidas if p.resultado.lower() == "vitória")
            derrotas = sum(
                1 for p in wl.partidas if p.resultado.lower() == "derrota")
            print(
                f"Relatório da Semana {wl.id}: {vitorias} Vitórias, {derrotas} Derrotas")

        elif opcao == "2":
            nome = input("Digite o nome do jogador: ")
            id_gerado = str(uuid.uuid4())[:8]
            if cadastrar_jogador(id_gerado, nome):
                print(f"Jogador {nome} cadastrado!")
            else:
                print("Jogador já existe no sistema.")

        elif opcao == "3":
            semana = int(input("Digite a semana da WL: "))
            wl = next((w for w in WLs if w.id == semana), None)
            if wl is None:
                print("Semana não encontrada. Crie a semana primeiro.")
                continue

            id_partida = len(wl.partidas) + 1
            adversario = input("Digite o adversário: ")
            placar = input("Digite o placar (ex: 2-1): ")

            resultado = input("Digite o resultado (Vitória/Derrota): ")
            while resultado.lower() not in ["vitória", "derrota"]:
                resultado = input(
                    "Resultado inválido. Digite apenas Vitória ou Derrota: ")

            partida = Partida(id_partida, adversario, placar, resultado)
            wl.adicionar_partida(partida)
            partidas.append(partida)

            while True:
                nome_jogador = input(
                    "Digite o nome do jogador (ou ENTER para parar): ")
                if nome_jogador == "":
                    break
                jogador = next(
                    (j for j in jogadores if j.nome.lower() == nome_jogador.lower()), None)
                if jogador:
                    gols = int(input("Gols marcados: "))
                    assist = int(input("Assistências: "))
                    jogador.atualizar_estatisticas(gols, assist)
                else:
                    print("Jogador não encontrado.")

            salvar_partidas(partidas)
            salvar_jogadores(jogadores)
            print("Partida registrada com sucesso!")

            vitorias = sum(
                1 for p in wl.partidas if p.resultado.lower() == "vitória")
            derrotas = sum(
                1 for p in wl.partidas if p.resultado.lower() == "derrota")
            print(
                f"Relatório da Semana {wl.id}: {vitorias} Vitórias, {derrotas} Derrotas")

        elif opcao == "4":
            print("\n=== Lista de Jogadores ===")
            jogadores = listar_todos_jogadores()
            if not jogadores:
                print("Nenhum jogador cadastrado.")
            else:
                for i, j in enumerate(jogadores, start=1):
                    print(
                        f"{i}. {j[1]} (ID: {j[0]}) | Gols: {j[2]} | Assistências: {j[3]}")

        elif opcao == "5":
            print("\n=== Semanas e Partidas ===")
            for wl in WLs:
                print(f"\nSEMANA {wl.id}")
                for p in wl.partidas:
                    print("   ", p)

        elif opcao == "6":
            print("\n=== Relatório por Semana ===")
            for wl in WLs:
                vitorias = sum(
                    1 for p in wl.partidas if p.resultado.lower() == "vitória")
                derrotas = sum(
                    1 for p in wl.partidas if p.resultado.lower() == "derrota")
                print(
                    f"Semana {wl.id}: {vitorias} Vitórias, {derrotas} Derrotas")

        elif opcao == "7":
            nome_remover = input(
                "Digite o nome do jogador que deseja remover: ")
            removido = remover_jogador_por_nome(nome_remover)
            if removido:
                print(f"Jogador {removido} removido com sucesso!")
            else:
                print("Jogador não encontrado.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


def main():

    iniciar_banco()

    menu()


if __name__ == "__main__":
    main()
