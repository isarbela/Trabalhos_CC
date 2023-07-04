# Trabalho - Construção de Compiladores

Repositório dedicado ao desenvolvimento dos trabalhos da disciplina de Construção de Compiladores ministrada pelo professor Lucrédio no semestre 2023/1.

## Feito pelos alunos:
 - Gabriel Penajo Machado. RA: 769712
 - Isabela Vieira Magalhães. RA: 769755
 - Matheus Teixeira Mattioli. RA: 769783

## Requisitos
 - Antlr 4.13 (https://github.com/antlr/antlr4/blob/master/doc/python-target.md)
 - Python 3 (https://www.python.org/downloads/)

## Como compilar, executar e rodar o corretor automático

1. Para executar o arquivo g4, rodar o comando a partir da pasta onde está localizado o Antlr
 ```
 java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 T1_CC/compilador/AnalisadorLA.g4
 ```
 
2. Para rodar o corretor "automágico" no sistema operacional Linux, executar o comando abaixo substituindo **CAMINHO1** pelo caminho do arquivo jar de correção na sua máquina, **CAMINHO2** pelo caminho desse projeto no seu computador e **CAMINHO3** o *path* dos casos de teste disponibilizados pelo professor..
 ```
 java -jar /home/CAMINHO1/compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python /home/CAMINHO2/T1_CC/compilador/Main.py" gcc /home/CAMINHO2/T1_CC/temp/ /home/CAMINHO3/casos-de-teste/ "769712 769755 769783" t1 
 ```
 
 ## Compilar e executar casos de teste um a um
 
 Para compilar o projeto executar o comando abaixo na pasta desse repositório, substituindo argv1 pelo arquivo .txt do caso de teste (arquivo com o programa) e argv2 pelo arquivo de saída
  ```
 python compilador/Main.py argv1 argv2
  ```

## Compilar e executar todos os casos de teste

Para compilar e executar todos os casos de teste, rodar o comando abaixo na pasta desse repositório, substituindo argv1 pela pasta com os casos de teste, a saída das execuções seram salvas na pasta temp/
  ```
  python run.py argv1
  ```

## T1

Como o T1 funciona diferente dos demais projetos, ele se encontra nesta outra branch [T1](https://github.com/isarbela/Trabalhos_CC/tree/trabalho1)
