
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o Objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo: R$ {}".format(self.get_saldo()))

    def depositar(self,valor):
        self.__saldo += valor
    
    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("o valor R$ {} passou o limite.".format(valor))
    
    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


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