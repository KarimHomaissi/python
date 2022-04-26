#!/bin/bash

converte_imagem() {
    cd ~/Downloads/imagens-livro
    if [ ! -d png ] 
    then
        mkdir png
    fi

    for imagem in *.jpg
    do
        local imagem_sem_extensao=$(ls $imagem | awk -F. '{ print $1 }')
        convert $imagem_sem_extensao.jpg png/$imagem_sem_extensao.png
    done
}

converte_imagem 2>erros_conversao.txt
if [ $? -eq 0 ]
then
    echo "Conversao realizada com sucesso"
else
    echo "Houve uma falha no processo de conversao"
fi

: '
  ~ = diretorio home
  convert = é usado através da biblioteca imagemagick para converter extensoes de imagens para outras extensoes
  #!/bin/bash = é o interpretador que queremos utilizar ao rodar nosso shell script
  rodamos com o comando bash conversao-jpg-png.sh
  SCRIPT SHELL NAO PERMITE A SEPARACAO DO = DA VARIAVEL E DO CONTEUDO
  DENTRO DO COLCHETES DO IF TEM QUE TER ESPACO
  VERIFICAMOS SE EXISTE O DIRETORIO /PNG PARA PODER JOGAR AS IMAGENS CONVERTIDAS LA
'

