processos = [
    {"id": "P1", "chegada": 0, "duracao": 8},
    {"id": "P2", "chegada": 1, "duracao": 4},
    {"id": "P3", "chegada": 2, "duracao": 2},
    {"id": "P4", "chegada": 3, "duracao": 1},
]
tempo = 0
finalizados = []
em_execucao = None
fila_pronta = []

for p in processos:
    p["restante"] = p["duracao"]

print("Escalonamento SRT:")
print("Tempo | Processo")

while len(finalizados) < len(processos):
    for p in processos:
        if p["chegada"] == tempo:
            fila_pronta.append(p)

    if fila_pronta:
        fila_pronta = sorted(fila_pronta, key=lambda x: x["restante"])
        em_execucao = fila_pronta[0]
        print(f"  {tempo}   |   {em_execucao['id']}")
        em_execucao["restante"] -= 1

        # Verificar se finalizou
        if em_execucao["restante"] == 0:
            finalizados.append(em_execucao)
            fila_pronta.remove(em_execucao)
    else:
        print(f"  {tempo}   |   Nenhum")

    tempo += 1
print("\nFinalizados:")
for p in finalizados:
    print(f"  {p['id']}")