class Usuario:
    qnt = 0

    def __init__(self, nome, email=""):
        self.nome = nome
        self.email = email
        self.qnt = Usuario.qnt
        Usuario.qnt += 1

    def imprime_usuario(self):
        print(f"Nome do Usuário: {self.nome}, e-amil do Usuário: {self.email}")

class Administrador(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome,email)
    def imprime_usuario(self):
        print(f"Nome do Usuário: {self.nome}, e-amil do Usuário: {self.email} - Administrador")

usu1=Usuario("Almir", "Almirlima140@exemplo.com")
usu=Administrador("Gabriel", "gabriel@exemplo.com")
usu.imprime_usuario()
usu1.imprime_usuario()
print(Usuario.qnt)