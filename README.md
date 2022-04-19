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

**multiplicação com Python:**

```
numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)
```

**O resultado nos surpreende:**

> 20202020202020202020

> Não deu erro e sim imprimiu 10 vezes 20! Mas eu não acabei de falar que o Python é rígido e não converte automaticamente?
> Falei e na verdade não aconteceu uma conversão automática/implícita. Trata-se apenas de um syntax sugar do mundo Python. Um syntax sugar, açúcar sintático da linguagem, apenas simplifica algo que seria trabalhoso, mas não muda a característica da linguagem. Então, ao invés de escrever dez vezes o número 20, podemos simplificar e escrever 10 \* "20". Tudo bem?
