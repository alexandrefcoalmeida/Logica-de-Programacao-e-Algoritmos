#Basico
print('hello world')

#Operaçãoes Aritméticas:
print(2 + 3)
#cálculo é sem aspas

#Concatenação
print( '2' + '3')
print('Olá ' + 'Mundo')
print('Olá' , 'Mundo')

#Concatenando mensagens e números
print('O resultado da soma de 2 + 3 é:', 2 + 3)

#OPERADORES E OPERAÇÕES MATEMÁTICAS:
# + ADIÇÃO
# - Subtração
# * Multiplicação
# / Divisão (com casas decimais)
# // Divisão (somente a parte inteira)
# % Módulo/ resto da divisão
# ** Exponenciação ou potenciação

#CUIDADO COM A ORDEM DOS ALGORITMOS
print(10*(5+7)/4)
print(10*(5+7/4))

#Atribuição
nota = 8.5
disciplina = 'Lógica e programação de algoritmos'
print(nota)
print(disciplina)
#ou
print('Disciplina: ', disciplina,'.Nota', nota)

#TIPOS DE DADOS
#VARIAVEL NUMÉRICA Inteiro (int) - números sem casas decimais
#PONTO FLUTUANTE (float) - números com casas decimais
#VARIÁVEL LÓGICA (1 OU 0) - variável booleana

#OPERADORES LÓGICOS

#  = atribuição
# == comparação de igualdade
#  > maior que
#  < menor que
# >= maior ou igual a
# <= menor ou igual a
# != diferente

#Variável lógica
a = 1
b = 5
print(a==b) #false
print(a!=b) #true

#Variável string ---------------------------------------------------------------------------------
frase = 'Qual o índice desta frase'
print(frase[0]) #Q
print(frase[3]) #l

#Concatenação de strings
s1 = 'Lógica de Programação'
s1 = s1 + ' e Algoritmos'
print(s1)

#Repetindo strings ma concatenação:
s1 = 'A' + '-' * 10 + 'B'
print(s1)

#Composição (string + variável)
nota = 8.5
s1 = ' Você tirou %f na disciplina de Algoritmos' % nota
print(s1)

#Agora limitando as casas decimais
nota = 8.5
s1 = ' Você tirou %.2f na disciplina de Algoritmos' % nota
print(s1)

#Várias variáveis:
nota = 8.5
s1 = ' Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)

#Marcadores
# %d ou %i para representar números inteiros
# %f Números de ponto flutuante .(float)
# %s Strings

#Composição moderna:
nota = 8.5
s1 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)
print(s1)

#Fatiamento de String:
s1 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)
print(s1[0:6])
print(s1[6:])

#Encontrar tamanho da String:
s1 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)
tamanho = len(s1)
print(tamanho) #66

#FUNÇÃO DE ENTRADA (INPUT- LER):
input('Qual é o seu nome?')

nome = input('Qual é o seu nome')
print('Olá {}, seja bem vindo!'.format(nome))

#Convertendo dados de entrada:
nota = float(input('Qual nota você recebeu na disciplina?'))
print('Você tirou nota {}.'.format(nota))


#-----------EXERCÍCIOS------------------
#1-Desenvolva um algoritmo que solicite ao usuário dois números inteiros,
#-e imprima a soma destes dois números na tela:

x = int(input('Digite um número inteiro:'))
y = int(input('Digite outro número inteiro:'))
#maneira clássica
res = 'O resultado da some de %i com %i é %i.' % (x, y,x + y)
print(res)
#maneira moderna
res = 'O resultado da soma de {} com {} é {}.'.format(x, y,x + y)
print(res)

#2-Escreva as seguintes expressões algébricas em liguagem phyton

#a) O somatório dos 5 primeiros números inteiros positivos
1 + 2 + 3 + 4 + 5
#b) A média entre 23,19 e 31
(23 + 19 + 31) / 3
#c) O número de vezes que 73 cabe em 403
403 // 73
#d) A sobra quando 403 é dividido por 73
403 % 73
#e) 2 elevado à 10ª potência
2 ** 10
#f) O valor absoluto da diferença entre 54 e 57
print(abs(54 - 57)) #calculo do valor absoluto independente do sinal
#g) O menor valor entrre 34, 29 e 31.
print(min(34, 29, 31)) #informa o valor mínimo entre os três

#3-Escreva as expressões em Phyton para:

#a) Atribuir o valor inteiro à variável a
a = 3
#b) Atribuir o valor 4 à variável b
b = 4
#c) Atribuir á variável c o valor da expressão a*a + b*b
c = a * a + b * b

#4- Execute as seguintes atribuições:

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

#Utilizando os operadores + e *, crie as saídas a seguir:
#a)ant bat cod
print(s1 + ' ' + s2 +' '+ s3)
#b) ant x10
print(10 * (s1 + ' '))
#c)ant bat bat cod cod cod
print(s1 + ' ' + (2 * (s2 + ' ')) + (3 * (s3 + ' ')))
#d)ant bat ant bat ant bat ant bat ant bat ant bat ant bat
print(7 * (s1 + ' ' + s2 + ' '))
#e) batbatcod batbatcod batbatcod batbatcod batbatcod
print(5 * (s2 + s2 + s3 + ' '))

#5- Desenvolva um algoritmo que solicite ao usuário o preço de um produto,
# e um percentual de desconto aplicado à ele. Calcule e exiba o valor do desconto
# e o preço final do produto:

preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o percentual de desconto sobre o produto (0-100):'))
desconto = preco * (p / 100)
final = preco - desconto
print('O preço do produto é {}.Com um dessconto de {}%'.format(preco, desconto))

#6- Escreva um prgrama que pergunte a quantidade de Km percorridos por um carro
# alugado pelo usuário, assim como a quantidadae de dias pelos quais o carro foi
#alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
# por Km rodado:

km =  int(input('Quantos Km foram percorridos?'))
dias =  int(input('Por quantos dias ele foi alugado?'))
preco = 60 * dias + 0.15 * km
print('KM={}. Dias:{}.'.format(km, dias))
print('Valor a ser pago:{}'.format(preco))

#7- Crie uma variável de string que receba uma frase qualquer. Depois crie uma
# variável, agora contendo a metade da string digitada. Imprima na tela
# somente os dois ultimos caracteres da segunda variável do tipo string:

frase = input('Digite uma frase:') #Alexandre
tam = len(frase)
frase2 = frase[:int(tam/2)] #Alex
print(frase2)

# FIM DA SEGUNDA AULA ---------------------------------------------------------




















