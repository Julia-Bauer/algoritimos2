class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    
    def imprimir(self):
        print("Nome:" + self.nome)
        print("Endereço:" + self.endereco)