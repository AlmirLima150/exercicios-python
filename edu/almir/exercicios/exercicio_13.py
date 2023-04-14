while True:
    n1 = float(input("digite a 1º nota"))
    while 0 < n1 > 10:
        n1 = float(input("digite a 1º nota"))
    n2=float(input("digite a 2º nota"))
    while 0 < n2 > 10:
        n2 = float(input("digite a 2º nota"))
    print(f"{(n1+n2)/2}")
    escolha=input("deseja continuar?")
    if escolha in "Ss":
        continue
    else:
        print("programa finalizado")
        break