
# ConectaDoação

O **ConectaDoação** é um gerenciador de doações de alimentos desenvolvido em Python utilizando Programação Orientada a Objetos (POO) para o mini projeto da trilha UFPE.

O projeto tem como objetivo auxiliar instituições sociais e ONGs no controle de doações recebidas, no acompanhamento dos alimentos disponíveis em estoque e na organização da distribuição desses produtos, por meio de uma estrutura simples e clara.

## 💡 Problema

Instituições que recebem doações de alimentos precisam organizar informações sobre os doadores, os produtos recebidos, as quantidades disponíveis e as datas de validade.

Quando esse controle é feito manualmente, podem ocorrer dificuldades para acompanhar o estoque, consultar o histórico de doações e identificar produtos próximos ou além da validade.

O ConectaDoação busca facilitar esse gerenciamento por meio de um sistema simples e organizado.

## ⚙️ Funcionalidades

- Cadastro de doadores;
- Cadastro de empresas doadoras;
- Registro de doações;
- Controle de estoque de alimentos;
- Retirada de produtos do estoque;
- Verificação de produtos vencidos;
- Consulta ao histórico de doações;
- Geração de relatório da instituição.

## 📁 Organização dos arquivos

```text
DoaFacil/
│
├── .gitignore   # Ignora o pycache 
├── classes.py   # Classes e funcionalidades do sistema
├── main.py      # Arquivo principal para executar o programa
└── README.md    # Documentação do projeto
```

### Sobre as classes

O projeto utiliza as seguintes classes:

| Classe | Responsabilidade |
|---|---|
| `Doador` | Armazena os dados dos doadores. |
| `Empresa` | Representa uma empresa doadora, herdando características de `Doador`. |
| `Produto` | Armazena informações dos alimentos, como nome, quantidade, unidade de medida e validade. |
| `Doacao` | Registra informações sobre uma doação, incluindo o doador, o produto e a data. |
| `Estoque` | Gerencia os produtos disponíveis, permitindo adicionar, retirar e consultar alimentos. |
| `Instituicao` | Centraliza o gerenciamento dos doadores, das doações e do estoque. |

## 🚀 Como executar

### 1. Pré-requisitos

- Python 3 instalado;
- Um editor de código, como VS Code.

O projeto utiliza apenas recursos da biblioteca padrão do Python.

### 2. Baixar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd DoaFacil
```

### 3. Executar

No terminal, execute:

```bash
python3 main.py
```

## 🛠️ Tecnologias utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Git e GitHub

