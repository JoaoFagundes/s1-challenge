# s1-challenge
Código do desafio para uma vaga de eságio como Full Stack Developer na [SumOne](http://www.sumone.com.br/). o desafio consiste basicamente em projetar um serviço de ordenação. Mais informações podem ser encontradas [aqui](https://github.com/sumoners/s1-programming-challenges/tree/master/v2).

## Requisitos para execução
+ Python 3.5.3
+ PyQt5 5.9
+ configparser 3.5.0

## Instalação de dependencias
A instalação dos pacotes necessários pode ser feita através do gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/installing/). Basta executar `pip install -r requirements.txt`, do diretório raiz do repositório. Depois disso, basta executar o software pelo arquivo `main.py`, utilizando o comando:
```
  python main.py
```

**Obs:** é sugerido utilizar um ambiente isolado do python, para evitar conflitos entre dependências. Isso pode ser feito utilizando [virtualenv](https://virtualenv.pypa.io/en/stable/), rodando os comandos 
```
  python -m venv <nome_do_ambiente>
  source <nome_do_ambiente>/bin/activate
```
antes da instalação das dependencias.

Uma pequena base de livros é salva no arquivo `books/small_list.json` e pode ser carregada através do software.

## Configurando a ordenação
Para configurar a prioridade do algoritmo de ordenação é utilizado o arquivo `.config`, na raiz do repositório. O arquivo segue o padrão:
```
  [sort]
  order = <Atributo#1> <Direção#1>, <Atributo#2> <Direção#2>, ...
```

Por exemplo:
```
  [sort]
  Author Ascendant, Title Descendant
```
