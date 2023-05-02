numero = int(input("digite um numero: "))
if numero % 2 == 0:
    if numero > 0:
        print("O numero é par e positivo")
    else:
        print("O numero é impar e positivo")

else:
    if numero < 0:
        print("O numero é par e negativo")
    else:
        print("O numero é impar e negativo")