import math

"""
Professora: Juliana G. Souza
Aluno: Guilherme V. Rocha
Turma: 1°Periodo - TADS
Data: 10/05/2020
Lista: Atividade EAD 4
"""

#1.  Faça uma função para cada letra que receba o raio, calcule e mostre:
#a) a área de uma esfera, sabe­se que A = 4piR²

"""
def esfera(raio):
    pi = math.pi
    a = 4 * pi * (raio ** 2)
    return a
def main():
    x = float(input("Digite o raio da esfera: "))
    area = esfera(x)
    print("A area da esfera é de ", area)
main()
"""
#b) o volume de uma esfera, sabe­se que V = (4piR³)/3

"""
def esfera(raio):
    pi = math.pi
    v = (4 * pi * (raio ** 2)) / 3
    return v
def main():
    x = float(input("Digite o raio da esfera: "))
    volume = esfera(x)
    print("A Volume da esfera é de ", volume)
main()
"""

#2. Goku recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as contas estão atrasadas, 
#Goku terá de pagar multa de 2% sobre cada conta por dia de atraso. Faça:
#a) uma função para calcular o valor de cada multa.
#b) uma função para calcular o restante do salário após o pagamento das multas.

"""
def pagamento(multa,salario):
    multa_dia = (multa * 2 ) / 100
    resto_salario = salario - multa_dia
    return multa_dia, resto_salario
def main():
    x = float(input("Digite o valor da multa: "))
    x1 = float(input("Digite o seu salario: "))
    multa, salario = pagamento(x, x1)
    print("A valor da sua multa após o atraso do pagamento é de ", multa, "e seu salario descontado após o pagamento da multa atrasado é ", salario)
main()
"""

#3. Faça um programa que receba a altura(h) e o sexo de uma pessoa e que calcule e mostre o seu peso ideal, 
#utilizando as seguintes fórmulas: 
#• para homens: (72.2*h) – 58
#• para mulheres: (62.1*h) – 44.7

"""
def peso_ideal(genero, altura):
    if genero == "H":
       peso = (72.2 * altura) - 58
    else:
       genero == "M"
       peso = (62.1 * altura) - 44.7
    return peso
def main():
    print(" H para homens e M para mulheres ")
    x = str(input("Digite o genero se é homem ou mulher: "))
    x1 = float(input("Digite a sua altura: "))
    peso = peso_ideal(x, x1)
    print("O seu peso ideal é : ", peso)
main()
"""

#4. Faça uma função que receba o salário de um funcionário e, usando a tabela a seguir, calcule e mostre o valor do  novo salário.
#Salário                Percentual de aumento (%)
#R$ 300,00             | 15
#R$ 300,00 a R$ 600,00 | 10
#R$ 600,00 a R$ 900,00 | 5
#Acima R$ 900,00       | 2

"""
def salario_novo(salario):
    if salario <= 300:
        salario_n = salario + (salario * 15) / 100
    elif salario > 300 and salario <= 600:
        salario_n = salario + (salario * 10) / 100
    elif salario > 600 and salario <= 900:
        salario_n = salario + (salario * 5) / 100
    else:
        salario > 900
        salario_n = salario + (salario * 2) / 100
    return salario_n
def main():
    x = float(input("Digite o seu salário: "))
    novo_salario = salario_novo(x)
    print("O valor do seu novo salário é de: ", novo_salario)
main()
"""

#5. Faça um programa que leia para N funcionários o nome e o salário, e retorne: o maior salário, o menor salário e a média salarial.

"""
def mmm():
   n = int(input("Quantos funcionarios tem na empresa: "))
   nome = input("Digite o nome do funcionario: ")
   salario = int(input("Digite o salario: "))
   contador = 0
   maior_salario = salario
   menor_salario = salario
   media = 0
   while contador < n :
      contador += 1
      nome = input("Digite o nome do funcionario: ")
      salario = int(input("Digite o salario: "))
      if salario > maior_salario:
         maior_salario = salario
      else:
         menor_salario < salario
         menor_salario = salario
   media = maior_salario / 2      
   print(maior_salario, media, menor_salario, )
mmm()
"""


