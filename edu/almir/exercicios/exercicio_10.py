from random import random, randint
while True:
    numero=int(input("digite uma opção. 1 - somar, 2 - multiplicar, 3 - maior, 4 - novos números, 5 - sair do programa"))
    if numero == 1:
        num=int(input("digite um numero"))
        num1=int(input("digite um numero"))
        print(f"a soma é {num+num1}")
    elif numero == 2:
        num=int(input("digite um numero"))
        num1=int(input("digite um numero"))
        print(f"a multipicação é {num*num1}")
    elif numero == 3:
        num=int(input("digite um numero"))
        num1=int(input("digite um numero"))
        if num > num1:
            print(num, num1)
        else:
            print(num1, num)
    elif numero== 4:
        valor=randint(1, 10)
        print(valor)
    elif numero== 5:
        break


