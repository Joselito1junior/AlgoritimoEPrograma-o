nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2

situacao = 'Aprovado' if media >=7 else 'Reprovado'

print('Sua média é {0} e você está {1}'.format(media, situacao))

                    
