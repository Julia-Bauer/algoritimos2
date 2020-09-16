from no import No

class Pilha:
    
    def __init__(self):
        self.fim = None
        self.tamanho = 0
    
    def adicionar(self, dado):
        no = No(dado)

        if self.tamanho == 0:
            self.fim = no
        else:
            no.anterior = self.fim
            self.fim = no

        self.tamanho +=1

    def imprimir(self):
        texto = ""
        if self.tamanho == 0:
            texto = "Pilha Vazia"
        else:
            ponteiro = self.fim
            while(ponteiro):
                texto = texto + str(ponteiro.dado) + " - "
                ponteiro = ponteiro.anterior
        print(texto)
    
    def remover(self):

        if self.tamanho == 0:
            print("Pilha Vazia")

        elif self.tamanho == 1:
            self.fim = None
            self.tamanho -= 1
        
        else:
            self.fim = self.fim.anterior
            self.tamanho -= 1


    