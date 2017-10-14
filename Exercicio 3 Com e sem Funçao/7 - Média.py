__author__ = "Joselito Junior"

print("Este programa faz o cálculo da média de 3 valores")
notas = input("Digite os três valores na oredem: nota1, nota2, nota3 (separados por vígula): ")

nota1, nota2, nota3 = notas.split(",")
print("		O valor da média é: ", (float(nota1) + float(nota2) + float(nota3)) / 3)

input("Pressione ENTER para sair...")