#O programa pede também o ano atual para que seja calculado o resultado.

__author__  = "Joselito Junior"

nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
ano = float(input("Digite o ano atual: "))

ano100 = (100 - idade) + ano

print('{0} completará 100 anos em {1}'.format(nome, ano100))
