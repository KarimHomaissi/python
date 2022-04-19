# ALGUNS COMANDOS DO GITHUB

**PARA ADICIONAR UM REPOSITORIO REMOTO**

```
git remote add nome_do_repositorio caminho_ou_url_do_repositorio
```

**PARA RENOMEAR UM REPOSITORIO REMOTO**

```
git remote rename nome_do_repositorio_antigo novo_nome_para_o_repositorio
```

**PARA LISTAR OS REPOSITORIOS REMOTOS**

```
git remote
```

**PARA LISTAR DETALHADAMENTE OS REPOSITORIOS REMOTOS**

```
git remote -v
```

**PARA REVERTER ALTERAÇÕES NA WORKING TREE**

```
git checkout -- nomedoarquivo
```

**PARA REVERTER ALTERAÇÕES EM STAGED**

```
git reset HEAD nomedoarquivo
```

**PARA REVERTER ALTERAÇÕES COMMITADAS**

```
git revert hash_do_commit
```

**PARA ARQUIVAR ALTERAÇÕES PARA DEPOIS VOLTAR A TRABALHAR NELA**

```
git stash
```

**LISTAR ALTERAÇÕES ARQUIVADAS**

```
git stash list
```

**APLICAR AS ALTERAÇÕES ARQUIVADAS**

```
git stash apply numero_do_indice
```

**REMOVER DA LISTA DE ARQUIVAMENTO**

```
git stash drop numero_do_indice
```

**REMOVE E APLICA A ULTIMA ALTERAÇÃO ARQUIVADA**

```
git stash pop
```

**LIMPAR A LISTA DE ALTERAÇÕES ARQUIVADAS**

```
git stash clear
```
