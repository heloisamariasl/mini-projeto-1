from classes import Doador, Produto, Doacao, Instituicao
from datetime import date

instituicao = Instituicao("Doacao")
doador = Doador("Ana", "81999999999")
instituicao.cadastrar_doador(doador)
produto = Produto("Arroz", 20, "kg", date(2027, 5, 10))
doacao = Doacao(doador, produto, date.today())
instituicao.registrar_doacao(doacao)
instituicao.relatorio()