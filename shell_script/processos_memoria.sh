#!/bin/bash

# ps -e (lista todos os processos rodando na maquina)
# ps -e -o pid (-o de output pedimos apenas a informacao referente ao id do processo)
# ps -e -o pid --sort -size (ordenamos os processos pelo tamanho de ocupacao de memoria com o --sort)
# usamos o pipe para redirecionar a saida para o head que exibe as 10 primeiras linhas, porem a 1 linha é o nome PID
# por isso usamos head -n 11 para retornar 11 informacoes, sendo 10 processos e o nome da coluna que é PID
# usamos novamente o pipe para redirecionar para o grep e pegar apenas numeros de 0 a 9
# com isso retornamos apenas o numero de 10 processos que mais consomem memoria no pc
# logo apos fazemos um laço for para percorrer esses numeros e usamos o ps -p de processo -o de output e comm= para exibir o nome dos processos

if [ ! -d log ]
then
    mkdir log
fi

processos_memoria() {
    processos=$(ps -e -o pid --sort -size | head -n 11 | grep [0-9])
    for pid in $processos
    do
        nome_processo=$(ps -p $pid -o comm=)
        echo -n $(date +%F,%H:%M:%S, ) >> log/$nome_processo.log
        tamanho_processo=$(ps -p $pid -o size | grep [0-9])
        echo "$(bc <<< "scale=2;$tamanho_processo/1024") MB" >> log/$nome_processo.log
    done
}

processos_memoria
if [ $? -eq 0 ]
then
    echo "Os arquivos foram salvos com sucesso"
else
    echo "Houve um problema ao salvar os arquivos"
fi