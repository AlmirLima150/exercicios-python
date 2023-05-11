from funcoes import *

while True:

    aluno_nome = input('Digite o nome do aluno: ')
    media_nota = input('Digite a media do aluno: ')
    media_nota = float(media_nota)
    lista_add(aluno_nome, media_nota)

    continuar = input('deseja continuar? ')
    if continuar in 'NnaoNAO':
        break

print(aluno)
print(media)
