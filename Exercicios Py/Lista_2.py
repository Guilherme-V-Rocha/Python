import math

"""
Professora: Juliana G. Souza
Aluno: Guilherme Vieira Rocha
Turma: 1° Periodo - TADS
Data: 25/03/2020
Lista 2 - comandos condicionais
"""

#1.Fazer um algoritmo que leia a capacidade de um elevador e o peso de 5 pessoas individualmente. O algoritmo deve retornar se o elevador está liberado
#para subir ou se excedeu a carga máxima.

"""
def elevador(peso1, peso2, peso3, peso4, peso5):
 total = peso1 + peso2 + peso3 + peso4 + peso5
 if total < 450:                                                   
    c = "Liberado para subir"
 else:
    c = "Execedeu a carga maxima"
    return c, total
def main():
  p1 = float(input("Digite o peso da primeira pessoa: "))
  p2 = float(input("Digite o peso da segunda pessoa: "))
  p3 = float(input("Digite o peso da terceira pessoa: "))
  p4 = float(input("Digite o peso da quarta pessoa: "))
  p5 = float(input("Digite o peso da quinta pessoa: "))
  result = elevador(p1, p2, p3, p4, p5)
  print(result)
main()
"""

#2.Escreva um programa que leia um número e informe se ele é ou não divisível por 3 e por 7.

"""
def divisivel(num1):
    if num1 % 3 == 0 and num1 % 7 == 0:
        n = "eh divisivel por 3 e por 7 "
    else:
        n = "nao e divisivel por 3 e por 7"
        return n
def main():
 x = float(input("Digite um numero: "))
 result = divisivel(x)
 print(result)
main()
"""

#3.Ler 4 notas, calcular a média e apresentar as mensagens “Aprovado” ou “Reprovado” conforme o resultado da média encontrada.
#Para aprovação, a média deverá ser maior ou igual a 7.

"""
def media_aluno(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 70:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        return situacao
def main():
  n1 = float(input("Digita a nota da primeira prova: "))
  n2 = float(input("Digita a nota da segunda prova: "))
  n3 = float(input("Digita a nota da terceira prova: ")) 
  n4 = float(input("Digita a nota da quartaa prova: "))
  result = media_aluno(n1, n2, n3, n4, n5)
  print(result)
main()
"""

#4.Dados dois números apresentar 60% da diferença do maior pelo menor valor.
def m_m(n1,n2):
    calculo = (n1 - n2) - 60 
    return calculo
def main():
    x = float(input("Digite um numero: "))
    x1 = float(input("Digite um numero: "))
    result = m_m(x, x1)
    print(result)
main()

#5.Ler 2 números inteiros do teclado (NUM1 e NUM2), verificar e imprimir qual deles é o maior, ou a mensagem “Os números são iguais”, caso realmente sejam.

#6.Considere que uma determinada operadora de telecomunicaçõesdisponibiliza aos seus clientes o seguinte plano tarifário:
              #Preço por minuto = R$ 0,30 – para os 10 primeiros minutos;
              #11º minuto e seguintes cobrados a R$ 0,05 por minuto.
#Faça um algoritmo que leia a duração da chamada em minutos eapresente o tempo de duração da chamada em horas e minutos e opreço a pagar pela chamada.

#7.As maçãs custam R$0,80 cada se forem compradas menos de uma dúzia e R$ 0,70 se forem compradas pelo menos 12.
#Escreva uma lgoritmo que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

#8.Ler 4 números inteiros e calcular a soma apenas dos que forem pares.

#9.Fazer um algoritmo para ajudar a bilheteria do metrô.  O passageiro deveinformar o tipo do bilhete que deseja comprar (unitário, duplo ou 10viagens),
#bem como o  valor entregue ao vendedor. O sistema   devemostrar, então, a  quantidade de bilhetes possíveis e o troco que opassageiro deve receber.
#Considere a seguinte tabela de preço:
   #Bilhete unitário ........................................1,30
   #Bilhete duplo ............................................2,60
   #Bilhete de 10 viagens ............................12,00

#10.Faça um programa que leia o salário de um funcionário e calcule seu novo salário baseado na seguinte regra:
    #Salários até R$ 800,00, reajuste de 10%;
    #Salários   acima   de R$800,00 e menores que R$1.500,00,reajuste de 7,5%.
    #Salários de R$ 1.500,00 para cima, reajuste de 5%.

#11.Ler um nome do teclado e ver se é igual ao seu nome. Imprimir conformeo caso: “NOME CORRETO” ou “NOME INCORRETO”.

#12.Elabore um algoritmo que dada a idade de um nadador classifica-o emuma das seguintes categorias:
  #5 - 7 anos infantil A
  #8 -10 anos infantil B
  #11 –13 anos juvenil A
  #14 - 17 anos juvenil B
  #maiores   ou   igual   a   18 anos Adulto

#13.Elaborar um algoritmo que lê 3 valores a,b,c e os escreve. A seguir,encontre o maior dos 3 valores e o escreva com a mensagem: "É o maior".

#14.Faça um algoritmo que leia um número qualquer. Caso o número seja parmenor que 10, escreva 'Número par menor que Dez', caso o número digitado seja
#ímpar menor que 10 escreva 'Número Ímpar menor que Dez', caso contrário Escreva 'Número fora do Intervalo'.

#15.Dado o salário de um funcionário, elabore um algoritmo que efetua o cálculo do reajuste deste salário. Considere que o funcionário deveráreceber um
#reajuste de 15% para salário inferior a R$500,00. Se o salário for maior ou igual que R$500,00, mas menor ou igual que R$1000,00 seu reajuste será de 10% e
#caso seja maior que R$ 1000,00 oreajuste é de 5%.

#
