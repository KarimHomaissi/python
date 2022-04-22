print("Meu nome é {}, tenho {} anos, sou estudante de {}.".format("Karim Homaissi",24,"Data e Analytics"))

# invertendo os parametros da interpolação através de um indice
print("Meu nome é {2}, tenho {1} anos, sou estudante de {0}.".format("Karim Homaissi",24,"Data e Analytics"))

# interpolacao com valores financeiros
print("R$ {}".format(1.59))
print("R$ {:f}".format(1.59)) # :f é para dizer que esta recebendo um parametro do tipo float
print("R$ {:.2f}".format(1.5)) # :.2f é para dizer que depois do ponto queremos apenas dois digitos
print("R$ {:7.2f}".format(1234.5)) # :7.2f o 7 que vem antes é para dizer a quantidade de caracteres total incluindo o ponto
print("R$ {:7.2f}".format(4.5)) # se faltar caracteres ele preenche com vazios a esquerda
print("R$ {:07.2f}".format(4.5)) # :07.2f ele preenche os caracteres faltantes com 0 a esquerda
print("R$ {:07d}".format(4)) # :07d (d) é para informar que é um caractere inteiro, 7 é para informar o total de caracteres
print("R$ {:7d}".format(4)) # :7d sem preencher com 0 a esquerda ele preenche com vazios
print("Data {:02d}/{:02d}".format(19,4)) # formatacao de datas com interpolacao de inteiros
print("Data {:02d}/{:02d}".format(19,11)) # formatacao de datas com interpolacao de inteiros