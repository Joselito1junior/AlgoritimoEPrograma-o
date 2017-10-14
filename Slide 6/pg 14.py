listaNomes = ["Jose", "Maria", "Marcos", "Pedro"]
print('1',listaNomes)
listaNomes += ["João", "Matheus"] #Adiciona nomes
print('2',listaNomes)
listaNomes.append("Adriana")# insere um valor no ultimo indice
print('3',listaNomes)
listaNomes.insert(4, "Sávio")# insere um valor no indice solicitado
print('4',listaNomes)
listaNomes.pop()# Exclui o ultimo item da lista
print('5',listaNomes)
listaNomes.pop(4)# Exclui o valor dentro do indice indicado dentro dos parêntesis
print('6',listaNomes)
#del(listaNomes[0])# Remove o valor do indice indicado dentro dos cochetes
print('7',listaNomes)
#del(listaNomes[2:5])# Remove o valor no intevalo indicado dentro do indice que está dentro dos cochetets
print('8',listaNomes)
#listaNomes.clear()
print('9',listaNomes)
listaNomes.sort(reverse=True)
print('10',listaNomes)

#for indice, pessoa in enumerate(listaNomes):
#    print("Posição:", indice, "Pessoa: ", pessoa)