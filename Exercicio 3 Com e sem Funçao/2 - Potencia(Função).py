__author__= "Joselito Junior"

#Função responsável pela potencia
def potencia(valor1, valor2):
    return float(valor1) ** float(valor2)
#Fim da função potencia

valor = input("informe os dois valores separados por virgula para que seja feita a soma: ")
valor1, valor2 = valor.split(",")

print("O resultado da potenciação é: ", potencia(valor1, valor2))
input("Pressione a ENTER para sair...")
