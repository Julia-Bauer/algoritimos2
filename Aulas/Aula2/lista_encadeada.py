# estrutura que armazena um conjunto de elementos, em determinada sequencia

# pemite alocação dinamica da memoria

# É construida por elementos que possuem uma estrutura de valor e endereço do próximo elementos

# Se estivermos no último elemento da lista, o campo para o endereço terá como valor: NULL

#--------------------------------

# vetor é uma variável que é possivel alocar vários valores

#vetor tem tamanho fixo

#---------------------------------

#quando não cria arrey, os valores ficam espalhados pela memória

from no import No

#classe com uma lista vazia
class Lista:
    #criar uma lista vazia
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    #para poder usar a função len na lista encadeada
    def __len__(self):
        #retorna tamanho da lista
        return self.tamanho

    def adicionar(self, valor):
        #se a lista não estiver vazia
        if self.inicio:
            #inserção quando a lista já possui elementos
            ponteiro = self.inicio
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(valor)
        else:
            #self.inicio terá apenas uma referência para o objeto
            self.inicio = No(valor)
        #incrementa em um o tamanho da lista
        self.tamanho = self.tamanho +1
    
    #Pega um índice e retorna o nó que está neste índice
    def getNo(self, index):
        ponteiro = self.inicio
        #para cada item no intervalo do index que eu quero
        for item in range(index):
            #se não estiver vazio
            if ponteiro:
                #ponteiro se torna o ponteiro do próximo elemento
                ponteiro = ponteiro.proximo
            #se a lista estiver vazia
            else:
                raise IndexError("Index fora do intervalo da Lista")
        return ponteiro

    def __getitem__(self, index):
        #ponteiro = self.inicio
        #para cada item no intervalo do index que eu quero
        #for item in range(index):
            #se não estiver vazio
            #if ponteiro:
                #ponteiro se torna o ponteiro do próximo elemento
                #ponteiro = ponteiro.proximo
            #se a lista estiver vazia
            #else:
                #raise IndexError("Index fora do intervalo da Lista")
        
        #A parte acima do código virou a função a parte getNo()
        ponteiro = self.getNo(index)
        
        #se não estiver vazio
        if ponteiro:
            #retorna o dado do ponteiro
            return ponteiro.dado
        #else
        raise IndexError("Index fora do intervalo da Lista")

    def __setitem__(self, index, Novoelemento):
        #ponteiro = self.inicio
        #para cada item no intervalo do index que eu quero
        #for item in range(index):
            #se não estiver vazio
            #if ponteiro:
                #ponteiro se torna o ponteiro do próximo elemento
                #ponteiro = ponteiro.proximo
            #se a lista estiver vazia
            #else:
                #raise IndexError("Index fora do intervalo da Lista")
        
        #A parte acima do código virou a função a parte getNo()
        ponteiro = self.getNo(index)

        #se não estiver vazio
        if ponteiro:
            #o dado do ponteiro se torna o novo elemento
            ponteiro.dado = Novoelemento
        else:
            raise IndexError("Index fora do intervalo da Lista")
    
    def index(self, elemento):
    #Retorna o índice do elemento na lista
        ponteiro = self.inicio
        #variável para guardar a posição, 0 é a primeira posição válida
        posicao = 0
        while(ponteiro):
            # se o dado do ponteiro for igual ao elemento procurado
            if ponteiro.dado == elemento:
                #se encontrar o elemento retorna posição
                return posicao
            # se o dado não for igual ao elemento
            #o ponteiro "anda" para a próxima posição
            ponteiro = ponteiro.proximo
            posicao += 1
        #Se não encontrar o elemento em nenhuma posição
        raise ValueError(f"O elemento {elemento} não está na lista")

    def inserir(self, index, Novoelemento):
        # cria o nó com o novo elemento
        no = No(Novoelemento)
        
        #Se quiser inserir na primeira posição da lista
        if index == 0:
            # O item de inicio da lista (não atualizada) se torna o no.proximo
            no.proximo = self.inicio
            #Atualiza o inicio da lista para o nó que entrou
            self.inicio = no
        #se quiser inserir numa posição diferente de 0
        else:
            #ponteiro começa na primeira posição
            #ponteiro = self.inicio
            #O -1 é para que possamos inserir após seu precessor, no local correto da lista
            #for item in range(index - 1):
                #se o ponteiro não está numa posição vazia(none), último da lista
                #if ponteiro:
                    #O ponteiro "anda" para o próximo da lista
                    #ponteiro = ponteiro.proximo
                #else:
                    #raise IndexError("Index fora do intervalo da Lista")
        
            #A parte acima do código virou a função a parte getNo()
            #O -1 garante que o item a ser incerido fique na posição correta
            ponteiro = self.getNo(index-1)
            #garante que os próximos valores serão "apontados"
            no.proximo = ponteiro.proximo
            ponteiro.next = no

        #aumenta o tamanho da lista em 1
        self.tamanho += 1

    #Reproduzir
    def __repr__(self):
        reproducao = ""
        ponteiro = self.inicio
        while(ponteiro):
            reproducao = reproducao + str(ponteiro.dado) + " -> "
            ponteiro = ponteiro.proximo
        return reproducao

    def __str__(self):
        return self.__repr__()

    #método para remover elemento da lista
    def excluir(self, elemento):
        #Se a lista está vazia
        if self.inicio == None:
            raise ValueError(f"O elemento {elemento} não está na lista")

        #Se o elemento for o primeiro da lista
        elif self.inicio.dado == elemento:
            #O inicio se tornará o próximo elemento
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            return True
        else:
            anterior = self.inicio
            ponteiro = self.inicio.proximo
            while(ponteiro):
                #se encontrou o elemento
                if ponteiro.dado == elemento:
                    #Ajuste do encadeamento, liga o anterior ao sucessor do nó que se quer remover
                    anterior.proximo = ponteiro.proximo 
                    #para sair do laço
                    ponteiro.proximo = None

                #Se não encontrou o elemento
                #o ponteiro está sempre uma posição a frente do "anterior"
                anterior = ponteiro
                ponteiro = ponteiro.proximo
            self.tamanho -= 1
            return True
        raise ValueError(f"O elemento {elemento} não está na lista")



    






    