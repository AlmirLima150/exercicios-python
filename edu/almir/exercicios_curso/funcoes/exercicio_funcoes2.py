def maior_idade(pessoa):
    if isinstance(pessoa, tuple):
        nome, idade = pessoa
    elif isinstance(pessoa, dict):
        nome = pessoa["nome"]
        idade = pessoa["idade"]
    else:
        raise ValueError("Tipo de dado inválido. Esperava-se uma tupla ou um dicionário.")

    if idade >= 18:
        print(f"{nome} é maior de idade.")
    else:
        print(f"{nome} não é maior de idade.")
pessoa1 = "almir", 22
maior_idade(pessoa1)
