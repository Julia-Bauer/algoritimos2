from pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, nomeJ, enderecoJ, CNPJJ):
        Pessoa.__init__(self, nomeJ, enderecoJ)
        self.cnpj = CNPJJ

    def imprimir(self):
        Pessoa.imprimir(self)
        print("CNPJ:" + self.cnpj)
    