class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, falando=False, andando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.andando = andando

    def comer(self, comida):
        self.comida = comida

        if self.falando == True:
            print(f'{self.nome} está falando, não pode comer')
        else:
            if self.comendo == True:
                print(f'{self.nome} já está comendo!')
            else:
                print(f'{self.nome} está comendo {self.comida}')
                self.comendo = True

    def parar_comer(self):

        if self.comendo == True:
            self.comendo = False
            self.comida = ''
            print(f'{self.nome} parou de comer!')
        else:
            print(f'{self.nome} não está comendo')

    def falar(self):

        if self.comendo == True:
            print(f'{self.nome} está comendo, não pode falar')
        else:
            if self.falando == True:
                print(f'{self.nome} já está falando!')
            else:
                print(f'{self.nome} comecou a falar')
                self.falando = True

    def parar_falar(self):

        if self.falando == True:
            self.falando = False
            print(f'{self.nome} parou de falar!')
        else:
            print(f'{self.nome} não está falando')

    def andar(self):

        if self.andando == True:
            print(f'{self.nome} já está andando!')
        else:
            print(f'{self.nome} comecou a andar')
            self.andando = True

    def parar_andar(self):
        if self.andando == True:
            self.andando = False
            print(f'{self.nome} parou de andar!')
        else:
            print(f'{self.nome} não está andando')

p1 = Pessoa('Almir', 100, 23)
p1.falar()
p1.andar()
p1.comer('macarrão')
