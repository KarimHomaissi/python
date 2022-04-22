# criar um arquivo
arquivo = open("nomedoarquivo.txt","w") # leitura (r) read escrita (w) write atualizacao (a) append
arquivo.write("banana\n") # escrevendo dentro do arquivo criado
arquivo.write("melancia\n") # escrevendo dentro do arquivo criado
arquivo.write("morango\n") # escrevendo dentro do arquivo criado
arquivo.write("maça\n") # escrevendo dentro do arquivo criado
arquivo.close() # fechando canal de comunicacao com sistema operacional
