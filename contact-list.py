import os
import pickle
import questionary
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_contatos(contatos):
    with open("contatos.pkl", "wb") as f:
        pickle.dump(contatos, f)

def carregar_contatos():
    if os.path.exists("contatos.pkl"):
        with open("contatos.pkl", "rb") as f:
            return pickle.load(f)
    return []

contatos = carregar_contatos()

def solicitar_dados_contato():
    nome = ""
    while not nome:
        nome = questionary.text("Digite o nome do contato:").ask()
        if not nome:
            console.print("O campo nome não pode estar vazio!", style="red")

    telefone = ""
    while not telefone:
        telefone = questionary.text("Digite o telefone:").ask()
        if not telefone:
            console.print("O campo telefone não pode estar vazio!", style="red")

    email = ""
    while not email:
        email = questionary.text("Digite o email:").ask()
        if not email:
            console.print("O campo email não pode estar vazio!", style="red")

    return nome, telefone, email

def adicionar_contato(contatos):
    nome, telefone, email = solicitar_dados_contato()
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    salvar_contatos(contatos)
    console.print(f"\nContato {nome} adicionado com sucesso!", style="green")
    
    cadastrar_mais = questionary.confirm("Deseja cadastrar mais contatos?").ask()
    if cadastrar_mais:
        clear()
        adicionar_contato(contatos)

def visualizar_contatos(contatos):
    if not contatos:
        console.print("Nenhum contato cadastrado.", style="red")
        input("\nPressione Enter para voltar...")
        return
    
    table = Table(title="Lista de Contatos", box=box.SIMPLE)

    table.add_column("Nome", justify="left", style="cyan")
    table.add_column("Telefone", justify="center", style="magenta")
    table.add_column("Email", justify="right", style="green")
    table.add_column("Favorito", justify="center", style="yellow")

    for contato in contatos:
        favorito = "⭐" if contato["favorito"] else ""
        table.add_row(contato["nome"], contato["telefone"], contato["email"], favorito)

    console.print(table)
    input("\nPressione Enter para voltar...")

def visualizar_contatos_favoritos(contatos):
    if not any(contato["favorito"] for contato in contatos):
        console.print("Não há contatos marcados como favorito.", style="red")
        input("\nPressione Enter para voltar...")
        return
    
    table = Table(title="Contatos Favoritos", box=box.SIMPLE)

    table.add_column("Nome", justify="left", style="cyan")
    table.add_column("Telefone", justify="center", style="magenta")
    table.add_column("Email", justify="right", style="green")
    table.add_column("Favorito", justify="center", style="yellow")

    for contato in contatos:
        if contato["favorito"]:
            table.add_row(contato["nome"], contato["telefone"], contato["email"], "⭐")

    console.print(table)
    input("\nPressione Enter para voltar...")

def editar_contato(contatos):
    if not contatos:
        console.print("Nenhum contato cadastrado.", style="red")
        input("\nPressione Enter para voltar...")
        return
    tabela_contatos(contatos)
    nomes = [contato["nome"] for contato in contatos] + ["<< Voltar"]
    nome_selecionado = questionary.select("Selecione o contato que deseja editar:", choices=nomes).ask()

    if nome_selecionado == "<< Voltar":
        return

    for contato in contatos:
        if contato["nome"] == nome_selecionado:
            novo_nome = questionary.text("Novo nome (pressione Enter para manter):", default=contato["nome"]).ask()
            novo_telefone = questionary.text("Novo telefone (pressione Enter para manter):", default=contato["telefone"]).ask()
            novo_email = questionary.text("Novo email (pressione Enter para manter):", default=contato["email"]).ask()

            contato["nome"] = novo_nome if novo_nome else contato["nome"]
            contato["telefone"] = novo_telefone if novo_telefone else contato["telefone"]
            contato["email"] = novo_email if novo_email else contato["email"]

            salvar_contatos(contatos)
            console.print("\nContato atualizado:", style="cyan")
            console.print(f"Nome: {contato['nome']}", style="green")
            console.print(f"Telefone: {contato['telefone']}", style="green")
            console.print(f"Email: {contato['email']}", style="green")
            input("\nPressione Enter para voltar...")
            break

def favoritar_contato(contatos):
    if not contatos:
        console.print("Nenhum contato disponível para favoritar.", style="red")
        input("\nPressione Enter para voltar...")
        return
    
    tabela_contatos(contatos)

    escolhas = [f"{index + 1}. {contato['nome']}" for index, contato in enumerate(contatos)] + ["<< Voltar"]
    index_selecionado = questionary.select(
        "Selecione o contato (use as setas para navegar):",
        choices=escolhas,
        use_arrow_keys=True
    ).ask()

    if index_selecionado == "<< Voltar":
        return

    index = int(index_selecionado.split('.')[0]) - 1
    contato_selecionado = contatos[index]
    contato_selecionado["favorito"] = not contato_selecionado["favorito"]
    status = "marcado" if contato_selecionado["favorito"] else "desmarcado"
    
    console.print(f"Contato {status} como favorito: {contato_selecionado['nome']}", style="green")
    salvar_contatos(contatos)

    input("\nPressione Enter para voltar...")

def deletar_contato(contatos):
    if not contatos:
        console.print("Nenhum contato cadastrado.", style="red")
        input("\nPressione Enter para voltar...")
        return
    tabela_contatos(contatos)
    nomes = [contato["nome"] for contato in contatos] + ["<< Voltar"]
    nome_selecionado = questionary.select("Selecione o contato que deseja deletar:", choices=nomes).ask()

    if nome_selecionado == "<< Voltar":
        return

    for contato in contatos:
        if contato["nome"] == nome_selecionado:
            contatos.remove(contato)
            salvar_contatos(contatos)
            console.print(f"Contato {contato['nome']} deletado com sucesso!", style="red")
            input("\nPressione Enter para voltar...")
            break

def tabela_contatos(contatos):
    table = Table(title="Contatos", box=box.SIMPLE)

    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Nome", justify="left", style="cyan")
    table.add_column("Telefone", justify="center", style="magenta")
    table.add_column("Email", justify="right", style="green")
    table.add_column("Favorito", justify="center", style="yellow")

    for index, contato in enumerate(contatos):
        favorito = "⭐" if contato["favorito"] else ""
        table.add_row(str(index + 1), contato["nome"], contato["telefone"], contato["email"], favorito)

    console.print(table)

def menu_opcoes():
    opcoes = [
        '➕ Adicionar Contato',
        '📖 Visualizar Lista de Contatos',
        '✏️  Editar Contato',
        '⭐ Marcar/Desmarcar como Favorito',
        '🌟 Visualizar Contatos Favoritos',
        '❌ Apagar Contato',
        '🚪 Sair'
    ]
    return questionary.select("📋 Lista de Contatos", choices=opcoes).ask()

while True:
    clear()
    opcao = menu_opcoes()

    clear()
    if 'Adicionar Contato' in opcao:
        console.print("Novo Contato", style="green")
        adicionar_contato(contatos)
    elif 'Visualizar Lista de Contatos' in opcao:
        visualizar_contatos(contatos)
    elif 'Editar Contato' in opcao:
        editar_contato(contatos)
    elif 'Marcar/Desmarcar como Favorito' in opcao:
        favoritar_contato(contatos)
    elif 'Visualizar Contatos Favoritos' in opcao:
        visualizar_contatos_favoritos(contatos)
    elif 'Apagar Contato' in opcao:
        deletar_contato(contatos)
    elif 'Sair' in opcao:
        console.print("Saindo do programa. Até logo!", style="red")
        break
