print("===Planejador de Eventos do Campus===")
print("1.Adicionar Evento")
print("2.Ver Todos os Eventos")
print("3.Filtrar por Categoria")
print("4.Marcar Evento como Participado")
print("5.Gerar Relatório")
print("6.Sair")

# Criando a classe Evento
class Evento:
    def __init___(self, nome, data, local, categoria):
        self.nome = nome
        self.data = data
        self.local = local
        self.categoria = categoria
        self.participado = False