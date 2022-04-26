#!/bin/bash

cd ~/Downloads/imagens-livros

for imagem in $@
do
    convert $imagem.jpg $imagem.png
done

: '
  ~ = diretorio home
  convert = é usado através da biblioteca imagemagick para converter extensoes de imagens para outras extensoes
  #!/bin/bash = é o interpretador que queremos utilizar ao rodar nosso shell script
  rodamos com o comando bash conversao-jpg-png.sh
'

