class Evento:
    def __init__(self, nome):
        self.nome=nome
        self.local="Recife"
    def altera_nome_evento(self, novo_nome):
        print("Alterando nome do evento")
        self.nome = novo_nome
    def altera_local_evento(self,novo_local):
        print("Alterando local do evento")
        self.local=novo_local

ev=Evento("Aula JvaScript")
ev2=Evento("Aula de Python")

print(ev.nome)
print(ev.local)
ev.altera_local_evento("Olinda")
print(ev.local)
ev.altera_nome_evento("Aula de Java")
print(ev.nome)
print(ev2.nome)
print(ev2.local)