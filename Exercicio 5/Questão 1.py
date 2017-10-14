__author__ = "Joselito Junior"

letra = input("Digite um caractere: ")

if isdigit():
    print("Digite uma letra")
else:
    if letra in "aeiouAEIOU":
        print("É uma vogal")
    else:
        print("É uma consoante")