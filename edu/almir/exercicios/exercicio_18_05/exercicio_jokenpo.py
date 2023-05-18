import random

def escolha_computador():
    escolhas_computador = ['Pedra', 'Papel', 'Tesoura']
    escolha = random.choice(escolhas_computador)
    return escolha

def escolha_pessoa():
    escolha = ['Pedra', 'Papel', 'Tesoura']
    while True:
        escolha_pessoa = input('Escolha: Pedra, Papel, Tesoura')
        if escolha_pessoa not in escolha:
            print('Escolha entre "Pedra, Papel, Tesoura"')
        else:
            return escolha_pessoa

def inicio_jokenpo():
    escolha_computador()

    escolha_pessoa()

    if escolha_computador == 'Pedra' and escolha_pessoa == 'Pedra':
        print('Foi empate')
    elif escolha_computador == 'Papel' and escolha_pessoa == 'Papel':
        print('Foi empate')
    elif escolha_computador == 'Tesoura' and escolha_pessoa == 'Tesoura':
        print('Foi empate')

inicio_jokenpo()