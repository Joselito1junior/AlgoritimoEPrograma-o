__autor__ = "Joselito Junior"

salario = float(input("Digite quanto você ganha: "))
Horas = input("Digite quantas horas você trabalha por mês: ")

impostoDeRenda = salario * 0.11
INSS = salario * 0.08
sindicato = salario * 0.05
valorLiquido = salario - (impostoDeRenda + INSS + sindicato)



print("Salario bruto =  ", salario)
print("Descontos")
print("    Imposto de Renda: ", impostoDeRenda)
print("    INSS: ", INSS)
print("    Sindicato: ", sindicato)
print("    Salario Liquido: ", valorLiquido)

print("Pressione ENTER para sair...")
input()