__author__="Joselito Junior"

valor = input("informe os dois valores separados por virgula para que seja feita a soma: ")

valor1, valor2 = valor.split(",")

print("O resultado da soma é: ", float(valor1) + float(valor2))
print("Pressione ENTER para sair...")
input()
