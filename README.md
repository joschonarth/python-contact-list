# 📝 Agenda de Contatos

Um projeto simples de **Agenda de Contatos** desenvolvido em Python, que permite ao usuário gerenciar sua lista de contatos de forma eficiente, onde toda a interação é realizada via terminal.

## 🎥 Demonstração

<div align="center">

https://github.com/user-attachments/assets/1d07d22c-d4e8-4c8a-9786-f407f4918793

</div>

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **[pickle](https://docs.python.org/3/library/pickle.html)**: Biblioteca padrão do Python para serialização e desserialização de objetos.
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
- **[prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)**: Biblioteca que fornece ferramentas para criar interfaces de linha de comando interativas.
- **[rich](https://github.com/Textualize/rich)**: Biblioteca para criar saídas de texto ricas e estilizadas no terminal.
  - `rich.console.Console`: Para exibir mensagens formatadas no terminal.
  - `rich.table.Table`: Para criar e exibir tabelas no terminal.
  - `rich.box`: Para customizar o estilo das bordas da tabela.

## ✅ Requisitos

- [<img src="https://skillicons.dev/icons?i=python&theme=dark" width="25" align="center">](https://www.python.org/) Ter o Python instalado

## 🚀 Como Rodar o Projeto

📌 1. Clone o repositório:

```bash
git clone https://github.com/joschonarth/python-contact-list
```

📌 2. Navegue até o diretório do projeto:

```bash
cd python-contact-list
```

📌 3. Instale as bibliotecas:

```bash
pip install prompt_toolkit questionary rich
```

📌 4. Execute o programa:

```bash
python agenda.py
```

## 📂 Estrutura do Projeto

* **`agenda.py`**: Arquivo principal que executa o programa.
* **`contatos.pkl`**: Arquivo onde os contatos são armazenados em formato de objeto serializado com `pickle`.

## Contribuições 🌟

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue com sugestões ou enviar um pull request com melhorias.


## 📜 Licença 

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📞 Contato 

<div>
    <a href="https://www.linkedin.com/in/joschonarth/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href="mailto:joschonarth@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>
