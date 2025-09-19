from datetime import datetime

print("===Planejador de Eventos do Campus===")
print("1.Adicionar Evento")
print("2.Ver Todos os Eventos")
print("3.Filtrar por Categoria")
print("4.Marcar Evento como Participado")
print("5.Gerar Relatório")
print("6.Sair")


# função para validar data
def validarData(data_str):
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
count = 0

# função para adicionar evento
def adicionarEvento(listaEvento, nome, data, local, categoria):
    global count
    count += 1

    if not validarData(data):
        print("Erro: Data inválida. Use o formato AAAA/MM/DD.")
        return

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

# listaEventos = [
#     {"id": 1, "nome": "Hackathon", "data": "2025-05-20", "local": "Hall", "categoria": "Social", "participado": False},
#     {"id": 2, "nome": "Palestra Python", "data": "2025-05-21", "local": "Sala 101", "categoria": "Acadêmico", "participado": True}
# ]

# função para listar os eventos
def listarEventos(listaEvento):
    if not listaEvento:
        print("Nenhum evento cadastrado.")
        return
    for evento in listaEvento:
        if evento["participado"] == True:
            status = "Sim"
        else:
            status = "Não"

        print(f"ID: {evento['id']}, Nome: {evento['nome']}, Data: {evento['data']}, "
              f"Local: {evento['local']}, Categoria: {evento['categoria']}, "
              f"Participado: {status}")
        
# listarEventos(listaEventos)

# função para procurar evento por nome ou categoria
def procurarEventoPorNome(listaEvento, filtro):
    for evento in listaEvento:
        if evento["nome"].lower() == filtro.lower() or evento["categoria"].lower() == filtro.lower():
            return evento
        
    print("Evento não encontrado.")
    return

# print(procurarEventoPorNome(listaEventos, "Hackathon"))  
# print(procurarEventoPorNome(listaEventos, "Acadêmico"))  
# print(procurarEventoPorNome(listaEventos, "Eventox")) 

