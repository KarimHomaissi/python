
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o Objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo: R$ {}".format(self.__saldo))

    def depositar(self,valor):
        self.__saldo += valor
    
    def sacar(self,valor):
        self.__saldo -= valor
    
    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)


conta = Conta(1,"Karim Homaissi",100.0,1000.0)
conta2 = Conta(2,"Marco Antonio",55.0,1000.0)

conta.extrato()
conta.depositar(100)
conta.extrato()
conta.sacar(10)
conta.extrato()

conta.transferir(90,conta2)
conta.extrato()
conta2.extrato()