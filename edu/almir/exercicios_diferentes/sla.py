class Porta:
    def __init__(self, situacao):
        self.situacao = situacao

    def mostrar_situacao(self):
        print(f"A porta está {self.situacao}")

    def abrir_porta(self):
        self.situacao = "aberta"

    def fechar_porta(self):
        self.situacao = "fechada"


porta1 = Porta("fechada")
porta2 = Porta("aberta")
porta3 = Porta("aberta")

porta1.mostrar_situacao()
porta2.mostrar_situacao()
porta3.mostrar_situacao()

porta1.abrir_porta()
porta2.fechar_porta()
porta3.fechar_porta()

porta1.mostrar_situacao()
porta2.mostrar_situacao()
porta3.mostrar_situacao()
