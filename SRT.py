# Lista de processos com seus respectivos tempos de chegada e duração (tempo total de execução)
processos = [
    {"id": "P1", "chegada": 0, "duracao": 8},
    {"id": "P2", "chegada": 1, "duracao": 4},
    {"id": "P3", "chegada": 2, "duracao": 2},
    {"id": "P4", "chegada": 3, "duracao": 1},
]

# Inicialização do tempo atual
tempo = 0

# Lista de processos finalizados
finalizados = []

# Processo que está sendo executado no momento
em_execucao = None

# Fila de processos prontos para serem executados (que já chegaram)
fila_pronta = []

# Adiciona a cada processo um campo extra: "restante" para guardar o tempo restante de execução
for p in processos:
    p["restante"] = p["duracao"]

# Cabeçalho da simulação
print("Escalonamento SRT:")
print("Tempo | Processo")

# Loop principal: continua até que todos os processos tenham sido finalizados
while len(finalizados) < len(processos):
    
    # Verifica se algum processo chega no tempo atual e o adiciona à fila pronta
    for p in processos:
        if p["chegada"] == tempo:
            fila_pronta.append(p)

    # Se houver processos prontos para executar
    if fila_pronta:
        # Ordena a fila pelos tempos restantes (SRT: o menor tempo restante é escolhido)
        fila_pronta = sorted(fila_pronta, key=lambda x: x["restante"])

        # Seleciona o processo com menor tempo restante para executar
        em_execucao = fila_pronta[0]

        # Exibe o processo em execução naquele tempo
        print(f"  {tempo}   |   {em_execucao['id']}")

        # Reduz o tempo restante do processo em 1 unidade de tempo
        em_execucao["restante"] -= 1

        # Se o processo terminou (tempo restante chegou a 0)
        if em_execucao["restante"] == 0:
            finalizados.append(em_execucao)      # Adiciona à lista de finalizados
            fila_pronta.remove(em_execucao)      # Remove da fila de prontos
    else:
        # Caso não haja processos prontos, imprime que nenhum está executando
        print(f"  {tempo}   |   Nenhum")

    # Avança o tempo
    tempo += 1

# Exibe os processos finalizados ao fim da execução
print("\nFinalizados:")
for p in finalizados:
    print(f"  {p['id']}")
