__author__ = "Joselito Junior"

sair = 0

def nomeUser(nome):
    return 1 if len(nome) > 3 else 0

def idadeUser(idade):
    return 1 if idade > 0 and idade < 120 else 0

def salarioUser(salario):
    return 1 if salario > 0 else 0

def sexoUser(sexo):
    return 1 if sexo is 'F' or sexo is 'M' else 0

def estadoUser(civil):
    return 1 if civil is 'S' or civil is 'C' or civil is 'V' or civil is 'D' else 0

while sair != 1:
    nome = input("Digite seu nome: ")
    sair = nomeUser(nome)

sair = 0
while sair != 1:
    idade = int(input("Digite sua idade: "))
    sair = idadeUser(idade)

sair = 0
while sair != 1:
    salario = int(input("Digite seu salário: "))
    sair = salarioUser(salario)

sair = 0
while sair != 1:
    sexo = input("Digite M para sexo masculino e F para sexo Feminino: ")
    sair = sexoUser(sexo)

sair = 0
while sair != 1:
    civil = input("Digite o estado civil\n S - Solteiro\n C - Casado\n V - Outros\n D - Divorciado \n")
    sair = estadoUser(civil)

print("Valeu Pai")