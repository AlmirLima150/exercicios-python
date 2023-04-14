# from random import random, randint
# valor = randint(1,5)
# numero = int(input('Escreva  o número aqui: '))
# if numero == valor:
#     print('Você venceu!')
# else:
#     print('Você perdeu')

from random import random, randint
valor=randint(1,10)
while True:
    numero = int(input("Tente adivinhar o número"))
    if numero != valor:
        print("você perdeu")
        continue
    else:
        print("você ganhou")
        break


