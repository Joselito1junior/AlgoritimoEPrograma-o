__author__ = "Joselito Junior"

avaliacaoFinal = 0

print("Digite 1 para SIM e 0 para NÂO no questionário abaixo:")

resposta = int(input("Conversou com a vítima nos últimos 2 dias?:"))
avaliacaoFinal = avaliacaoFinal + 1 if resposta == 1 else  avaliacaoFinal + resposta
resposta = int(input("Esteve no lugar do crime?:"))
avaliacaoFinal = avaliacaoFinal + 1 if resposta == 1 else  avaliacaoFinal + resposta
resposta = int(input("Mora perto da vítima:"))
avaliacaoFinal = avaliacaoFinal + 1 if resposta == 1 else  avaliacaoFinal + resposta
resposta = int(input("Pegou dinheiro emprestado com a vítima:"))
avaliacaoFinal = avaliacaoFinal + 1 if resposta == 1 else  avaliacaoFinal + resposta
resposta = int(input("Já trabalhou com a vítima:"))
avaliacaoFinal = avaliacaoFinal + 1 if resposta == 1 else  avaliacaoFinal + resposta


if avaliacaoFinal == 5:
    print("Assassino")
elif avaliacaoFinal >= 3 and avaliacaoFinal <=4:
    print("Cúmplice")
elif avaliacaoFinal == 2:
    print("Suspeito")
else:
    print("Inocente")

