from pessoa import Pessoa
from fisica import Fisica 
from juridica import Juridica 

p = Pessoa("Julia", "Av. Ipiranga")
f = Fisica("Maria", "Av. Protásio Alves", "111.222.333-44")
j = Juridica("Mercado do João", "Av. A, 132", "11.222.333/0001-44")

p.imprimir()
f.imprimir()
j.imprimir()