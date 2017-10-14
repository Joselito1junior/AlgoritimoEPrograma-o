__author__ = "Joselito Junior"

print("Cálculo da área e perímetro de um retângulo")

valor = input("Digite na ordem: base, altura (separados por vírgula): ")
base, altura = valor.split(",")

print("    Área é igual a: ", float(base) * float(altura))
print("    O Perímetro é: ", (2 * float(base)) + (2 * float(altura)))

input("Pressione a tecla ENTER para sair... ")
