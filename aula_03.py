#ESTRUTURA CONDICIONAL

#CONDICIONAL SIMPLES: (ou um bloco é executado ou nada)

#1-Lê dois valores inteiros e compara ambos
x = int(input('Digite um valor inteiro:'))
y = int(input('Digite o segundo valor inteiro:'))
if(x > y):
    print('O primeiro valor é maior que o segundo!')

#CONDICIONAL COMPOSTA: (um bloco é executado ou outro)

#2- Desenvolva um programa que lê um valor inteiro e descobre se é par ou ìmpar:
x = int(input('Digite um valor inteiro:'))
if (x % 2 == 0):           #(% é o módulo (mod), o resto da divisão)
    print('O número é par!')
else:
    print('O número é impar!')

#OPERADORES LÓGICOS

#not (negação - não) Se tem verdadeiro vira falso, nega uma variável booliana
#and (conjunção -  e) provem resultado verdadeiro, se ambas as entradas forem verdadeiras
#or  (disjunção - ou) rovem resultado verdadeiro, se ao menos uma das entradas forem verdadeiras

#exemplos:

#not
x =  True
y = False
print(not x)
print(not y)

#and
x =  True
y = False
print(x and y)

#or
x =  True
y = False
print(x or y)

# PRECEDÊNCIA DOS OPERADORES:

#1º CALCULA-SE OS PARENTESES
#2º OPERADORES ARITMETICOS DE POTNCIAÇÃO OU RAIZ
#3º OPERADORES ARITMETIVOS DE MULTIPLICAÇÃO, DIVISAO E MÓDULO
#4º ADIÇÃO E SUBTRAÇÃO
#5º OPERADORES RELACIONAIS
#6º OPERADORES LÓGICOS not
#7º OPERADORES LÓGIDOS and
#8º OPERADORES LÓGICOS or
#9º ATRIBUIÇÕES

#EXPRESSÕES LÓGICAS BOOLEANAS
x = 10
y = 1
res = not x > y #FALSO
print(res)

x = 10
y = 1
z = 5.5
res =  x > y and z == y #FALSO
print(res)

#EXERCÍCIOS:

#1- Um, aluno para passar de ano precisa ser aprovado em todas as matérias que,
# está cursando. Assuma que a média para aprovação é a partir de 7l e que o aluno cursa 3 matérias,
# somente. Escreva um algoritmo que leia a nota final do aluno em cada materia e,
# informe na tela se ele passou de ano ou não:

m1 = float (input('Digite a nota da primeira matéria:'))
m2 = float (input('Digite a nota da primeira matéria:'))
m3 = float (input('Digite a nota da primeira matéria:'))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno está aprovado de ano!')
else:
    print('O aluno está reprovado de ano!')

#CONDICIONAIS ANINHADAS

#2- Escreva um algoritmo em Phyton em que o usuário escole se quer comprar maçãs, laranjas ou bananas.
# Deverá ser apresentado na tela um menu com as opçoes 1 para maçã, 2 para laranja e 3 para banana
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve
# calcular o preço total a pagar do produto escolhido e mostrár-lo na tela.
# Considere que : MAÇA = 2,30 / LARANJA = 3,60 / BANANA = 1,85

print('Escolha o produto que deseja comprar:')
print('1 - Maçã:')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas unidades?'))
if (produto == 1):
    pagar = qtd + 2.3
    print('Você comprou {} maçãs. Total à pagar: {}'.format(qtd, pagar))
else:
  if (produto == 2):
        pagar = qtd + 3.6
        print('Você comprou {} laranjas. Total à pagar: {}'.format(qtd, pagar))
  else:
       if (produto == 2):
         pagar = qtd + 3.6
         print('Você comprou {} bananas. Total à pagar: {}'.format(qtd, pagar))
       else:
         print('Produto inexistente')

#MESMO PROGRAMA PORÉM RESOLVIDO COM ELIF:
print('Escolha o produto que deseja comprar:')
print('1 - Maçã:')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas unidades?'))
if (produto == 1):
    pagar = qtd + 2.3
    print('Você comprou {} maçãs. Total à pagar: {}'.format(qtd, pagar))
elif (produto == 2):
 pagar = qtd + 3.6
 print('Você comprou {} laranjas. Total à pagar: {}'.format(qtd, pagar))
elif (produto == 3):
 pagar = qtd + 1.85
 print('Você comprou {} bananas. Total à pagar: {}'.format(qtd, pagar))
else:
 print('Produto inexistente!')

#3-Escreva um algoritmo que lê um nome e uma idade, caso o nome seja Vinicius
# escreva isso na tela, caso o usuário digite qualquer outro nome, verifique sua idade.
# informe que é de menor. Se for maior que 100 anos, informe que esta pessoa possivelmente
# não existe:

nome = input('Qual seu nome?')
idade = input('Qual sua idade?')
if nome == 'Vinicius':
 print('Olá,Vinicius!')
elif idade < 18:
  print('Você não é o Vinicius e é menor de idade!')
elif idade > 100:
 print('Diferente de você, o Vinicius não é imortal')

#EXPRESSOES BOOLEANAS:

#4- Escreva as seguintes expressoes booleanas em Phyton:
#a) O somatório de 2 com 2 é menor do que 4:
print(2 + 2 < 4)
#b) O valor de 7 // 3 é igual a 1 + 1:
print(7 // 3 == 1 + 1)
#c) A soma de 3 elevado ao quadrado com 4 elevado ao 4 quadrado é igual a 25:
print(3**2 + 4**2) == 25
#d)A soma de 2, 4 6 é maior que 12:
print(2 + 4 + 6 > 12)
#e) 1387 é divisivel por 19:
print(1387 // 19)
#f) 31 é par:
print( 31 % 2 == 0)
#) O menor valor entre: 34, 29 e 31 é menor que 30:
print(min(34, 29, 31) < 30)

#5- Exercicio dos triângulos
A =  int(input('Digite o 1º lado do triângulo:'))
B =  int(input('Digite o 2º do triângulo:'))
C =  int(input('Digite o 3º do triângulo:'))
if (A > 0) and (B > 0) and (C > 0):
  if (A + B > C) and (A + C > B) and (B + C > A):
     if (A != B and A != C and B != C):
        print('Triângulo escaleno.')
     else:
         if (A == B) and (A == C) and (B == C):
             print('Triângulo equilátero.')
         else:
             print('Triângulo isósceles.')
  else:
      print('Ao menos um dos valores indicados não servem para formar um triângulo.')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')

#6 Calculadora simples:
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação você deseja fazer?')

x = int(input('Digite o primeiro valor'))
y = int(input('Digite o segundo valor'))

if (op == '+'):
    res = x + y
    print('Resultado: {} + {} = {}'.format(x, y, res))
elif(op == '-'):
    res = x - y
    print('Resultado: {} + {} = {}'.format(x, y, res))
elif (op == '*'):
    res = x * y
    print('Resultado: {} + {} = {}'.format(x, y, res))
elif (op == '/'):
    res = x / y
    print('Resultado: {} + {} = {}'.format(x, y, res))
else:
    print('Operação inválida')

print('Encerrando o programa...')

# FIM DA AULA 3 -------------------------------------






