# Sistema Bancário com Programação Orientada a Objetos 🐍🏦

Este repositório contém a resolução do desafio de codificação do bootcamp **Luizalabs - Back-end com Python**. O objetivo é migrar um sistema bancário funcional de uma estrutura de dicionários para um modelo robusto de **Programação Orientada a Objetos (POO)**.

## 📌 Objetivo do Desafio
Atualizar a implementação do sistema bancário para armazenar dados de clientes e contas bancárias em objetos, seguindo rigorosamente o modelo de classes UML fornecido.

## 🏗️ Arquitetura e Conceitos Aplicados
Para garantir a organização e escalabilidade, o projeto foi estruturado utilizando pacotes (modules), aplicando os pilares da POO:

- **Encapsulamento:** Uso de atributos privados (`_saldo`, `_historico`) e propriedades (`@property`).
- **Herança:** Implementação de `PessoaFisica` herdando de `Cliente` e `ContaCorrente` herdando de `Conta`.
- **Abstração:** Uso da classe base abstrata (`ABC`) para a interface `Transacao`.
- **Polimorfismo:** O método `sacar` possui comportamentos distintos entre a classe base e a classe filha.
- **Composição & Agregação:** Relação estruturada entre Clientes, Contas e seus respectivos Históricos.

## 📂 Estrutura de Pastas
```text
.
├── main.py                 # Ponto de entrada e interface com o usuário
├── README.md               # Documentação do projeto
└── modelos/                # Pacote de domínio do sistema
    ├── __init__.py         # Inicialização do pacote
    ├── cliente.py          # Classes Cliente e PessoaFisica
    ├── conta.py            # Classes Conta e ContaCorrente
    ├── historico.py        # Gestão de logs de transações
    └── transacao.py        # Interface e implementações de Deposito e Saque
```

## 🛠️ Tecnologias Utilizadas

* **Python 3.14+**
* **Biblioteca ABC** (Abstract Base Classes) para interfaces.
* **Módulo Datetime** para registro de logs.
* **Git/GitHub** para versionamento.

## 🚀 Como Executar

1. Certifique-se de ter o **Python** instalado em sua máquina.
2. No terminal, navegue até a pasta raiz do projeto.
3. Execute o comando:

```bash
python main.py
```
