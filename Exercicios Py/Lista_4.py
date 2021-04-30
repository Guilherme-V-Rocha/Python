import math

"""
Professora: Juliana G. Souza
Aluno: Guilherme V. Rocha
Turma: 1°Periodo - TADS
Data: 29/04/2020
Lista 4 - Repetição por Condição
"""

#1) Supondo que a população de um país A seja da ordem de 90.000.000 de habitantes com uma taxa anual de crescimento de 3% e que a população de um país B
#seja, aproximadamente, de 200.000.000 de habitantes com uma taxa anual de crescimento de 1,5%, fazer um algoritmo que calcule e escreva o número de anos
#necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas essas taxas de crescimento.

"""
a = 90000000
b = 200000000
cont = 0
while a <= b:
  a += a * 0.03
  b += b * 0.015
  cont += 1
print("Para ultrapassar ou igualar B, levará o tolta de ", cont, " anos")
"""

#2) Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a massa inicial, em gramas, fazer um algoritmo que determine o
#tempo necessário para que essa massa se torne menor do que 0,5 grama. Escreva a massa inicial, a massa final e o tempo calculado em horas, minutos e
#segundos.

"""
def massa():
 massa_i = 10
 massa_f = massa_i
 tempo = 0
 hora = 0
 minutos = 0
 segundos = 0
 while massa_f > 0.5:
    massa_f = massa_f / 2
    tempo += 50
    minutos = 50 / 60
    hora = minutos / 60
    segundos = minutos * 60
    
    
 print (massa_f, hora, minutos,  segundos)
massa()
"""

#3) As idades de Bob e Renata são respectivamente 42 e 17 anos. Faça uma função para determinar quando Bob terá o dobro da idade de Renata.

"""
def idade():
   bob = 17
   retana = 42
   while bob < retana:
         bob += bob
   print(bob)
idade()
"""

#4) Didi possui 52 anos de idade, e seus filhos possuem 10 e 12 anos, respectivamente. Faça uma função para determinar quando a idade de
#Didi será igual a soma das idades dos seus filhos.

"""
def soma_idade():
    didi = 52
    filho = 10
    filho1 = 12
    soma = filho + filho1
    menos = 0
    while soma < didi:
       menos += didi - soma
       didi += menos
       filho += menos
       filho1 += menos
       soma = filho + filho1
    print("Daquia 30 anos quando Didi tiver", didi,"e seus filhos tiverem", filho, "e", filho1)
soma_idade()
"""

#5) Chico tem 1,50 m e cresce 2 cm por ano, enquanto Juca tem 1,10 m e cresce 3 centímetros por ano. Construir uma função para calcular
#quantos anos serão necessários para que Juca seja maior que Chico.

"""
def quem_cresce():
  chico = 1.50
  juca = 1.10
  cont = 0
  while juca < chico:
    chico =  chico + 0.02
    juca = juca + 0.03
    cont += 1
  print("Para ultrapassar ou igualar Chico, levará o tolta de ", cont, " anos")
quem_cresce()
"""

#6) Utilize o while para implementar as funções abaixo:
#    a) Faça uma função para exibir os números de 1 a 100.

"""
def um_cem():
    n = 0
    while n <= 100:
      print(n)
      n += 1
um_cem()
"""

#    b) Faça uma função para exibir os números pares de 10 a 50.

"""
def par():
  n = 10
  while n <= 50:
    print(n)
    n += 2
par()
"""

#    c) Faça uma função para exibir os números ímpares de 10 a 50.

"""
def impar():
  n = 10
  while n < 51:
    n += 1
    if n % 2 != 0:
      print (n)
impar()
"""

#    d) Faça uma função para exibir os números de 20 a 0.

""""
def vinte_zero():
  n = 20
  while n > -1:
    print(n)
    n -= 1
vinte_zero()
"""

#e) Faça uma função para somar os números de 3 a 10.

""""
def soma():
  somar = 3
  n = 3
  while n <= 10:
     print(somar)
     n = n + 1
     somar += n
soma()
"""

#f) Faça  uma função para somar os números pares de 4 a 20.

"""
def soma_par():
  soma = 4
  par = 4
  while par <= 20:
    print(soma)
    par += 2
    soma += par
soma_par()
"""

#    g) Faça uma função para somar os números ímpares de 10 a 15.

