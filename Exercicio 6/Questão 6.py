__author__ = "Joselito Junior"

listaNum = [0]

i = 0

while i <= 19:
    i += 1
    listaNum.insert(i,i)

i = 0
while i <= 19:
    print(listaNum[i])
    i += 1
print(listaNum)