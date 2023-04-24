# lista=['banana', 'maçã', 'melancia']
# for i in lista:
#     print(i)

# alunos=int(input("digite a quantidade de alunos"))
# lista_alunos=[]
# for i in range(0, alunos, +1):
#     lista_alunos.append(input("digite o nome do aluno"))
# for x in lista_alunos:
#     print(x)

# alunos=int(input("digite a quantidade de alunos"))
# lista_alunos=[]
# for i in range(0, alunos, +1):
#     lista_alunos.append(input("digite o nome do aluno"))
# for y in range(alunos):
#     print(lista_alunos[y], y)

# alunos=int(input("digite a quantidade de alunos"))
# lista_alunos=[]
# for i in range(0, alunos, +1):
#     lista_alunos.append(input("digite o nome do aluno"))
# nome=input("digite o nome a ser procurado")
# for x in range(lista_alunos):
#     if nome == lista_alunos[x]:
#         print(x, lista_alunos[x])

# notas = []
# soma = 0
# i = 0
# for x in range(5):
#     notas.append(float(input("digite a nota do aluno")))
# for z in range(5):
#     soma += notas[z]
# media = soma / 5
# print(f"A media da sala é {media:.2f}")
# for y in range(5):
#     if notas[y] >= media:
#         i+=1
# print(f"a quantidade de alunos a cima da media é {i}")

# numeros = []
# resultados = []
#
# for x in range(10):
#     numeros.append(int(input("digite um numero")))
# x=int(input("digite um multiplicador"))
# for y in range(10):
#     resultados.append(numeros[y] * x)
# print(resultados)

# numero = []
# # contrario = []
# for x in range(5):
#     numero.append(int(input("digite um numero")))
# for x in range(5-1, -1, -1):
#     print(numero[x])
# print(contrario)
# for i in range(5):
#     print(numero[i], end='')
# print()
# for j in range(5):
#     print(numero[4-j], end='')

# nome_usuario = []
# senha_usuario = []
# for x in range(5):
#     nome_usuario.append(input("digite o seu usuario"))
#     senha_usuario.append(input("digite a sua senha"))
# for y in range(5):
#     print(f'posição: {y}, usuario: {nome_usuario[y]}, senha: {senha_usuario[y]}')

nome_usuario = []
senha_usuario = []
for x in range(1):
    nome_usuario.append(input("digite o seu usuario"))
    senha_usuario.append(input("digite a sua senha"))
# while True:
digite_seu_usuario = input("digite seu usuario: ")
digite_sua_senha = input("digite sua senha: ")
for z in range(5):
    if digite_seu_usuario == nome_usuario[z] and digite_sua_senha == senha_usuario[z]:
        print("Login efetuado com sucesso!")
    #     break
    # else:
    #     print("Login ou senha errados, tente novamente")
    #