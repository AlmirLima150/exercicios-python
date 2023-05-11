def somar(numero1, numero2):
    print(f"A soma dos números é {numero1 + numero2} \n")

def subtrair(numero1, numero2):
    print(f"A subtração dos números é {numero1 - numero2} \n")

def dividir(numero1, numero2):
    print(f"A divisão dos números é {numero1 / numero2} \n")

def multiplicar(numero1, numero2):
    print(f"A multiplicação dos números é {numero1 * numero2} \n")

def valor_estoque(nome, quantidade, vl_unitario):
    valor_do_estoque = quantidade * vl_unitario
    return nome, valor_do_estoque

def imprimir_nome(nome):
    print(f"Nome: {nome[::-1]}")

def repeticao(numero):
    for x in range(1, numero+1):
        print(x*str(x))

def achando_vogais(texto):
    VOGAIS = "AaEeIiOoUu"
    i = 0
    for x in texto:
        if x in VOGAIS:
            i+=1
    print(f"A quantidade de vogais no texto é {i}")

def argumento():
    argumento = input('Digite uma numero: ')
    if argumento.isdigit():
        argumento = int(argumento)
        if argumento > 0:
            print('Positivo')
        elif argumento == 0:
            print('Zero')
        else:
            print('Negativo')

aluno = []
media = []
def lista_add(aluno_nome, media_nota):
    aluno.append(aluno_nome)
    media.append(media_nota)

def somar(*args):
    soma = 0
    for x in args:
        soma += x
    print(f"A soma dos números é {soma}")




