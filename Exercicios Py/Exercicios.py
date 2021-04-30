import math

"""
  Professora Juliana Goncalves de Souza
  Aluno Guilherme Vieira Rocha
  Turma 1°Periodo Curso TADS
  Data 10/03/2020
"""

#1) dado três numero de entrada, faça funcões para calcular (a) soma, (b) subtração, (c) multiplicaçâo, (d) divisão.
#a

"""
def soma(a,b,c):
    s = a+b+c
    return s
#b    
def subtracao(a,b,c):
    d = a-b-c
    return d
#c    
def multiplicacao(a,b,c):
    e = a * b * c  
    return e
#d    
def divisao (a,b,c):
    j = a / b / c
    return j
def main():
    o = int(input("Digite um numero: "))
    x = int(input("Digite um numero: "))
    b = int(input("Digite um numero: "))
    resultado = soma(x,b,o)
    batata = subtracao(x,b,o)
    comida = multiplicacao(x,b,o)
    arroz = divisao(x,b,o)
    print(resultado, batata, comida, arroz)
main()
"""

#2) Faça funções para calcular a area e o perímetro da formas geométricas: (a) retângulo, (b) quadrado, (c) círculo, (d) triângulo.
#a

"""
def retangulo(h,b):
   a = b * h
   return a
#b
def quadrado(l,i):
   ba = l * i
   return ba
#c
def circulo(r):
  a = math.pi * r**2
  return a
def triangulo(b,h):
  ar = b * h / 2
  return ar
def main():
   n1 = float(input("Digite um numero: "))
   n2 = float(input("Digite um numero: "))
   resultado_a = retangulo(n1,n2)
   resultado_b = quadrado(n1,n2)
   resultado_c = circulo(n1,n2)
   resultado_d = triangulo(n1,n2)
   print(resultado_a, resultado_b, resultado_c, resultado_d)
main()
"""

#3) Faça uma função para que fornecido apenas o lado de um triângulo equilátero, seja calculada e retornada a área dessa figura.

"""
def triangulo_equilatero_todos_lados(l):
  lado = l**2
  baixo = lado / 4
  area = baixo ** (1/3)
  return area
def triangulo_equilatero_um_lado(a,c):
  um_lado = c**2 - a**2
  return um_lado ** (1/2)
def main():
  base = float(input("Digite: "))
  lado = float(input("Digite: "))
  resultado = triangulo_equilatero_um_lado(base, lado)
  print(resultado)

main()
"""

#4) Faça uma função para calculara a média de um aluno. Sabe-se que a média é composta por 4 avaliações bimestrais.

"""
def calcular_media(a, b, c):
  cal = a + b / 10 + c
  media = (a * 4 + b * 6)/10
  return cal
def main():
  avali1 = int(input("Digite a nota da primeira avaliação: "))
  avali2 = int(input("Digite a nota da segunda avaliação: "))
  avali3 = int(input("Digite a nota da terceira avaliação: "))
  avali4 = int(input("Digite a nota da quarta avaliação: "))
  media_aluno = calcular_media(avali1, avali2)
  print("A média do aluno é: ", media_aluno)
main()"""

#5) Faça uma função que retorne o antecessor e o sucessor de um número inteiro positivo.

"""
def ant_suc (a):
  ant = a - 1
  suc = a + 1
  return ant // suc
def main():
  numero = int(input("Digite um numero: "))
  antece = ant_suc(numero)
  print("O antecessor e o sucessor ", antece)
main()
"""

#6) Retorne a terça parte do quadrado de um número inteiro positivo.

"""
def terca_quadrado(a):
   calculo_1 = 3 * a
   return calculo_1 ** (1/2) 
def main():
   numero1 = int(input("Digite um numero: "))
   calculo = terca_quadrado(numero1)
   print("A terça parte do quadrado é: ", calculo)
main()
"""

#7) Retorne o quadrado e a raíz quadrada de um valor inteiro positivo.

"""
def quadrado(a):
  elevando = a**2
  return elevando
def raiz(b):
  r_quadrado = b
  return r_quadrado ** (1/2)
def main():
  numero1 = int(input("Digite um numero: "))
  calculo_1 = quadrado(numero1)
  calculo_2 = raiz(numero1)
  print("Os valores do quadrado ", calculo_1, " e raiz quadrada é: ", calculo_2)
main()
"""

#8) Faça uma função para calcular a média poderada de  4 valores. 

"""
def valor(a,b,c,d):
  valores = a + b + c + d / 4
  return valores
def main():
  num1 = int(input("Digite um valor: "))
  num2 = int(input("Digite um valor: "))
  num3 = int(input("Digite um valor: "))
  num4 = int(input("Digite um valor: "))
  resultado = valor(num1, num2, num3, num4)
  print("A média ponderada é: ", resultado)
main()
"""

#-----------------------------------------------------
                #Data:24/03/2020

#1. Faça uma função que receba dois números e retorne o maior.

"""
def r_dois_numeros(a,x):
    if a>x:
      return a
      return x
print(r_dois_numeros(5,6))
"""

