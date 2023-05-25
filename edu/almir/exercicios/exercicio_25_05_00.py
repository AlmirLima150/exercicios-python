class Animal:
    def __init__(self, cor, nome):
        self.cor = cor
        self.nome = nome

    def comer(self):
        print(f'{self.nome} foi comer')

class Cachorro(Animal):
    def __init__(self, cor, nome):
        super().__init__(cor,nome)

    def emitir_som(self):
        print(f'{self.nome} está emitindo som')

    def comer(self, alimento):
        self.alimento = alimento
        print(f'{self.nome} foi comer {alimento}')

class Gato(Animal):
    def __init__(self, cor, nome):
        super().__init__(cor,nome)

    def emitir_som(self):
        print(f'{self.nome} está emitindo som')

    def comer(self, alimento):
        self.alimento = alimento
        print(f'{self.nome} foi comer {alimento}')

class Vaca(Animal):
    def __init__(self, cor, nome):
        super().__init__(cor,nome)

    def emitir_som(self):
        print(f'{self.nome} está emitindo som')

class Coelho(Animal):
    def __init__(self, cor, nome):
        super().__init__(cor,nome)

    def emitir_som(self):
        print(f'{self.nome} está emitindo som')

    def saltar(self):
        print(f'{self.nome} está saltando')

animal1 = Cachorro('Branco', 'Rabbit')
animal1.comer('Ração')

animal2 = Gato('Sortido', 'Cat')
animal2.comer('Peixe')
