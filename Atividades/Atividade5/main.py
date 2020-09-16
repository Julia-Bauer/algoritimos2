from pilha import Pilha

pilha = Pilha()
opcao = ""

while(opcao != "0"):
    print("\n ---------------")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Imprimir")
    print("0 - Sair")
    
    opcao = input("Digite sua opção:")

    if opcao == "1":
        dado = input("Informe um Valor:")
        pilha.adicionar(dado)
    if opcao == "2":
        pilha.remover()
    if opcao == "3":
        pilha.imprimir()