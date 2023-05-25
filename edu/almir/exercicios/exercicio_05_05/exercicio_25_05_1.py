class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprime_ingresso(self):
        print(f'O valor do ingresso é R$ {self.valor}')

class vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprime_ingresso(self, valor_adicional):
        valor_adicional = self.valor * valor_adicional
        valor_total = self.valor + valor_adicional
        print(f'O valor do ingresso VIP é R$ {valor_total}')

ingresso1=Ingresso(150)
ingresso1.imprime_ingresso()
ingresso2 = vip(150)
ingresso2.imprime_ingresso(0.20)