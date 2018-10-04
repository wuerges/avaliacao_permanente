# Avaliação Periódica

Este repositório contem um programa simples para realizar a avaliação periódica do curso de CC da UFFS.


## Dependências

As dependêcias do projeto são:

1. python 3.7
2. bottle
3. matplotlib
4. pandas

As dependêcias podem ser instaladas individualmente, ou com o pipenv, automaticamente.

## Coletando as respostas

Para rodar o servidor, basta usar o seguinte comando:

```bash
$ python serve.py
```

Desta maneira, um servidor web estará atendendo as URL no seguinte formato:

http://localhost:8080/turma/<codigo da turma>

## Gerando os resultados

Para gerar os resultados, basta executar o seguinte comando:

```bash
$ python results.py
```

Depois disso, dentro da pasta 'outputs', serão criados os relatórios em formato HTML.

## Configurando as perguntas.

As perguntas estão descritas no arquivo `simples.mf'.
Cada linha desse arquivo ou contém uma pergunta, ou uma resposta. 
As perguntas começam com P. As respostas começam com r. , c. ou t.

- P. Inicia uma nova pergunta, e as repostas seguintes pertencerão a esta pergunta.
- r. Indica que a resposta pertence a um conjunto de respostas em que só uma pode ser assinalada.
- c. Indica que a resposta pertence a um conjunto em que mais de uma pode ser assinalada.
- t. Cria uma caixa de texto para o usuário digitar a resposta.

IMPORTANTE: Não pode ter linhas em branco. 

## Configurando as turmas.

As turmas estão descritas no arquivo `ofertas.mf'.
Este arquivo pode ter 2 tipos de linha. 

- As linhas que começam com T. indicam uma nova turma.
- As linhas que começam com D. indicam o nome da disciplina. Nesta versão, estas linhas são ignoradas.

O formato das linhas T. é importante. Elas precisam estar neste formato:

```
T. <código de turma> - <outras informações>
```

IMPORTANTE: Não pode ter linhas em branco.
