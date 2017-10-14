# Exemplo de utilização do 'is'

letra = input("Digite a letra J: ")

if(letra is 'J'):
    print("Obrigado")
else:
    print("Desculpe você errou!")

letra = input("Digite a letra j: ")

if(letra is not 'j'):
    print("Desculpe você errou!")
else:
    print("Obrigado!")