import os
import uuid
from armazenamento import iniciar_banco, cadastrar_jogador, buscar_jogador_por_nome, remover_jogador_por_nome, listar_todos_jogadores, session, Jogador, WL, Partida


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

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            semana = int(input("Digite o número da semana da WL: "))
            wl_existente = session.query(WL).filter(WL.id == semana).first()
            if wl_existente:
                print(f"Semana {semana} já está cadastrada!")
            else:
                nova_wl = WL(id=semana)
                session.add(nova_wl)
                session.commit()
                print(f"Semana {semana} criada com sucesso!")
                print(f"Relatório da Semana {semana}: 0 Vitórias, 0 Derrotas")

        elif opcao == "2":
            nome = input("Digite o nome do jogador: ")
            id_gerado = str(uuid.uuid4())[:8]
            if cadastrar_jogador(id_gerado, nome):
                print(f"Jogador {nome} cadastrado!")
            else:
                print("Jogador já existe no sistema.")

        elif opcao == "3":
            semana = int(input("Digite a semana da WL: "))
            wl = session.query(WL).filter(WL.id == semana).first()
            if wl is None:
                print("Semana não encontrada. Crie a semana primeiro.")
                continue

            id_partida = len(wl.partidas) + 1
            adversario = input("Digite o adversário: ")
            placar = input("Digite o placar (ex: 2-1): ")
            resultado = input("Digite o resultado (Vitória/Derrota): ")
            while resultado.lower() not in ["vitória", "vitoria", "derrota"]:
                resultado = input(
                    "Resultado inválido. Digite apenas Vitória ou Derrota: ")

            nova_partida = Partida(id_partida=id_partida, wl_id=wl.id,
                                   adversario=adversario, placar=placar, resultado=resultado)
            session.add(nova_partida)

            while True:
                nome_jogador = input(
                    "Digite o nome do jogador (ou ENTER para parar): ")
                if nome_jogador == "":
                    break
                j = session.query(Jogador).filter(
                    Jogador.nome.ilike(nome_jogador)).first()
                if j:
                    gols = int(input("Gols marcados: "))
                    assist = int(input("Assistências: "))
                    j.gols += gols
                    j.assist += assist
                else:
                    print("Jogador não encontrado.")

            session.commit()
            print("Partida registrada com sucesso!")

            vitorias = sum(1 for p in wl.partidas if p.resultado.lower() in [
                           "vitória", "vitoria"])
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
                        f"{i}. {j.nome} (ID: {j.id}) | Gols: {j.gols} | Assistências: {j.assist}")

        elif opcao == "5":
            print("\n=== Semanas e Partidas ===")
            todas_wls = session.query(WL).all()
            if not todas_wls:
                print("Nenhuma semana cadastrada.")
            else:
                for wl in todas_wls:
                    print(f"\nSEMANA {wl.id}")
                    for p in wl.partidas:
                        print(
                            f"  Partida {p.id_partida} vs {p.adversario} | Placar: {p.placar} | Resultado: {p.resultado}")

        elif opcao == "6":
            print("\n=== Relatório por Semana ===")
            todas_wls = session.query(WL).all()
            if not todas_wls:
                print("Nenhuma semana cadastrada.")
            else:
                for wl in todas_wls:
                    vitorias = sum(1 for p in wl.partidas if p.resultado.lower() in [
                                   "vitória", "vitoria"])
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
