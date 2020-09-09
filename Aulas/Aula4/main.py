from fila_fifo import Fila

fila = Fila()
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
        fila.adicionar(dado)
    if opcao == "2":
        fila.remover()
    if opcao == "3":
        fila.imprimir()
