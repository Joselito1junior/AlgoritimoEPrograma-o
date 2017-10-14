__author__ = "Joselito Junior"

i = 0

def Verifica(valor):
    if valor >= 0 and valor <= 10:
        print("Obrigado")
        return 1
    else:
        print("Digite novamente!")
        return 0

while i == 0:
    valor = float(input("Digite um valor entre 0 e 10: "))
    i = Verifica(valor)