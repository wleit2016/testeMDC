def eDivisivel(numero, fatorPrimo):
    resposta = False
    if numero % fatorPrimo == 0:
        resposta = True
    return resposta

def ePrimo(numero):
    resposta = False
    posicao = 2
    contar = 0

    while (posicao <= numero) and (contar != 2):
        if numero % posicao == 0:
            contar = contar + 1
        posicao = posicao + 1

    if contar == 1:
        resposta = True

    return resposta

def proximoNumeroPrimo(numero):
    numero = numero + 1

    while not ePrimo(numero):
        numero = numero + 1

    return numero