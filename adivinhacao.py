print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu numero: "))

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

print("Você digitou", chute)

if(acertou):
    print("Você Acertou!")
else:
    if(maior):
        print("Você Errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
        print("Você Errou! O seu chute foi menor do que o número secreto.")
print("Fim do Jogo!")