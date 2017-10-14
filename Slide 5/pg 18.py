#Uso do continue e break

for numero in range(0, 11):
    if numero % 2 == 0:
        continue
    elif numero == 7:
        break

    print(numero)
print("Fim do laço")
