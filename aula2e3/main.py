from no import No
from lista_encadeada import Lista

lista = Lista()

print(f"Tamanho da lista:{str(lista.tamanho)}")

lista.adicionar(3)

print(f"Tamanho da lista:{str(lista.tamanho)}")

lista.imprimir()

valor = input("Digite um valor:")
lista.adicionar(valor)
print("\n--------------------\n")
lista.imprimir()
print(f"Tamanho da lista:{str(lista.tamanho)}")

valor = input("Digite um valor para excluir:")
lista.excluir(valor)
lista.imprimir()