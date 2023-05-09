def somar(numero1, numero2):
    print(f"A soma dos números é {numero1 + numero2} \n")
def subtrair(numero1, numero2):
    print(f"A subtração dos números é {numero1 - numero2} \n")
def dividir(numero1, numero2):
    print(f"A divisão dos números é {numero1 / numero2} \n")
def multiplicar(numero1, numero2):
    print(f"A multiplicação dos números é {numero1 * numero2} \n")

while True:
    escolha = int(input("Escolha 1 - somar"
                        "\n        2 - subtrair"
                        "\n        3 - dividir"
                        "\n        4 - multiplicar"
                        "\n        5 - sair "
                        "\nDigite sua escolha: "))
    match escolha:
        case 1:
            numero1 = int(input("Digite um numero: "))
            numero2 = int(input("Digite um numero: "))
            somar(numero1, numero2)
        case 2:
            numero1 = int(input("Digite um numero: "))
            numero2 = int(input("Digite um numero: "))
            subtrair(numero1, numero2)
        case 3:
            numero1 = int(input("Digite um numero: "))
            numero2 = int(input("Digite um numero: "))
            dividir(numero1, numero2)
        case 4:
            numero1 = int(input("Digite um numero: "))
            numero2 = int(input("Digite um numero: "))
            multiplicar(numero1, numero2)
        case 5:
            break



