
def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

conta1 = criar_conta(1,"Karim",100.00,1000.00)
print(conta1["numero"],conta1["titular"])