valores = [1,2,3,4,5,"x"]
print(6 in valores) # verifica se um valor esta dentro da lista de valores
print("x" in valores) # verifica se um valor esta dentro da lista de valores
print("a" in "banana") # funciona também para strings que são consideradas uma sequencia de caracteres
print(len(valores)) # mostra a quantidade total de itens na lista
valores = [1,2,3,4,5,6,7,8,9,10,10,1,2] # redefine a lista
print(min(valores)) #imprime valor minimo da lista
print(max(valores)) #imprime valor maximo da lista
print(valores.count(10)) # conta a frequencia com que aparece o numero 10
valores.append(20) # adiciona um elemento no final da lista
valores.pop() # remove um elemento no final da lista
valores[0] = 2 # sobrescreve o elemento no indice 0 da 
print("banana".capitalize()) # funcao da classe str que coloca a 1 letra em maiuscula
print("banana".upper()) # funcao da classe str que coloca todas letras em maiusculas
print("BANANA".lower()) # funcao da classe str que coloca todas letras em minusculas
print("algazarra".count("r")) # funcao da classe str que conta a frequencia com que aparece a letra r
print("    alto    ".split()) # # funcao da classe str que remove espaços em branco no inicio e fim