from lista_duplamente_encadeada import Lista
from no import No

lista = Lista()

lista.adicionar(1)
lista.adicionar(22)
lista.adicionar(7)
lista.adicionar(2)
lista.adicionar(41)
lista.adicionar(78)
lista.adicionar(13)
lista.adicionar(4)
lista.adicionar(8)

#Printar na ordem normal (false indica que não é inverso)
print(lista.__repr__(False))

#Printar na ordem inversa (true indica que é inverso)
print(lista.__repr__(True))