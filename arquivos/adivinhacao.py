import random

def jogar():
        
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    # numero_secreto = round(random.random()*100) # gera um numero entre 0.0 e 1.0
    numero_secreto = random.randrange(1,101) # gera um numero entre 1 e 100
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificíl")

    nivel = int(input("Define o nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você Errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você Errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) # usando funcao built-in abs para nao dar valores negativos
            pontos = pontos - pontos_perdidos


    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar()