__author__ = "Joselito Junior"

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if(media < 4):
    print("Reprovado")
elif((media >= 4) & (media < 7)):
    print("Você está na final")
else:
    print("Aprovado")





