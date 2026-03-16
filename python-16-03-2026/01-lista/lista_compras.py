# Crie um programa que gerencie uma lista de compras. O usuário pode adicionar, remover, listar
# e buscar itens. O programa deve rodar em loop até o usuário escolher sair.

continua = True
lista = []
while continua:
    print ("Adicionar digite 1")
    print ("Remover digite 2 para remover pelo nome")
    print ("Listar todos digite 3")
    print("Buscar item posição digite 4")
    print ("Sair digite 0")
    opcao = int(input("Escolha a opção desejada: "))

    if opcao.is_integer():
        if opcao == 1:
            lista.append(input("Item: "))
        elif opcao == 2:
            lista.remove(input("Item para remover: "))
        elif opcao == 3:
            print(lista)
        elif opcao == 4:
            posicao = int(input("Posição: "))
            print(lista[posicao])
        elif opcao == 0:
            continua = False
        else:
            print("Dado Inválido")