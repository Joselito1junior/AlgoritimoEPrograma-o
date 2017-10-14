__author__= "Joselito Junior"

#Função responsável pela potencia
def conversao(valor1, valor2):
    return (float(valor1) * 60) + float(valor2)
#Fim da função potencia

valor = input("informe os dois valores, minutos e segundos separados por virgula: ")
valor1, valor2 = valor.split(",")

print("O resultado da conversão é: ", conversao(valor1, valor2))
input("Pressione a ENTER para sair...")
