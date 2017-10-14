__autor__ = "Joselito Junior"


####################
#Funções de calculos
def impostoDeRenda(salario):
    return salario * 0.11

def INSS(salario):
    return salario * 0.08
    

def sindicato(salario): 
    return salario * 0.05
     

def valorLiquido(salario):
    impostoDeRenda = salario * 0.11
    INSS = salario * 0.08
    sindicato = salario * 0.05
    return (salario - (impostoDeRenda + INSS + sindicato))
     
#Fim das funções de calculos
############################

salario = float(input("Digite quanto você ganha: "))
Horas = input("Digite quantas horas você trabalha por mês: ")

print("Salario bruto =  ", salario)
print("    Imposto de Renda: ", impostoDeRenda(salario))
print("    INSS: ", INSS(salario))
print("    Sindicato: ", sindicato(salario))
print("    Valor Liquido: ", valorLiquido(salario))


print("Pressione ENTER para sair...")
input()
