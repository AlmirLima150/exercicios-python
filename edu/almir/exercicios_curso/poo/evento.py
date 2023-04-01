class Evento:
    id = 1

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Local do evento: {self.local}")
        print("------------------------------")

    @staticmethod
    def area_pessoas_evento(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return "Nessa área não é possivel realizar o evento"

class EventoOnline(Evento):
    def __init__(self, nome, _=""):
        local = f"htts://tamarcado.com/eventos?id={EventoOnline.id}"
        super().__init__(nome, local)
    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Link para acessar o evento: {self.local}")
        print("------------------------------")



ev = Evento("Aula de python","João Pessoa")
ev2=Evento("Aula de puthon", "Recife")
ev3=EventoOnline("Aula de python")
ev.imprime_informacoes()
ev2.imprime_informacoes()
ev3.imprime_informacoes()



# ev_online2 = Evento.cria_evento_online("Aula de java")
# ev_online3 = Evento.cria_evento_online("Aula de Bootstrap")
# ev=Evento("Aula de python")
# ev_online=Evento.cria_evento_online("Live de pyhton")
# ev.imprime_informacoes()
# ev2.imprime_informacoes()
# ev_online.imprime_informacoes()
# print(ev_online.imprime_informacoes())
# print(ev_online2.imprime_informacoes())
# print(ev_online3.imprime_informacoes())