#Ex1
marcas_carros = {"fiat", "chevrolet", "honda"}

#adicionando um elemento por vez
marcas_carros.add("hyundai")
marcas_carros.add("ferrari")
print(marcas_carros)

marcas_carros.update(["volvo, BMW"])
print(marcas_carros)

#Ex2
tipoCarro = set()

tipoCarro.add("Sedâ")
tipoCarro.add("Pick up")

print(tipoCarro)

#Ex3
conjuntoSimples = set(['a', 'b'])

conjuntoSimples.remove('c')
conjuntoSimples.discard('d')
print(conjuntoSimples)