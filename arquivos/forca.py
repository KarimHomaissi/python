import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")


    with open("palavras.txt","r") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(letras_acertadas)-erros))     

        enforcou = erros == len(letras_acertadas)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você Acertou !!")
    else:
        print("Você Perdeu!!")
        print("A Resposta era: {}".format(palavra_secreta))

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar()