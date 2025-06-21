# SRT - Simulador de Tempo com Python

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Finalizado-green)

## Sobre o Projeto 🎯

> Atividade da disciplina _**Sistemas Operacionais**_ do curso de **Ciência da Computação** — _Atitus Educação_.

Este sistema simula o algoritmo **Shortest Remaining Time (SRT)**, um método de escalonamento preemptivo que prioriza o processo com o menor tempo restante de execução. A simulação é feita em Python, onde cada processo é controlado com base no tempo de chegada e duração restante.

Ideia principal:
- Simular o funcionamento de um escalonador de processos com SRT.
- Compreender a lógica preemptiva e priorização por tempo restante.
- Estudar algoritmos de escalonamento de CPU.
- Aplicar conceitos teóricos na prática, através da programação.

---

## Funcionalidades 🧩

- Simulação por ciclos de tempo
- Escalonamento dinâmico com interrupções
- Impressão da ordem de execução dos processos
- Relatório final com processos finalizados
- Interface por terminal simples e clara

## Dinâmica do sistema

Cada processo tem um **ID**, um **tempo de chegada** e uma **duração total**.
O código simula o tempo passando (``tempo``) e acompanha:
- Os processos que já chegaram (``fila_pronta``).
- O processo que está em execução no momento.
- Os processos finalizados.

A cada unidade de tempo:
- Verifica se algum novo processo chegou e o adiciona à fila.
- Ordena os processos prontos pelo tempo restante.
- Executa por 1 unidade de tempo o processo com menor tempo restante.
- Se o processo termina, ele é marcado como finalizado.

A simulação continua até todos os processos finalizarem. Por fim, o código imprime a ordem de execução e os processos finalizados.

---

# Como executar a aplicação localmente

### Pré Requisitos
- ``Git`` (para clonar o repositório)
- ``Python 3.10`` (ou superior)
- ``Editor de código`` (VSCode recomendado)

### Instalação ⬇️

1. Clone o repositório:

```bash
git clone https://github.com/marian4melara7/SRT-Simulador-De-Tempo.git
```
2. Acesse a pasta do projeto:

```bash
cd SRT-Simulador-De-Tempo
```

3. Abra no VSCode:

```bash
code .
```


### Configuração e Uso ⚙️

1. Execute o script principal:

```bash
python SRT.py
```
---

## Exemplos de Saída

```bash
Tempo | Processo
0     | P1
1     | P2
2     | P3
3     | P3
4     | P4
5     | P2
6     | P2
7     | P2
8     | P1
9     | P1
10    | P1
11    | P1
12    | P1
13    | P1
14    | P1
```

**Finalizados:** P3 → P4 → P2 → P1


‼️ Esse comportamento é esperado no algoritmo SRT, que:

- Sempre escolhe o processo com menor tempo restante, não importa quem começou antes.
- Faz interrupção de processos quando necessário.
- Dá vantagem para processos curtos que chegam depois.

O motivo de P1 terminar por último, mesmo tendo chegado primeiro, é que ele foi interrompido várias vezes por processos com menor duração, o que é típico no SRT.

---

## Contribuidores 🧑🏻‍💻
- Alessandro da Rosa
- Arthur Spada
- Carolline Piccoli
- Guilherme Castellani
- Julia Braccini
- Maria Eduarda Schulze
- Mariana Melara

## Autores

<div align="left">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/jubraccini">
          <img src="https://avatars.githubusercontent.com/u/117121095?v=4" width="100px" alt="Julia Braccini" style="border-radius: 50%;" /><br />
          <sub><b>Julia Braccini</b></sub>
        </a>
      </td>
      <td align="center" style="padding-left: 30px;">
        <a href="https://github.com/ArthurBava">
          <img src="https://avatars.githubusercontent.com/u/171097679?v=4" width="100px" alt="Arthur Spada" style="border-radius: 50%;" /><br />
          <sub><b>Arthur Spada</b></sub>
        </a>
      </td>
    </tr>
  </table>
</div>
