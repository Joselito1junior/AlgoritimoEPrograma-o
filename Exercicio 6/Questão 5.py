__author__ = "Joselito Junior"

print("Software que compara a taxa de crescimento e o numero de tocedores de dois times")
print("Informe as taxas de crescimento e o número de torcedores de cada timee")

aTorc = float(input("digite o número de torcedores do time A: "))
aTaxa = float(input("digite a taxa de crescimento do time A: "))
bTorc = float(input("digite o número de torcedores do time B: "))
bTaxa = float(input("digite a taxa de crescimento do time B: "))

print("Time A:\n Torcedores =", aTorc, "\n Taxa de crescimento =", aTaxa,'%')
print("Time B:\n Torcedores =", bTorc, "\n Taxa de crescimento =", bTaxa,'%')
print("Levando em consideração as taxas de crescimento e a quantidade de tocedores atuais tem-se que:")

aTaxa = aTaxa * 0.01
bTaxa = bTaxa * 0.01

if aTorc < bTorc:
    i = 0
    while aTorc < bTorc:
        aTorc += aTorc * aTaxa
        bTorc += bTorc * bTaxa
        i += 1
    print("- Em",i,"anos a torcida do time A será maior que a torcida do time B")

elif aTorc > bTorc:
    i = 0
    while aTorc > bTorc:
        aTorc += aTorc * aTaxa
        bTorc += bTorc * bTaxa
        i += 1
    print("- Em",i,"anos a torcida do time B será maior que a torcida do time A")

print("Torcida do Time A = ",int(aTorc))
print("Torcida do Time B = ", int(bTorc))