__author__ = "Joselito Junior"

def calculo(valor1, valor2, operacao):
    if operacao == '1':
        if valor1 >= 0:
            if valor2 >= 0:
                return "Os valores são positivos"
            else:
                return "Apenas o valor 2 é negativo"
        elif valor2 >= 0:
            return "Apenas o valor 1 é negativo"
        else:
            return "Ambos valores são negativos"

    elif operacao == '2':
        if valor1 % 2 == 0:
            if valor2 % 2 == 0:
                return "Ambos valores são pares"
            else:
                return "Apenas o valor 1 é par"
        elif valor2 % 2 == 0:
            return "Apenas o valor 2 é par"
        else:
            return "Ambos valores são ímpares"


    elif operacao == '3':
        return valor1 + valor2
    elif operacao == '4':
        return valor1 - valor2
    elif operacao == '5':
        return valor1 * valor2
    elif operacao == '6':
        return valor1 / valor2

while True:
    valor = input("Digite dois valores separados por vírgula:\n ")
    valor1, valor2 = valor.split(",")

    operacao = input("Digite o número correspondente a opção que você deseja:\n 1- Deseja saber se o número é positívo?\n 2- Deseja saber se o número é negativo?\n 3- Somar\n 4- Subtrair\n 5- Multiplicar\n 6- Dividir\n")

    resultado = calculo(float(valor1),float(valor2),operacao)

    print(resultado)