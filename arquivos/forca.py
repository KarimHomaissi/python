import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

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

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    with open("palavras.txt","r") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()