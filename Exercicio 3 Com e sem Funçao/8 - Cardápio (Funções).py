__author__ = "Joselito Junior"

def total(hamburger, batataFritas, milkshake):
    return ((float(hamburger) * 10) + (float(batataFritas) * 8) + (float(milkshake) * 16))

print("Programa que calcula do valor consumido pelo cliente no restaurante")
print("")
hamburger = input("Digite a quantidade de Hambúrger: ")
batataFritas = input("Digite a quantidade de Batata Fritas: ")
milkshake = input("Digite a quantidade de Milkshake: ")
print("")
print("	O valor total é: ", total(hamburger, batataFritas, milkshake))
print("")
input("Pressione ENTER para sair...")
