while True:
    valor_base = float(input("Digite o valor da base"))
    valor_altura = float(input("Digite o valor da altura"))
    valor_area = (valor_base * valor_altura) / 2

    print(f"O valor da area é {valor_area}")

    continuar = input("Deseja continuar? ")

    if continuar not in ("S, s, sim, Sim, SIM"):
        break
