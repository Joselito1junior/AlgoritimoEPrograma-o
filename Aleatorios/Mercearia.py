#Programa de gerenciamento de uma mercearia, no entanto é necessário implementação do banco de dados para
#o software ser considerado funcional.

#   Listas Separadas de Nomes e Quantidades
#   Lista 1 - Cereais
#   Lista 2 - Legumes
#   Lista 3 - Higiêne Pessoal
#   Lista 4 - Outros
listaCereais = ["Milho","Arroz","Feijao"]
listaLegumes = ["Alface", "Batata", "Cebola"]
listaHigiene = ["Creme Dental", "Sabonete", "Desodorante"]
listaOutros = ["Pão", "Biscoito", "Mortadela"]

listaQuantCereais = [10,10,10]
listaQuantLegumes = [10,10,10]
listaQuantHigiene = [10,10,10]
listaQuantOutros = [10,10,10]

listaPrecoCereais = [10,10,10]
listaPrecoLegumes = [10,10,10]
listaPrecoHigiene = [10,10,10]
listaPrecoOutros = [10,10,10]


def adicionaProduto():
    sair = 0
    while sair != -1:
        categoriaProdutos()#Exibe a lista de categorias disponíveis
        opcao = int(input("Escolha um opcão ou digite -1 para voltar para o menu principal: "))
        if opcao == 1:
            addCereais()
        elif opcao == 2:
            addLegumes()
        elif opcao == 3:
            addHigienePessoal()
        elif opcao == 4:
            addOutros()
        elif opcao == -1:
            sair = opcao
        else:
            print("Digite um valor válido: \n")

def addCereais():
    cereal = input("Digite separados por virgula o nome, quantidade e preço do cereal que você deseja adicionar ao estoque: ")
    nome, quantidade, preco = cereal.split(",")

    listaCereais.append(nome)
    listaQuantCereais.append(int(quantidade))
    listaPrecoCereais.append(float(preco))

def addLegumes():
    legume = input("Digite separados por virgula o nome, quantidade e preço do legume que você deseja adicionar ao estoque: ")
    nome, quantidade, preco = legume.split(",")

    listaLegumes.append(nome)
    listaQuantLegumes.append(int(quantidade))
    listaPrecoLegumes.append(float(preco))

def addHigienePessoal():
    higiene = input("Digite separados por virgula o nome, quantidade e preço do item de Higiene que você deseja adicionar ao estoque: ")
    nome, quantidade, preco = higiene.split(",")
    listaHigiene.append(nome)
    listaQuantHigiene.append(int(quantidade))
    listaPrecoHigiene.append(float(preco))

def addOutros():
    outros = input("Digite separados por virgula o nome, quantidade e preço do item que você deseja adicionar ao estoque: ")
    nome, quantidade, preco = outros.split(",")

    listaOutros.append(nome)
    listaQuantOutros.append(int(quantidade))
    listaPrecoOutros.append(float(preco))

def veEstoque():
    i = 0
    lista1 = listaCereais + listaLegumes + listaHigiene + listaOutros
    lista2 = listaQuantCereais + listaQuantLegumes + listaQuantHigiene + listaQuantOutros
    print("Descrição | Qtd")
    while i < len(lista1):
        print(lista1[i],'|', lista2[i])
        i += 1
    print("")

def opcoesUsuario():
    print("Olá, Seja bem vindo! Tecle:")
    print("1 - Para adicionar um Produto")
    print("2 - Para ver o estoque")
    print("-1 - Para sair\n")

def categoriaProdutos():
    print("1 - Cereais")
    print("2 - Legumes")
    print("3 - Higiêne Pessoal")
    print("4 - Outros")

if __name__ == '__main__':

    sair = 0

    print("GERENCIADOR DE ESTOQUE\n")
    while sair != -1:
        opcoesUsuario()
        funcao = int(input("Qual função deseja realizar: "))
        print("")
        if funcao == 1:
            adicionaProduto()
        elif funcao == 2:
            veEstoque()
        elif funcao == -1:
            sair = -1
        else:
            print("Digite um valor válido")
