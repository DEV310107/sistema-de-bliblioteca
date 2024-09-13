class Cliente:
    def __init__(self, nome, email, senha, telefone, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.cpf = cpf
        self.reservas = []

    def reservar_livro(self, livro):
        self.reservas.append(livro)

    def listar_reservas(self):
        return self.reservas


class Bibliotecario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def adicionar_livro(self, lista_livros, nome, genero, classificacao):
        livro = Livro(nome, genero, classificacao)
        lista_livros.append(livro)


class Livro:
    def __init__(self, titulo, genero, classificacao, reservado=False):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.reservado = reservado

    def reservar(self):
        self.reservado = True

    def __str__(self):
        return f"{self.titulo} - {self.genero} - Classificação: {self.classificacao} - Reservado: {'Sim' if self.reservado else 'Não'}"