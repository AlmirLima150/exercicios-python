USUARIO = "Almir"
SENHA = "123456"
nome_usuario = input("Digite o nome do usuário: \n")
senha_usuario = input("Digite a senha: \n")

if nome_usuario == USUARIO and senha_usuario == SENHA:
    print("Login bem sucedido!")
else:
    print("Usuario ou senha incorretos, digite novamente.")

