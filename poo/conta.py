
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o Objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


conta = Conta(1,"Karim Homaissi",100.0,1000.0)
conta2 = Conta(2,"Marco Antonio",55.0,1000.0)

print(conta.titular,conta2.titular)