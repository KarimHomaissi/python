# criar um arquivo
arquivo = open("nomedoarquivo.txt","w") # leitura (r) read escrita (w) write atualizacao (a) append
arquivo.write("banana\n") # escrevendo dentro do arquivo criado
arquivo.write("melancia\n") # escrevendo dentro do arquivo criado
arquivo.write("morango\n") # escrevendo dentro do arquivo criado
arquivo.write("maça\n") # escrevendo dentro do arquivo criado
arquivo.close() # fechando canal de comunicacao com sistema operacional
arquivo.open("nomedoarquivo.txt", "r") # modo leitura
print(arquivo.read()) # le o arquivo inteiro, e na segunda chamada da funcao retorna o final do arquivo que retorna nada
arquivo.close()  # fechando canal de comunicacao com sistema operacional
arquivo.open("nomedoarquivo.txt", "r") # modo leitura
arquivo.readline() # le apenas uma linha e pula para proxima
for linha in arquivo: # le linha por linha
    print(linha, end="") # o print coloca por padrão um \n no end , logo se voce ler os textos vai estar separados por espacos por ter dois \n
arquivo.close() # fechando canal de comunicacao com sistema operacional
