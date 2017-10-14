__author__="Joselito Junior"

valor = input("informe os dois valores, minutos e segundos separados por virgula: ")

valor1, valor2 = valor.split(",")

print("Esse tempo é composto por: ", (float(valor1) * 60) + float(valor2))
print("Pressione ENTER para sair...")

input()
