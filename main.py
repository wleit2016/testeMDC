from Calculos import proximoNumeroPrimo
from Calculos import eDivisivel

def exibir(numero1, numero2, primo):
    print(numero1, "-", numero2, "|", primo)

if __name__ == '__main__':
    numeroPrimo = 2
    repita = True
    listaNumerosPrimos = []

    numero1TXT = input("Digite um numero: ")
    numero2TXT = input("Digite outro numero: ")

    numero1 = int(numero1TXT)
    numero2 = int(numero2TXT)

    while repita:
        if eDivisivel(numero1, numeroPrimo) and eDivisivel(numero2, numeroPrimo):
            exibir(numero1, numero2, numeroPrimo)
            listaNumerosPrimos.append(numeroPrimo)
            numero1 = int(numero1 / numeroPrimo)
            numero2 = int(numero2 / numeroPrimo)
        else:
            if eDivisivel(numero1, numeroPrimo):
                exibir(numero1, numero2, numeroPrimo)
                numero1 = int(numero1 / numeroPrimo)
            else:
                if eDivisivel(numero2, numeroPrimo):
                    exibir(numero1, numero2, numeroPrimo)
                    numero2 = int(numero2 / numeroPrimo)
                else:
                    numeroPrimo = proximoNumeroPrimo(numeroPrimo)

        if numero1 == 1 and numero2 == 1:
            repita = False