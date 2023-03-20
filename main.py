from Calculos import proximoNumeroPrimo

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
        if numero1 % numeroPrimo == 0 and numero2 % numeroPrimo == 0:
            exibir(numero1, numero2, numeroPrimo)
            listaNumerosPrimos.append(numeroPrimo)
            numero1 = int(numero1 / numeroPrimo)
            numero2 = int(numero2 / numeroPrimo)
        else:
            if numero1 % numeroPrimo == 0:
                exibir(numero1, numero2, numeroPrimo)
                numero1 = int(numero1 / numeroPrimo)
            else:
                if numero2 % numeroPrimo == 0:
                    exibir(numero1, numero2, numeroPrimo)
                    numero2 = int(numero2 / numeroPrimo)
                else:
                    numeroPrimo = proximoNumeroPrimo(numeroPrimo)

        if numero1 == 1 and numero2 == 1:
            repita = False