__author__ = "Joselito Junior"

#valor = input("Digite dois números inteiros separados por virgula:\n")
#valor1, valor2 = valor.split(',')

valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))


if valor1 < valor2:
    while valor1 < valor2:
        valor1 += 1
        print(valor1)

if valor2 < valor1:
    while valor2 < valor1:
        valor2 += 1
        print(valor2)



