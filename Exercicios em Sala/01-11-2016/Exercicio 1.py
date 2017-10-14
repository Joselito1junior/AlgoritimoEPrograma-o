listaNome = ["jose", "jose", "jose", "israel", "israel", "lucas", "jose"]
listaTelefone = ["123","321","456","654","789","987","098"]
listaIndice = []

def opcaoUser():
    print("Você deseja: ")
    print(" 1 - Cadastrar: ")
    print(" 2 - Pesquisar: ")
    print(" 3 - Excluir: ")
    print(" 4 - Atualizar:")
    print(" -1 - Sair da Lista: \n")

def cadastrar():
    nome = 0
    telefone = 0

    nome = input("Digite o nome completo: ")
    telefone = input("Digite o número do telefone: ")

    if nome and telefone != 0:
        listaNome.append(nome)
        listaTelefone.append(telefone)
    else:
        return
    print("")

def pesquisaNome(nome):
    i = 0
    j = 1
    listaIndice.clear()
    if nome in listaNome:
        print("\nAtualmente há",listaNome.count(nome),"contatos com o nome: ",nome)
        while i < len(listaNome):
            if nome in listaNome[i]:
                print(j,'-',listaNome[i],'|',listaTelefone[i])
                #print(i) #Quando não comentado esse print mostra o indice
                listaIndice.append(i)
                j += 1
            i += 1
    else:
        print("Não cadastrado")
    print("")
    return

def pesquisarNumero(numero):
    i = 0
    j = 1
    listaIndice.clear()
    if numero in listaTelefone:
        print("\nAtualmente há", listaTelefone.count(numero),"contatos com o número: ",numero)
        while i < len(listaTelefone):
            if numero in listaTelefone[i]:
                print(j,'-',listaNome[i],'|',listaTelefone[i])
                # print(i) #Quando não comentado esse print mostra o indice
                listaIndice.append(i)
                j += 1
            i += 1
    else:
        print("Não cadastrado")
    print("")
    return

def listarTodos():
    i = 0
    listaIndice.clear()
    print("\nLISTA COM TODOS OS CONTATOS:")
    while i < len(listaTelefone):
        print(i+1,'-',listaNome[i],'|', listaTelefone[i])
        listaIndice.append(i)
        i += 1
    print("")
    return

def pesquisar(funcao):
    opcao = 0
    while opcao != '-1':
        if funcao == 1:#Caso a função seja chamada pelo usuário apresenta o texto abaixo
            opcao = input("Deseja pesquisar por:\n 1 - Nome\n 2 - Número\n 3 - TODOS\n -1 - Voltar\n Digite: ")
        elif funcao == 2: #Caso a função seja chamada pela função excluir apresenta o texto abaixo
            opcao = input("Deseja pesquisar para excluir por:\n 1 - Nome\n 2 - Número\n 3 - Mostrar TODOS\n -1 - Voltar\n Digite: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            pesquisaNome(nome) #Chama a função que verifica o nome
        elif opcao == '2':
            numero = input("Digite o número: ")
            pesquisarNumero(numero) #Chama a função que verifica o número
        elif opcao == '3':
            listarTodos()
        else:
            print("Tente novamente, digite uma das opções acima: ")

        if funcao == 2:
            opcao = '-1'
    return

def excluir():
    funcao = 2 #Indica que pesquisar foi chamada pela função excluir
    opcao = 0
    while opcao != -1:
        i = 0
        pesquisar(funcao)
        opcao = int(input("Digite o número relativo ao contato que deseja excluir ou -1 para sair: "))
        if opcao != -1:
            while i < len(listaTelefone):
                i += 1
                if opcao == i:
                    listaNome.pop(listaIndice[opcao-1])
                    listaTelefone.pop(listaIndice[opcao-1])
                    #opcao = -1
                    #i = 0
    return

def atualizar():
    return

if __name__ == '__main__':

    print("\nBEM VINDO A SUA LISTA DE CONTATOS\n")
    opcao = 0
    while opcao != '-1':
        opcaoUser()
        opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            funcao = 1 #Indica que pesquisar foi chamado pelo usuário pesquisar
            pesquisar(funcao) #Caso seja chamada pelo usuário a função pesquisar retorna o valor 1
        elif opcao == '3':
            excluir()
        elif opcao == '4':
            atualizar()
        elif opcao == '-1':
            break
        else:
            print("Digite um valor válido\n")