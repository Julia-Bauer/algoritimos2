from no import No
from lista_semcomentarios import Lista

lista = Lista()

print(f"Tamanho da lista:{str(lista.tamanho)}")

lista.adicionar(3)

print(f"Tamanho da lista:{str(lista.tamanho)}")

print(lista)

valor = input("Digite um valor:")
lista.adicionar(valor)

valor = input("Digite um valor:")
lista.adicionar(valor)

valor = input("Digite um valor:")
lista.adicionar(valor)

print("\n--------------------\n")
print(lista)
print(f"Tamanho da lista:{str(lista.tamanho)}")

valor = input("Digite um valor para excluir:")
lista.excluir(valor)

print(lista)