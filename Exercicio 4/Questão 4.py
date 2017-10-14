__author__ = "Joselito Junior"

ano = float(input("Digite um ano: "))

if((ano % 4) == 0):
    if((ano % 100) != 0):              #Verifica se o ano termina em 00
        print("Esse ano é bissexto")
    elif((ano % 400) == 0):
        print("Esse ano é bissexto")
    else:
        print("Esse ano não é bissexto")
else:
    print("Esse ano não é bissexto")