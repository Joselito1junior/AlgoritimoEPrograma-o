__author__ = "Joselito Junior"

def Alcool(litros):
    if litros <= 20:
        return (2.98 - (2.98 * 0.03)) * litros
    else:
        return (2.98 - (2.98 * 0.05)) * litros

def Gasolina(litros):
    if litros <= 20:
        return (3.79 - (3.79 * 0.04)) * litros
    else:
        return (3.79 - (3.79 * 0.06)) * litros

#inicio da função principal
while True:
    tipo = input("Digite a o tipo de combustível\n G - para Gasolina \n A - para Álcool\n ")
    litros = float(input("Digite a quantidade em litros:\n"))

    if tipo is 'A':
        total = Alcool(litros)
        print("Você deve pagar por essa quantidade de Álcool: R$", total)

    if tipo is 'G':
        total = Gasolina(litros)
        print("Você deve pagar por essa quantidade de Gasolina : R$", total)
    print("________________________________________________________________\n")