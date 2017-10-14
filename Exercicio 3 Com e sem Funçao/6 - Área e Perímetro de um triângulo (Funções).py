__author__ = "Joselito Junior"

def area(base, altura):
    return (float(base) * float(altura))

def perimetro(base, altura):
    return (2 * float(base)) + (2 * float(altura))

print("Cálculo da área e perímetro de um retângulo")

valor = input("Digite na ordem: base, altura (separados por vírgula): ")
base, altura = valor.split(",")


print("    Área é igual a: ", area(base, altura))
print("    O Perímetro é: ", perimetro(base, altura))

input("Pressione a tecla ENTER para sair... ")
