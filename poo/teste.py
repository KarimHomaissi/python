
def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo: {}".format(conta["saldo"]))

conta1 = criar_conta(1,"Karim",100.00,1000.00)
print(conta1["numero"],conta1["titular"],conta1["saldo"],conta1["limite"])
sacar(conta1,50)
extrato(conta1)
depositar(conta1,20)
extrato(conta1)