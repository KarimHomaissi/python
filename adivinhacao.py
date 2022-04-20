import random


print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

# numero_secreto = round(random.random()*100) # gera um numero entre 0.0 e 1.0
numero_secreto = random.randrange(1,101) # gera um numero entre 1 e 100
total_de_tentativas = 3
rodada = 1

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
        print("Você Acertou!")
        break
    else:
        if(maior):
            print("Você Errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você Errou! O seu chute foi menor do que o número secreto.")


print("Fim do Jogo!")