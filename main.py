print("===Planejador de Eventos do Campus===")
print("1.Adicionar Evento")
print("2.Ver Todos os Eventos")
print("3.Filtrar por Categoria")
print("4.Marcar Evento como Participado")
print("5.Gerar Relatório")
print("6.Sair")

count = 0

def adicionarEvento(listaEvento, nome, data, local, categoria):
    global count
    count += 1

    if not nome or not data or not local or not categoria:
        print("Erro: Todos os campos são obrigatórios.")
        return
    novoEvento = {
        "id": count,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": False    
    }
    listaEvento.append(novoEvento)
    print("Evento adicionado com sucesso!")