#6. Faça um programa que leia para N funcionários o nome, o sexo e o salário, e imprima o maior salário masculino, o maior salário feminino, 
#a média salarial masculina e a média salarial feminina.

"""
def mGenero():
   n = int(input("Quantos funcionarios tem na empresa: "))
   nome = input("Digite o nome do funcionario: ")
   genero = input("Digite seu genero: ")
   salario = int(input("Digite o salario: "))
   maior_salario = salario
   maior_salariom = salario
   media = 0
   mediam = 0
   contador = 1
   while contador < n:
     contador += 1 
     nome = input("Digite o nome do funcionario: ")
     genero = input("Digite seu genero: ")
     salario = int(input("Digite o salario: "))
     if genero == "H":
        if salario > maior_salario:
           maior_salario = salario
     media = maior_salario / 2
     if genero == "M":
        if salario > maior_salariom:
           maior_salariom = salario
     mediam = maior_salariom / 2
   print("Media salario Masculino: ", media, "Maior salario Masculino", maior_salario, "\n Media salario Feminino: ", mediam, "Maior salario feminino: ", maior_salariom)
mGenero()
"""

#7. Faça um programa que leia valores inteiros positivos do usuário até que seja digitado um valor maior que o dobro do anterior.

"""
def inteiro():
   numero = int(input("Digite um numero inteiro: "))
   cont = numero * 2
   while numero > 0:
      cont = numero * 2
      numero = int(input("Digite um numero inteiro: "))
      if cont == numero:
         print("O numero digitado é dobro do anterior", cont)
         break
inteiro()
"""

#8. Faça um programa que leia valores inteiros do usuario até que seja digitado dois números iguais. Deve­se retornar a soma dos valores lidos 
#sem considerar os valores iguais. Seja o primeiro a mandar uma mensagem para a professora com o código manga com leite e ganhe pontos extras.

"""
def lendo():
   inteiro = int(input("Digite o numero: "))
   ig = inteiro
   soma = 0
   cont = 0
   while inteiro > 0:
      cont += 1
      inteiro = int(input("Digite o numero: ")) 
      if inteiro == ig:
         soma = inteiro + cont
         print(soma)
lendo()
"""

#9. Faça um programa que receba a idade, o peso, a altura , 
#a cor dos olhos (A – Azul, P –Preto, V-Verde e C – Castanho) e a cor dos cabelos (P – Preto, C – Castanho, L –Louro e R – Ruivo) de 8 pessoa e calcule:
 #• a quantidade de pessoa com idade superior a 50 anos e peso inferior a 60 quilos;
 #• a média das idades das pessoas com altura inferior a 1,50;
 #• a percentagem de pessoas com olhos azuis entre todas as pessoas analisadas;
 #• a quantidade de pessoas ruivas e que não possuem olhos azuis.

""
def recebendo():
    m = 0
    im = 0
    c = 0
    porcentagem = 0
    for i in range(2):
     idade = int(input("Digite a idade: "))
     peso = float(input("Digite o peso: "))
     altura = float(input("Digite a altura: "))
     cor_olhos = input("Digite a cor do olhos: ")
     cor_cabelo = input("Digite a cor do cabelo: ")
     if idade > 50 and peso < 60:
        m+=1
     elif altura < 1.50:
        im += 1
     elif cor_olhos == ("A" or "P" or "V" or "C"):
        porcentagem = (cor_olhos * m ) / 100
     else:
        cor_cabelo == ("P" or "C" or "L" or "R") and cor_olhos != "A"
        c += 1
     print(m, im, c, porcentagem)
recebendo()
""

#10. Faça um programa para uma loja que leia o nome do produto, o preço e a quantidade até que seja digitado o código ­1. 
#Retorne o valor total em mercadorias da loja.

"""
def mercado():
   n_produto = input("Digite o nome do produto: ")
   preco = float(input("Valor do produto: "))
   q_produto = int(input("Quantidade de produto: "))
   valor_total = 0
   while q_produto > 0:
      valor_total = q_produto * preco
      q_produto = int(input("Quantidade de produto: "))     
   print(valor_total)
mercado()
"""
