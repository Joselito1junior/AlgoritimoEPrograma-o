__autor__ = "Joselito Junior"

#Função responsável pela conversão
def conversao(valor):
    return float(KM) * 1.6
#Fim da função conversão

KM = input("Informe o valor me KM para que seja convertido em Milhas: ")

print("O valor convertido em Milhas é: ", conversao(KM))
input("Pressione ENTER para sair...")

