# 📝 Agenda de Contatos

Um projeto simples de **Agenda de Contatos** desenvolvido em Python, que permite ao usuário gerenciar sua lista de contatos de forma eficiente, onde toda a interação é realizada via terminal.

## 🎥 Demonstração

![Demonstração do Projeto](assets/agenda-demo.gif)

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **pickle**: Biblioteca padrão do Python para serialização e desserialização de objetos.
- **[questionary](https://github.com/tmbo/questionary)**: Biblioteca para criar prompts interativos e amigáveis, melhorando a experiência do usuário.
- **[rich](https://github.com/Textualize/rich)**: Biblioteca para criar saídas de texto mais ricas e estilizadas no terminal.

## ⚙️ Funcionalidades

- 📝 **Cadastro de Contatos**: Cadastre novos contatos, que serão armazenados em um arquivo `.pkl` usando a biblioteca `pickle`.
- 📖 **Exibição de Contatos**: Visualize todos os contatos cadastrados com informações como nome, telefone e email.
- ✏️ **Edição de Contatos**: Edite as informações de um contato existente.
- ⭐ **Favoritar Contatos**: Marque contatos como favoritos para fácil acesso.
- ❌ **Remoção de Contatos**: Permite deletar contatos, removendo-os também do arquivo `.pkl`.
- 🏃‍♂️ **Encerrar o Programa**: Selecione "Voltar" ou "Sair" para encerrar o programa. Os dados são preservados no arquivo `.pkl`.

## 📚 Bibliotecas Utilizadas

- **[os](https://docs.python.org/3/library/os.html)**: Módulo padrão do Python para interações com o sistema operacional.
- **[pickle](https://docs.python.org/3/library/pickle.html)**: Módulo padrão do Python para serialização e desserialização de objetos.
- **[questionary](https://github.com/tmbo/questionary)**: Biblioteca para criar prompts interativos no terminal.
- **[rich](https://github.com/Textualize/rich)**: Biblioteca para criar saídas de texto ricas e estilizadas no terminal.
  - `rich.console.Console`: Para exibir mensagens formatadas no terminal.
  - `rich.table.Table`: Para criar e exibir tabelas no terminal.
  - `rich.box`: Para customizar o estilo das bordas da tabela.

## ✅ Requisitos

- [<img src="https://skillicons.dev/icons?i=python&theme=dark" width="25" align="center">](https://www.python.org/) Python 3.8+

## 🚀 Como Rodar o Projeto

📌 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/python-agenda-contatos
