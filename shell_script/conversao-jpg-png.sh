#!/bin/bash

cd ~/Downloads/imagens-livros

for imagem in *.jpg
do
    imagem_sem_extensao = $(ls $imagem | awk -F . '{ print $1 }')
    convert $imagem_sem_extensao.jpg $imagem_sem_extensao.png
done

: '
  ~ = diretorio home
  convert = é usado através da biblioteca imagemagick para converter extensoes de imagens para outras extensoes
  #!/bin/bash = é o interpretador que queremos utilizar ao rodar nosso shell script
  rodamos com o comando bash conversao-jpg-png.sh
'

