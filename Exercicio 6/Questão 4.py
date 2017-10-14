__author__ = "Joselito Junior"

print("Time A:\n Torcedores = 80000\n Taxa de crescimento = 3%")
print("Time B:\n Torcedores = 200000\n Taxa de crescimento = 1,5%\n")
print("Levando em consideração as taxas de crescimento e a quantidade de tocedores atuais tem-se que:")

i = 0
a = 80000
b = 200000

while a < b:
    a += a * 0.03
    b += b * 0.015
    i += 1
print("- Em",i,"anos a torcida do time A será maior que a torcida do time B")