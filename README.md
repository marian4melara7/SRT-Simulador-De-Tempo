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

Analise dos Resultados, após rodar o código.
Escalonamento SRT:
Tempo | Processo    
  0   |   P1      
  1   |   P2       
  2   |   P3
  3   |   P3
  4   |   P4
  5   |   P2
  6   |   P2
  7   |   P2
  8   |   P1
  9   |   P1
  10   |   P1
  11   |   P1
  12   |   P1
  13   |   P1
  14   |   P1

Finalizados:
  P3
  P4
  P2
  P1
Esse comportamento é esperado no algoritmo SRT, que:
Sempre escolhe o processo com menor tempo restante, não importa quem começou antes.
Faz interrupção de processos quando necessário.
Dá vantagem para processos curtos que chegam depois.
O motivo de P1 terminar por último, mesmo tendo chegado primeiro,
é que ele foi interrompido várias vezes por processos com menor duração, o que é típico no SRT.


