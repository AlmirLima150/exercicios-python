class Evento:
    def altera_nome_evento(self, novo_nome):
        print("Alterando nome do evento")
        self.nome = novo_nome

ev=Evento()
ev.nome="Aula de python"
print(ev.nome)

ev.altera_nome_evento("Aula de JavaScript")
print(ev.nome)