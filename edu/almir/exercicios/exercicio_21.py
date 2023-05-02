continuar = "sim"
while continuar == "sim":
    numero = int(input("digite um numero: "))

    if numero == 0:
        print("Digite um numero diferente de zero")
        continue
    if numero > 0:
        print("O número digitado é positivo")
    else:
        print("O número digitado é negativo")

    continuar = input("Deseja continuar? ")