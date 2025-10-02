from datetime import datetime

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

    if not nome or not data or not local or not categoria:
        print("Erro: Todos os campos são obrigatórios.")
        return
    
    if not validarData(data):
        print("Erro: Data inválida. Use o formato AAAA-MM-DD.")
        return
    
    count += 1
    # novo_id = len(listaEvento) + 1
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
    print("\n======================================")
    print("======== Lista de Eventos: ============")
    print("======================================")
    for evento in listaEvento:
        if evento["participado"] == True:
            status = "Sim"
        else:
            status = "Não"

        print(f"ID: {evento['id']}, Nome: {evento['nome']}, Data: {evento['data']}, "
              f"Local: {evento['local']}, Categoria: {evento['categoria']}, "
              f"Participado: {status}")
        print("--------------------------------------------------------------")
    print("=======================================================================\n")
# listarEventos(listaEventos)

# função para procurar evento por nome ou categoria
def procurarEventoPorNome(listaEvento, filtro):
    resultados = []
    for evento in listaEvento:
        if filtro.lower() in evento["nome"].lower() or filtro.lower() in evento["categoria"].lower():
            resultados.append(evento)
    
    if not resultados:
        print("Nenhum evento encontrado.")
        return [] # Retorna lista vazia se nada for encontrado
        
    return resultados 

# print(procurarEventoPorNome(listaEventos, "Hackathon"))  
# print(procurarEventoPorNome(listaEventos, "Acadêmico"))  
# print(procurarEventoPorNome(listaEventos, "Eventox")) 

# função para deletar evento
def deletarEvento(listaEvento, id):
    for i, evento in enumerate(listaEvento):
        if evento["id"] == id:
            listaEvento.pop(i)
            print("Evento deletado com sucesso!")
            return
    print("Evento não encontrado.")
    
# deletarEvento(listaEventos, 1)
# listarEventos(listaEventos)


# # Teste
# eventos = []
# adicionarEvento(eventos, "Evento 1", "2024-12-01", "Local A", "Categoria X")
# adicionarEvento(eventos, "Evento 2", "2024-12-02", "Local B", "Categoria Y")

# # Deletar um evento
# deletarEvento(eventos, 1)

# # Adicionar novo - ID deve ser 3, não 2
# adicionarEvento(eventos, "Evento 3", "2024-12-03", "Local C", "Categoria Z")

# listarEventos(eventos)
# # Deve mostrar: ID 2 e ID 3 (não ID 1 e 2)

# ==============================
# ======== ESTUDANTE B =========
# ==============================

# função displayMenu
def displayMenu():
    print("\n=========================================")
    print("==== Planejador de Eventos do Campus ====")
    print("=========================================")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Procurar por Nome/Categoria")
    print("6. Deletar Evento por ID")
    print("7. Gerar Relatório")
    print("8. Sair")
    print("=========================================")

#função para escolha do usuário
def getEscolhaDoUsuario():
    try:
        return int(input("Escolha uma opção (1-8): "))
    except ValueError:
        return 0
    
# função para filtrar eventos por categoria
def filtrarEventosPorCategoria(listaEventos, categoria):
    encontrados = [evento for evento in listaEventos if evento["categoria"].lower() == categoria.lower()]
    if not encontrados:
        print("\n==============================================================")
        print("Nenhum evento encontrado para a categoria especificada.")
    else:
        print("\n==============================================================")
        print(f"Eventos na categoria '{categoria}':")
        print("================================================================")

        for evento in encontrados:
            status = "Sim" if evento["participado"] else "Não"
            print(f"ID: {evento['id']}, Nome: {evento['nome']}, Data: {evento['data']}, "
                  f"Local: {evento['local']}, Categoria: {evento['categoria']}, "
                  f"Participado: {status}")
            print("--------------------------------------------------------------")
        print("======================================\n")


# Chamar a main
if __name__ == "__main__":
    eventos = []
    while True:
        displayMenu()
        escolha = getEscolhaDoUsuario()
        print("=========================================\n")

        match escolha:
            case 1:
                nome = input("Nome do Evento: ")
                data = input("Data (AAAA-MM-DD): ")
                local = input("Local: ")
                categoria = input("Categoria: ")
                adicionarEvento(eventos, nome, data, local, categoria)  
            
            case 2:
                listarEventos(eventos)

            case 3:
                categoria = input("Digite a categoria para filtrar: ")
                filtrarEventosPorCategoria(eventos, categoria)

            case 5:
                nomeOuCategoria = input("Digite o nome ou categoria para buscar: ")
                procurarEventoPorNome(eventos, nomeOuCategoria)
            
            case 6:
                try:
                    idEvento = int(input("Digite o ID do evento a ser deletado: "))
                    deletarEvento(eventos, idEvento)
                except ValueError:
                    print("\n===========================")
                    print("ID inválido.")
                    print("===========================\n")

            case 8:
                print("\n===========================")
                print("Saindo do sistema...")
                print("===========================\n")
                break