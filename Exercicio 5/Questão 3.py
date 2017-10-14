__author__ = "Joselito Junior"

valor1 = float(input("Digite o valor do primeiro produto: "))
valor2 = float(input("Digite o valor do segundo produto: "))
valor3 = float(input("Digite o valor do terceiro produto: "))

if((valor1 < valor2) & (valor1 < valor3)):
    print("Compre o primeiro produto")
elif((valor2 < valor1) & (valor2 < valor3)):
    print("Compre o segundo produto")
else:
    print("Compre o terceiro produto")