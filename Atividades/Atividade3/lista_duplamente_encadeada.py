from no import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def adicionar(self, valor):
        no = No(valor)
        if self.inicio:
            ponteiro = self.inicio
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = no
            no.anterior = ponteiro
            self.fim = no
        else:
            self.inicio = no
            self.fim = no
        self.tamanho += 1
    
    def __repr__(self, reverso):
        reproducao = ""
        if reverso == False:
            ponteiro = self.inicio
            while(ponteiro):
                reproducao = reproducao + str(ponteiro.dado) + " -> "
                ponteiro = ponteiro.proximo
            return reproducao
        if reverso == True:
            ponteiro = self.fim
            while(ponteiro):
                reproducao = reproducao + str(ponteiro.dado) + " -> "
                ponteiro = ponteiro.anterior
            return reproducao

    def __str__(self):
        return self.__repr__()
    
    