# PROJETO DO CURSO DA ALURA DE CRIAR UM JOGO EM PYTHON

**OBSERVACOES:**

```

idade1 = 10
idade2 = "20"
print(idade1 + idade2)

```

> O código na verdade não funciona, e exibe a seguinte mensagem de erro no console:

> unsupported operand type(s) for +: 'int' and 'str'
> Isso acontece porque não podemos realizar uma operação de soma envolvendo uma string. Para resolvermos o problema, podemos apelar para a função int(), > que converte uma string que contém um número, em um número inteiro:

```

idade1 = 10
idade2 = int("20")
print(idade1 + idade2)

```
