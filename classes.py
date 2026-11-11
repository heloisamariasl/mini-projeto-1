from datetime import date


class Doador:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")


class Empresa(Doador):
    def __init__(self, nome, telefone, cnpj):
        super().__init__(nome, telefone)
        self.cnpj = cnpj

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"CNPJ: {self.cnpj}")


class Produto:
    def __init__(self, nome, quantidade, medida, validade):
        self.nome = nome
        self.quantidade = quantidade
        self.medida = medida
        self.validade = validade

    def exibir_dados(self):
        print(f"Produto: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Medida: {self.medida}")
        print(f"Validade: {self.validade}")


class Doacao:
    def __init__(self, doador, produto, data_doacao):
        self.doador = doador
        self.produto = produto
        self.data_doacao = data_doacao

    def exibir_dados(self):
        print(f"Doador: {self.doador.nome}")
        print(f"Produto: {self.produto.nome}")
        print(f"Quantidade: {self.produto.quantidade} {self.produto.medida}")
        print(f"Data da Doação: {self.data_doacao}")


class Estoque:
    def __init__(self):
        self.produtos = []  #lista para armazenar os produtos no estoque

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def retirar_produto(self, produto, quantidade):
        if produto in self.produtos:
            if quantidade <= produto.quantidade:
                produto.quantidade -= quantidade

                if produto.quantidade == 0:
                    self.produtos.remove(produto)
            else:
                print("Quantidade insuficiente no estoque.")
        else:
            print("Produto não encontrado no estoque.")

    def listar_produtos(self):
        for produto in self.produtos:
            produto.exibir_dados()

    def verificar_validade(self):
        data_atual = date.today()
        produtos_vencidos = []

        for produto in self.produtos:
            if produto.validade < data_atual:
                produtos_vencidos.append(produto)

        return produtos_vencidos


class Instituicao:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = Estoque()
        self.doadores = []
        self.historico_doacoes = []

    def cadastrar_doador(self, doador):
        self.doadores.append(doador)

    def registrar_doacao(self, doacao):
        self.historico_doacoes.append(doacao)
        self.estoque.adicionar_produto(doacao.produto)

    def distribuicao(self, produto, quantidade):
        self.estoque.retirar_produto(produto, quantidade)

    def relatorio(self):
        print(f"Relatório da Instituição: {self.nome}")

        print("Doadores:")
        for doador in self.doadores:
            doador.exibir_dados()
            print()

        print("Produtos no Estoque:")
        self.estoque.listar_produtos()
        print()

        print("Histórico de Doações:")
        for doacao in self.historico_doacoes:
            doacao.exibir_dados()
            print()