print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu numero: "))

print("Você digitou", chute)

if(numero_secreto == chute):
    print("Você Acertou!")
else:
    if(chute > numero_secreto):
        print("Você Errou! O seu chute foi maior do que o número secreto.")
    if(chute < numero_secreto):
        print("Você Errou! O seu chute foi menor do que o número secreto.")
print("Fim do Jogo!")