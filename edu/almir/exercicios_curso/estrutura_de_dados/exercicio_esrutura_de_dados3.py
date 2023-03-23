lista = [1, 10, 20, 35, 22, 12]
i = 0
total = 0
while i < len(lista):
    total = total + lista[i]
    media = total // len(lista)
    print("A media é", media)
    i += 1