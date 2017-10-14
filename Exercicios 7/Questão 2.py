__author__ = "Joselito Junior"
'''2. Escreva um Algoritmo que leia 10 valores, adicione-os em uma lista e em seguida utilize a
estrutura de repetic~ao while para exibir o numero do ndice e o valor do elemento.'''
def recebeValores():
    x = []
    for i in range(10):
        x.append(float(input("Digite o valor: ")))
    return x

i = 0
x = recebeValores()
while i < 10:
    print("Posição:", i, "Valores:", x[i])
    i += 1