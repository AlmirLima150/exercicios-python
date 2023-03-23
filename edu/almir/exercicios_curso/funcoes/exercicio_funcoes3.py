def encontrar_maior(lista):
    maior = lista[0]
    posicao = 0

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i

    return (posicao, maior)
lista = [10, 5, 7, 21, 4, 55, 7, 26, 13]
posicao, maior = encontrar_maior(lista)
print(f"O maior número é {maior} e está na posição {posicao}")