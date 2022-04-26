#!/bin/bash

CAMINHO_IMAGENS = ~/Downloads/imagens-livros

for imagem in $@
do
    convert $CAMINHO_IMAGENS/$imagem.jpg $CAMINHO_IMAGENS/$imagem.png
done

: '
  ~ = diretorio home
  convert = é usado através da biblioteca imagemagick para converter extensoes de imagens para outras extensoes
  #!/bin/bash = é o interpretador que queremos utilizar ao rodar nosso shell script
  rodamos com o comando bash conversao-jpg-png.sh
'

