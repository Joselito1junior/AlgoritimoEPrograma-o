__author__ = "Joselito Junior"

def Saudacao(turno):
    if turno in "Mm":
        print("Bom dia")

    if turno in "Vv":
        print("Boa Tarde")

    if turno in "Nn":
        print("Boa Noite")

while True:
    turno = input("Digite o turno que você estuda:\n")

    if turno in "MmVvNn":
        Saudacao(turno)
    else:
        print("Valor Inválido")







