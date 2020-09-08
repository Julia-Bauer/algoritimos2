from no import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def adicionar(self, valor):
        if self.inicio:
            ponteiro = self.inicio
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(valor)
        else:
            self.inicio = No(valor)
        self.tamanho = self.tamanho +1
    
    def getNo(self, index):
    #Retorna o ponteiro do index requerido
        ponteiro = self.inicio
        for item in range(index):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("Index fora do intervalo da Lista")

        return ponteiro

    def __getitem__(self, index):
        ponteiro = self.getNo(index)
        if ponteiro:
            return ponteiro.dado
        raise IndexError("Index fora do intervalo da Lista")

    def __setitem__(self, index, Novoelemento):
        ponteiro = self.getNo(index)
        if ponteiro:
            ponteiro.dado = Novoelemento
        else:
            raise IndexError("Index fora do intervalo da Lista")
    
    def index(self, elemento):
        ponteiro = self.inicio
        posicao = 0
        while(ponteiro):
            if ponteiro.dado == elemento:
                return posicao
            ponteiro = ponteiro.proximo
            posicao += 1
        raise ValueError(f"O elemento {elemento} não está na lista")

    def indexInsercaoOrdem(self, elemento):
        no = No(elemento)
        posicao = 0
        ponteiro = self.inicio
        try:
            prox = ponteiro.proximo
        except:
            prox = None

        #se a lista estiver vazia
        if self.inicio == None:
            self.inicio = no
            self.tamanho += 1
            return True

        #se o o dado for menor de todos, primeiro da lista
        if elemento < ponteiro.dado:
            no.proximo = self.inicio
            self.inicio = no
            self.tamanho += 1
            return True

        else:
            while True:
                
                #se for o último da lista
                if prox == None:
                    ponteiro.proximo = no
                    self.tamanho +=1
                    return True

                if elemento <= prox.dado:
                    ponteiro.proximo = no
                    no.proximo = prox
                    self.tamanho +=1
                    return True

                if elemento > prox.dado:
                    ponteiro = prox
                    prox = prox.proximo
                    posicao += 1
                


    def inserir(self, index, Novoelemento):
        no = No(Novoelemento)
        if index == 0:
            no.proximo = self.inicio
            self.inicio = no
        else:
            ponteiro = self.getNo(index-1)
            no.proximo = ponteiro.proximo
            ponteiro.next = no
        self.tamanho += 1

    def __repr__(self):
        reproducao = ""
        ponteiro = self.inicio
        while(ponteiro):
            reproducao = reproducao + str(ponteiro.dado) + " -> "
            ponteiro = ponteiro.proximo
        return reproducao

    def __str__(self):
        return self.__repr__()

    def excluir(self, elemento):
        if self.inicio == None:
            raise ValueError(f"O elemento {elemento} não está na lista")

        elif self.inicio.dado == elemento:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            return True
        else:
            anterior = self.inicio
            ponteiro = self.inicio.proximo
            while(ponteiro):
                if ponteiro.dado == elemento:
                    anterior.proximo = ponteiro.proximo 
                    ponteiro.proximo = None
                anterior = ponteiro
                ponteiro = ponteiro.proximo
            self.tamanho -= 1
            return True
        raise ValueError(f"O elemento {elemento} não está na lista")



    






    