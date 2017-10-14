__author__ = "Joselito Junior"
#Escreva um Algoritmo que leia 10 valores, adicione-os em uma lista e em seguida utilize a
#estrutura de repetição for para exibir o numero do ndice e o valor do elemento.

def recebeValores():
    x = []
    for i in range(10):
        x.append(float(input("Digite o valor: ")))
    return x

x = recebeValores()
for i, x in enumerate(x):
    print("Posição:", i, "Valores:", x)
