# exercicio 1
lista = []
while True:
    receba_um_numero = int(input("Digite um número "))
    lista.append(receba_um_numero)
    if receba_um_numero < 0:
        lista.pop()
        break
print(lista)

