__author__= "Joselito Junior"

#Função responsável pela soma
def somar(valor1, valor2):
    return float(valor1) + float(valor2)
#Fim da função somar

valor = input("informe os dois valores separados por virgula para que seja feita a soma: ")
valor1, valor2 = valor.split(",")

print("O resultado da soma é: ", somar(valor1, valor2))
print("Pressione ENTER para sair...")
input()
