SENHA="123456"
vezes=0
senha1=input("digite uma senha")
while senha1!=SENHA:
    senha1=input("Digite uma senha valida")
    vezes += 1
    if senha1!=SENHA and vezes==2:
        print("Limite de tentativas excedidas, sua senha foi bloqueada")
        break
else:
    print("efetuando login")