#ou

"""
def r_dois_numeros(a,x):
   maior = a
   if x>a:
   return x
print(r_dois_numeros(6,5))
"""

#2 Faça uma função que receba dois números e retorne o menor.

"""
def recebe_d_numeros(a,b):
    if a<b:
      return a
def main():
    x = float(input("Digite um numero: "))
    a = float(input("Digite outro numero: "))
    resultado = recebe_d_numeros(x,a)
    print(resultado)
main()
"""

#3 Faça uma função que receba dois números e retorne se são iguais.

"""
def recebe_numeros(a,x):
    if a==x:
        return a,x
    else:
        valor= "são diferentes"
        return valor
print(recebe_numeros(5,4))
"""

#4 Faça uma função para retornar se um número é par.

"""
def par(a):
    if a%2 == 0:
       return si
    else:
       par = "não é par"
       return par
print(pares(2))
"""

#5 Faça uma função que receba quatro notas de um aluno e retorne
#“Aprovado” ou “Reprovado”.

"""
def media(nota1, nota2, nota3, nota4):
    media = 7
    calcular = (nota1 + nota2 + nota3 + nota4) // 4
    if calcular >= 7:
        media = "Aluno Aprovado"
    else:
        calcular < 7
        media = "Aluno Reprovado"
        return media
print(media(10,10,10,10))
"""

#-----------------------------------------------------

#1. Faça uma função que receba dois números e retorne a soma se ambos
#forem iguais ou a subtração se forem diferentes.

"""
def recebendo(a,b):
    valor = 0
    if a == b:
      valor = a + b
    else:
      valor = a - b
      return valor
print(recebendo(4,4))
"""
#2 Faça uma função que receba duas medidas de um retângulo e um
#terceiro parâmetro: “A” ou “P”. A função deve retornar a área se o
#terceiro parâmetro for “A“ ou o perı́metro se for ”P“.
"""
def medindo_retangulo(a,b,p)
    if p == "A":
       area = a * b 
       return area
    else:
        perimetro = a + a + b + b
        return perimetro
"""

#ou

"""
def medindo_retangulo(a,b,p)
    if p == "A":
       resultado = a * b 
    else:
       resultado = a + a + b + b
        return resultado
"""

#3 Faça uma função para calcular a solução de uma equação de segundo
#grau. Se não for possı́vel resolver, retorne uma mensagem dizendo:
#”Não há solução real“.)

"""
def equacao_segundog(a,b,c):
    delta = b - (4*a*c)
    if delta < 0:
        reprovado = "não há solucao real"
        return reprovado
    else:
        x1 =(- b + math.sqtr(delta)) / (2*a)
        x2 =(- b - math.sqtr(delta)) / (2*a)
        return x1,x2
print(equacao_segundog(3,4,5))
"""

#---------------------------------------------------
            #data:25/03/2020
#1.Faça uma função que receba dois números e retorne a soma se forem
#iguais, a subtração se o primeiro for maior que o segundo ou a
#multiplicação se o segundo for maior que o primeiro.
"""
def recebe(a,b):
    if a == b:
       m = a + b
       return m
    elif a > b:
       m1 = a - b
       return m1
    elif b > a:
       m2 = b * a
       return m2
print(recebe(2,4))
"""
#2Faça uma função que aceite como entrada uma medida em
#centı́metros e uma string: “m” (metros), “mm” (milı́metros) ou
#“km” (quilômetros). A função deve converter a medida conforme o
#valor fornecido: m, mm ou km.
"""
def media(m,mm,km):
    valor = km * mm
    valor1 = m * mm
    valor2 = m / km
    valor3 = mm / km
    #return valor, valor1, valor2, valor3
print(media(125,1450,10))
"""
#--------------------------------------------------------

#1.Faça uma função que receba três numeros e retorne o maior.

#2.Em uma empresa, um funcionario recebe 50% de hora-extra se for “vendedor” e 25% se for “gerente”.
#Sabe-se que acima de 44 horas de trabalho semanal ́e considerado hora extra.  Faca uma funcao quecalcule o saĺario semanal de um funcionario.

#3.Faca uma func̃ao que receba a idade e a categoria de habilitacao (A,B ou AB) de uma pessoa.
#Se a pessoa nao tem idade para dirigir,calcule o tempo que falta para a habilita ̧c ̃ao e retorne a mensangem“Faltam N anos para habilita ̧c ̃ao.”.
#Se tem idade para digirir retorneo tipo de veıculo permitido (“A” - Moto, “B” - Carro, “AB” - Carro eMoto).


#--------------------------------------------------------
           #Data 01/04/2020
#1° Exercício

"""
print(range(3,6,1))
range(-2,7,2)
range(1,11)
range(7)
range(-10,-6)
range(0,31,3)
range(6,1,-1)
"""

#2° Exercicio

"""
def tabuada_dois():
    for valor in range(0,11,1):
        cak = valor * 2
        print("2 x ", valor ," = ", cak )
tabuada_dois()
"""

