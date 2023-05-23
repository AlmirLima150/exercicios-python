class Conta:
    def __init__(self, id_conta, nome_conta, tipo_conta):
        self.id_conta = id_conta
        self.saldo = 0
        self.status_conta = False
        self.nome_conta = nome_conta
        self.tipo_conta = tipo_conta

    def depositar(self, valor_deposito):
        self.valor_deposito = valor_deposito
        if self.status_conta == False:
            print('A sua conta não está ativa')
        else:
            self.saldo += valor_deposito
            print(f'Um deposito de {valor_deposito} foi efetuado')

    def sacar(self, saque):
        if self.status_conta == False:
            print('A sua conta não está ativa')
        else:
            if self.saldo <= 0:
                print('Você não tem saldo para poder sacar')
            else:
                self.saldo -= saque
                print(f'Um saque de {saque} foi realizado')


    def verificar_saldo(self):
        if self.status_conta == False:
            print('A sua conta não está ativa')
        else:
            if self.saldo == 0:
                print('Seu saldo está zerado')
            else:
                print(f'O seu saldo é {self.saldo}')

    def ativar_conta(self):

        if self.status_conta == False:
            self.status_conta = True
        else:
            print('A conta já está ativa')

    def desativar_conta(self):

        if self.status_conta == True:
            if self.saldo >= 0:
                print('Você ainda tem saldo em conta, '
                        'primeiro saque o seu saldo')
            else:
                self.status_conta = False
                print('A sua conta foi destivada')
        else:
            print('Sua conta já está desativada')

    def ativar_limite(self, limite):
        self.limite = limite

    def desativar_limite(self):
        self.limite = 0
        print('O seu limite foi desativado')


conta1 = Conta(123456, 'Almir de Lima', 'Corrente')
conta1.ativar_conta()
conta1.ativar_conta()
conta1.depositar(100)
conta1.verificar_saldo()
conta1.sacar(100)
conta1.sacar(100)
conta1.sacar(100)
conta1.verificar_saldo()
conta1.sacar(100)
conta1.depositar(10)
conta1.desativar_conta()
