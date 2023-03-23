while True:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    operador = input("Digite o operador: ")
    if operador == "+":
        resultado = a + b
        print("O resultado é:", resultado)
    elif operador == "-":
        resultado = a - b
        print("O resultado é:", resultado)
    elif operador == "*":
        resultado = a * b
        print("O resultado é:", resultado)
    elif operador == "/":
        resultado = a / b
        print("O resultado é:", resultado)
    elif operador == "0":
        print("Fim!")
        break
    elif operador != "+" or "-" or "*" or "/":
        print("Digite um operador válido")


