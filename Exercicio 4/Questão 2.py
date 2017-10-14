__author__ = "Joselito Junior"

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if((valor1 > valor2) & (valor1 > valor3)):
    print("O maior valor é: ", valor1)
elif((valor2 > valor1) & (valor2 > valor3)):
    print("O maior valor é: ", valor2)
elif((valor3 > valor2) & (valor3 > valor1)):
    print("O maior valor é: ", valor3)

if((valor1 < valor2) & (valor1 < valor3)):
    print("O valor menor é: ", valor1)
elif((valor2 < valor1) & (valor2 < valor3)):
    print("O valor menor é: ", valor2)
elif((valor3 < valor1) & (valor3 < valor2)):
    print("O valor menor é: ", valor3)