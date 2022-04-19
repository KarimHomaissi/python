print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
  print("Tentativa", rodada, "de", total_de_tentativas)
  chute = int(input("Digite o seu numero: "))
  print("Você digitou", chute)

  acertou = chute == numero_secreto
  maior   = chute > numero_secreto
  menor   = chute < numero_secreto

  if(acertou):
      print("Você Acertou!")
  else:
      if(maior):
          print("Você Errou! O seu chute foi maior do que o número secreto.")
      elif(menor):
          print("Você Errou! O seu chute foi menor do que o número secreto.")

      rodada = rodada + 1


print("Fim do Jogo!")