#   ---------------------------------
#   -             PESSOA            -
#   ---------------------------------
#   -   - código: int               - 
#   -   + nome: string              -
#   -   # endereço: string          -
#   -   - telefone: string          - 
#   ---------------------------------
#   -   +imprimeNome(): sring       -
#   -   -imprimeTelefone(): void    -
#   ---------------------------------


class Pessoa:
    def __init__(self):
        self._codigo = None
        self.nome = None
        self.__endereco = None
        self._telefone = None

    def getCodigo(self):
        return self._codigo

    def getNome(self):
        return self.nome 
    
    def getEndereco(self):
        return self.__endereco

    def getTelefone(self):
        return self._telefone

    def setCodigo(self, codigo):
        try:
            codigo = int(codigo)
            self._codigo = codigo
        except:
            print('Código inválido')

    def setNome(self, nome):
        if len(nome) > 2:
            self.nome = nome
        else:
            print('Nome inválido')
    
    def setEndereco(self, endereco):
        self.__endereco = endereco

    def setTelefone(self, telefone):
        self._telefone = telefone

    def imprimeNome(self):
        print(self.nome)

    def imprimeTelefone(self):
        return None
