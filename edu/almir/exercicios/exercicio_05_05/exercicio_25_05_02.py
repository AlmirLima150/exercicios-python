class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcula_area(self, base, altura):
        self.area = base * altura
        print(f'O valor da area é {self.area}')

    def calcula_perimetro(self, *lados):
        self.perimetro = lados + lados + lados + lados
        print(f'O valor do perimetro é {self.perimetro}')

class Triangulo(Forma):

    def __init__(self,altura):
        super().__init__()
        self.altura = altura

    def calcula_area(self, base):
        self.area = (base * self.altura)/2
        print(f'O valor da area é {self.area}')

    def calcula_perimetro(self, lado1, lado2, lado3):
        self.perimetro = lado1 + lado2 + lado3
        print(f'O valor do perimetro é {self.perimetro}')

ob1 = Triangulo(10)
ob1.calcula_area(5)
ob2 = Retangulo()
ob2.calcula_area(10, 5)
