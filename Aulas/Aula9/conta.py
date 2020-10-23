class Conta:
    def __init__(self):
        self.__saldo = 0

    def getSaldo(self):
        logado = True
        if logado:
            return self.__saldo

    def setSaldo(self, valor):
        admin = True
        if admin:
            self.__saldo = valor

    def __descontarTarifa(self):
        self.__saldo -= 1.5

    def depositar(self, valor):
        if valor >= 0:
            self.__saldo += valor
            self.__descontarTarifa()
