#First in first out
#Estrutura de dados linear
#Inserções são realizadas no final da fila
#Exclusões são realizadas no inicio da fila
#Estrutura que armazena na sequência em que os elementos chega,
#Permite alocação dinâmica de memória
#É constituida por elementos que possuem uma estrutura composta por valor e endereço do proxomo elemento
#Se estivermos no último elemento da fila, o campo para o proximo tera como valor NULL

from no import No

class Fila:
    
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def adicionar(self, dado):
        no = No(dado)

        if self.tamanho == 0:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no

        self.tamanho +=1

    def imprimir(self):
        texto = ""
        if self.tamanho == 0:
            texto = "Fila Vazia"
        else:
            ponteiro = self.inicio
            while(ponteiro):
                texto = texto + str(ponteiro.dado) + " - "
                ponteiro = ponteiro.proximo
        print(texto)
    
    def remover(self):

        if self.tamanho == 0:
            print("Fila Vazia")

        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1


    