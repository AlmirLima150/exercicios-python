def maior_idade(pessoa):
    nome, idade = pessoa
    if idade >= 18:
        print(f"{nome} é maior de idade.")
    else:
        print(f"{nome} não é maior de idade.")

pessoa1 = ("Almir", 22)
pessoa2 = ("Heloysa", 8)
maior_idade(pessoa1)
maior_idade(pessoa2)