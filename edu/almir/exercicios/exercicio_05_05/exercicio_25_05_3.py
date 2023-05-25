class Atleta:
    def __init__(self, peso):
        self.aposentado = False
        self.peso = peso
    def aposentar(self):
        self.aposentado = True
        print('O atleta se aposentou!')

    def aquecer(self):
        print('O atleta está aqucendo!')

class Corredor(Atleta):
    def __init__(self,peso):
        super().__init__(peso)

    def correr(self):
        print('O atleta foi correr')

class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def nadar(self):
        print('O atleta foi nadar')

class Ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def pedalar(self):
        print('O atleta foi pedalar')

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, peso):
        super().__init__(peso)

almir = TriAtleta(79)
almir.aquecer()
almir.nadar()
almir.correr()
almir.pedalar()
almir.aposentar()