"""
def soma_impar():
  soma = 0
  impar = 10
  while impar <= 15:
    impar += 1
    if impar % 2 != 0:
      soma += impar
      print(soma)
soma_impar()
"""

#h) Faça uma função para multiplicar os números no intervalo fechado de 2 a 5.

"""
def intervalo_fechado():
  numero = 2
  multiplica = 2
  while numero <= 5:
    print(multiplica)
    numero += 1
    multiplica = numero * multiplica
intervalo_fechado()
"""
# 2,6,24,120

#    i) Faça uma função para calcular a média dos números de 1 a 10.

"""
def calcular_media():
  numero = 1
  soma = 1
  media = 0
  while numero <= 10:
    print(media)
    numero += 1
    soma += numero
    media = soma / numero 
calcular_media()
"""

#j) Faça uma função para calcular a média dos números ímpares de 10 a 50.

"""
def media_impar():
  numero = 10
  soma = 0
  media = 0
  while numero < 50:
    numero += 1
    if numero % 2 != 0:
      soma += numero
      media = soma / numero
      print(media)
media_impar()
"""

#k) Faça uma função para calcular a média dos números divisíveis por 5 no intervalo de 10 a 50.

"""
def divisivel():
  numero = 10
  soma = 0
  media = 0
  while numero < 50:
    numero += 1
    if numero % 5 == 0:
      soma += numero
      media = soma / numero
      print(media)
divisivel()
"""

#7) Faça uma função para exibir o seguinte resultado: (Faça a mesma função usando o while e usando o for)
#10.0 11.1,  12.2,  13.3, 14.4,  15.5,  16.6,  17.7, 18.8,  19.9, 20.0

"""
def exibe():
  soma = 0.0
  numero = 10.0
  x = 0.0
  while numero < 21:
    soma = numero + x
    numero += 1
    x += 0.1
    if soma > 20:
      soma = 20.0
    print(soma)
exibe()
"""

"""
def exibe():
  soma = 0.0
  x = 0.0
  for v in range(10,21):
   soma = v + x
   x += 0.1
   if soma > 20:
     soma = 20.0
   print(soma)
exibe()
"""

#8) Faça uma função que receba dois números inteiros positivos (a e b, onde a > b ) e calcule o MDC (Máximo Divisor Comum) usando o processo das
#divisões sucessivas. Exemplo: a= 48 e b=30 - 48/30 = 1 (resto 18) - 30/18 = 1 (resto 12) - 18/12 = 1 (resto 6) - 12/6 = 2 (resto 0),
#logo o MDC (48,30) = 6

"""
def numero_inteiro():
  a = 48
  b = 30
  resto = 0
  while b != 0:
     resto = a % b
     a = b
     b = resto
  print(a)  
numero_inteiro()
"""
#9) Por meio das equações de Pell é possível alcançar uma aproximação inteira para a raiz quadrada de um número inteiro positivo. Para calcular a
#aproximação deve-se subtrair consecutivamente dos resultados do valor a ser extraído a raiz, os números ímpares 1, 3, 5, … até que o valor a ser subtraído
#seja maior que o resultado.
#Exemplo: número = 19
"""
19 – 1 = 18
18 – 3 = 15
15 – 5 = 10
10 – 7 = 3
"""
#O próximo seria 3 – 9, mas como  3 é menor que 9, a sequência deve ser parada.
#Como 4 subtrações foram efetuadas, então a resposta é 4.

"""
def pell():
  numero = 19
  cont = 0
  impar = 1
  resultado = 1
  while resultado < numero:
    impar += 2
    numero = numero - impar
    cont += 1
  print(cont)
pell()
"""

#10) Faça uma função que receba um número n, onde n>=3, e calcule a soma dos n primeiro
#termos da série de fibonacci. Exemplo: n = 5 Série: 0, 1, 1, 2, 3
#→ Soma = 0 + 1 + 1 + 2 + 3 = 7.

"""
def fibonacci():
   n = int(input("Digite um numero: "))
   t1 = 0
   t2 = 1
   term = 1
   n1 = 2
   soma = 0
   soma += term
   while n1 < n:
      n1 += 1
      term = t1 + t2
      t1 = t2
      t2 = term
      soma += term
      term = t1 + t2
   print(soma)
fibonacci()
"""
