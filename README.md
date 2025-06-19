# SRT-Simulador-De-Tempo

Componentes: 
Alessandro da Rosa
Arthur B. Spada
Carolline Piccoli
Guilherme Castellani
Julia Braccini
Maria Eduarda B. Schulze
Mariana Melara

Este código simula o escalonamento de processos com o algoritmo SRT, que sempre escolhe o processo com o menor tempo restante de execução.
Funcionamento:
Cada processo tem um ID, um tempo de chegada e uma duração total.
O código simula o tempo passando (tempo) e acompanha:
Os processos que já chegaram (fila_pronta),
O processo que está em execução no momento,
Os processos finalizados.
A cada unidade de tempo:
Verifica se algum novo processo chegou e o adiciona à fila.
Ordena os processos prontos pelo tempo restante.
Executa por 1 unidade de tempo o processo com menor tempo restante.
Se o processo termina, ele é marcado como finalizado.
A simulação continua até todos os processos serem finalizados.
Ao final, o código imprime a ordem de execução e os processos finalizados.

Como executar:
Abrindo um editor de código, ou abrindo um prompt de comando dentro do diretório aonde está o arquivo
rodando o nome do arquivo, ex: python SRT.py (como é o título do nosso arquivo),
assim ele irá executar o código.
