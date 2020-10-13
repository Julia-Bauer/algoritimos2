from pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nomeF, enderecoF, cpfF):
        #self.nome = nomeF
        #self.endereco = enderecoF
        Pessoa.__init__(self, nomeF, enderecoF)
        self.cpf = cpfF    
    
    def imprimir(self):
        Pessoa.imprimir(self)
        print("CPF:" + self.cpf)
