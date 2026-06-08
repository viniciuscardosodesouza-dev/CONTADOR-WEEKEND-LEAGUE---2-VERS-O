import time


def busca_sequencial(lista, chave, atributo="id"):
    comparacoes = 0
    inicio = time.time()
    for item in lista:
        comparacoes += 1
        if getattr(item, atributo) == chave:
            fim = time.time()
            salvar_log("Sequencial", comparacoes, fim - inicio)
            return item
    fim = time.time()
    salvar_log("Sequencial", comparacoes, fim - inicio)
    return None


def busca_binaria(lista, chave, atributo="id"):
    comparacoes = 0
    inicio = time.time()
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        valor = getattr(lista[meio], atributo)
        if valor == chave:
            fim = time.time()
            salvar_log("Binária", comparacoes, fim - inicio)
            return lista[meio]
        elif valor < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    fim = time.time()
    salvar_log("Binária", comparacoes, fim - inicio)
    return None


def salvar_log(tipo_busca, comparacoes, tempo):
    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(
            f"{tipo_busca} | Comparações: {comparacoes} | Tempo: {tempo:.6f}s\n")
