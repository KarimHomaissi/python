

class Cliente:

    def __init__(self,nome):
        self.__nome = nome
    
    @property
    def nome(self):
        print("passou pela property")
        return self.__nome.upper()
    
    @nome.setter
    def nome(self,nome):
        print("passando pelo setter nome")
        self.__nome = nome

cliente = Cliente("karim")
print(cliente.nome)
cliente.nome = "marco"