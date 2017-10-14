__author__ = "Joselito Junior"

i = 0

def confereDados(nome, senha):
    return 1 if nome != senha else 0

while i == 0:
    nome = input("Digite seu nome de usuário:\n")
    senha = input("Digite uma senha diferente do nome de usuário:\n")
    i = confereDados(nome, senha) # sai do loop caso o valor retornado seja 1
    if i == 0:
        print("DIGITE UMA SENHA DIFERENTE DO NOME DE USUÁRIO!")

print("Obrigado")



