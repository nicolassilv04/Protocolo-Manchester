# Simulador de Triagem - Protocolo de Manchester

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Este projeto é um simulador de sistema de triagem hospitalar baseado no Protocolo de Manchester. Ele foi desenvolvido como uma atividade acadêmica para a disciplina de Estrutura de Dados.

O objetivo principal é aplicar na prática duas estruturas de dados fundamentais:
1.  **Árvores de Decisão:** para classificar a urgência do paciente.
2.  **Filas (Queues):** para gerenciar os pacientes de cada nível de prioridade.

---

## 🚀 Funcionalidades

O sistema opera através de um menu interativo no terminal, permitindo as seguintes ações:

* **1. Cadastrar Paciente:**
    * O sistema faz uma série de perguntas (a "árvore de decisão") para classificar o paciente.
    * Ao final, o paciente é adicionado à fila de prioridade correspondente (Vermelho, Laranja, Amarelo, Verde ou Azul).

* **2. Chamar Paciente:**
    * O sistema chama o próximo paciente a ser atendido, seguindo rigorosamente a ordem de prioridade.
    * A prioridade é: `Vermelho > Laranja > Amarelo > Verde > Azul`.
    * Dentro de uma mesma cor, os pacientes são chamados por ordem de chegada (FIFO).

* **3. Mostrar Status das Filas:**
    * Exibe a contagem de quantos pacientes estão aguardando em cada uma das cinco filas.

* **0. Sair:**
    * Encerra a execução do programa.

---

## 🛠 Estruturas de Dados Utilizadas

Este projeto foi construído do zero (`vanilla`) em Python, sem bibliotecas externas, para focar na implementação das estruturas de dados.

### 🌲 Árvore de Decisão

O "cérebro" da classificação é uma Árvore Binária de Decisão, implementada na classe `NodoArvore`.

* **Nó Interno (Pergunta):** Possui uma `pergunta` e dois ponteiros (`ramo_sim` e `ramo_nao`) que levam à próxima pergunta ou a uma classificação final.
* **Nó Folha (Resposta):** Não possui pergunta (`is_folha() == True`) e armazena a `cor` e a `descricao` da classificação final.

O processo de triagem (`função triagem()`) é uma navegação por esta árvore, começando da `raiz` e descendo os ramos de acordo com as respostas "sim" ou "não" do usuário, até que um nó folha seja alcançado.

### ➡️ Fila (Queue)

Para gerenciar os pacientes, o sistema utiliza cinco instâncias da classe `Fila`, uma para cada cor de prioridade.

* **Implementação:** A Fila foi implementada usando como base uma **Lista Simplesmente Encadeada**.
* **Performance (FIFO):** A estrutura foi otimizada para operações de Fila (First-In, First-Out).
    * `enqueue(valor)`: Adiciona um paciente ao final da fila. Esta operação é $O(1)$ (tempo constante), pois mantemos um ponteiro direto para a `__cauda` da lista.
    * `dequeue()`: Remove um paciente do início da fila. Esta operação também é $O(1)$, pois operamos diretamente na `__cabeca` da lista.

---

## 💻 Como Executar

O projeto não requer nenhuma biblioteca externa, apenas Python 3.

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd SEU-REPOSITORIO
    ```
3.  Execute o arquivo `main.py`:
    ```bash
    python main.py
    ```
    *(ou `python3 main.py` dependendo da sua configuração)*

---

## 🌳 Lógica da Árvore de Triagem (Simplificada)

A árvore implementada segue a lógica simplificada fornecida na especificação do projeto:

```
O paciente está respirando?
├── Não ➔ [VERMELHO]
└── Sim
    └── Está consciente?
        ├── Não ➔ [LARANJA]
        └── Sim
            └── Está com dor intensa?
                ├── Sim ➔ [AMARELO]
                └── Não ➔ [VERDE]
```

---

## 📄 Licença

Este projeto é distribuído sob a licença MIT.
