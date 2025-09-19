print("===Planejador de Eventos do Campus===")
print("1.Adicionar Evento")
print("2.Ver Todos os Eventos")
print("3.Filtrar por Categoria")
print("4.Marcar Evento como Participado")
print("5.Gerar Relatório")
print("6.Sair")

def adicionarEvento(listaEvento, nome, data, local, categoria):
    novoEvento = {
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": False    
    }
    listaEvento.append(novoEvento)
    print("Evento adicionado com sucesso!")
