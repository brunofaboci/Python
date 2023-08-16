class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=5000):
        print("iniciando...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def get_titular(self):
        return self.__titular

    def set_limite(self, limite):
        self.__limite = limite

    def extrato(self):
        print("Titular: {}".format(self.__titular))
        print("Saldo: {}".format(self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, conta_destino, valor):
        self.sacar(valor)
        conta_destino.depositar(valor)


conta = ContaCorrente(123, "bruno", 150, 10000)
# conta2 = ContaCorrente(456, "joao", 200)
# print(conta.extrato())
# print(conta.depositar(100))
# print(conta.extrato())
# print(conta.sacar(50))
# print(conta.extrato())
# print(conta.get_saldo())
# print(conta.get_limite())
# print(conta.get_titular())
