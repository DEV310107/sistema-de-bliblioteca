# funcoes.py

from classe import Cliente, Bibliotecario, Livro

bibliotecario_senha_padrao = "Adm110211"  # senha predefinida para bibliotecário

lista_livros = [
    Livro("Harry Potter e a Pedra Filosofal", "Fantasia", "10+"),
    Livro("Jogos Vorazes", "Distopia", "14+"),
    Livro("O Hobbit", "Fantasia", "12+"),
    Livro("A Culpa é das Estrelas", "Romance/Drama", "12+"),
    Livro("Percy Jackson e o Ladrão de Raios", "Fantasia", "10+"),
    Livro("O Código Da Vinci", "Mistério", "16+"),
    Livro("Cinquenta Tons de Cinza", "Romance/Erótico", "18+"),
    Livro("Extraordinário", "Drama", "Livre")
]

clientes = []


def linha():
    print('════════════════════════════════════════════════ ♦️')


def main():
    linha()
    print("BIBLIOTECA SENAI")
    linha()
    print("1 - CADASTRAR         2 - LOGIN")
    linha()
    escolha = int(input("Qual opção deseja? \n--> "))
    return escolha


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    
    cliente = Cliente(nome, email, senha, telefone, cpf)
    clientes.append(cliente)
    print("Cadastro realizado com sucesso!")
    return cliente


def login():
    email = input("Email: ")
    senha = input("Senha: ")

    # Verifica se é o bibliotecário
    if email == "admin@biblioteca.com" and senha == bibliotecario_senha_padrao:
        print("Login bibliotecário bem-sucedido!")
        return Bibliotecario(email, senha), "bibliotecario"

    # Verifica se é um cliente
    for cliente in clientes:
        if cliente.email == email and cliente.senha == senha:
            print(f"Bem-vindo(a), {cliente.nome}!")
            return cliente, "cliente"

    print("Email ou senha incorretos.")
    return None, None


def listar_livros_disponiveis():
    print("Livros disponíveis:")
    for livro in lista_livros:
        if not livro.reservado:
            print(livro)


def adicionar_livro(bibliotecario):
    nome = input("Nome do livro: ")
    genero = input("Gênero: ")
    classificacao = input("Classificação: ")
    bibliotecario.adicionar_livro(lista_livros, nome, genero, classificacao)
    print("Livro adicionado com sucesso!")


def cliente_opcoes(cliente):
    linha()
    print("1 - Reservar Livro    2 - Ver Reservas    3 - Sair")
    linha()
    opcao = int(input("Qual opção deseja? \n--> "))

    if opcao == 1:
        listar_livros_disponiveis()
        livro_nome = input("Digite o nome do livro para reservar: ")

        for livro in lista_livros:
            if livro.titulo == livro_nome and not livro.reservado:
                cliente.reservar_livro(livro)
                livro.reservar()
                print(f"Você reservou o livro: {livro.titulo}")
                return

        print("Livro não encontrado ou já reservado.")
    
    elif opcao == 2:
        reservas = cliente.listar_reservas()
        if reservas:
            print("Seus livros reservados:")
            for livro in reservas:
                print(livro)
        else:
            print("Você não possui livros reservados.")
    
    elif opcao == 3:
        return


def bibliotecario_opcoes(bibliotecario):
    while True:
        linha()
        print("1 - Adicionar Livro    2 - Listar Livros Disponíveis    3 - Sair")
        linha()
        opcao = int(input("Qual opção deseja? \n--> "))

        if opcao == 1:
            adicionar_livro(bibliotecario)
        elif opcao == 2:
            listar_livros_disponiveis()
        elif opcao == 3:
            break