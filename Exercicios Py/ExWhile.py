import math

#1. Faça um programa que peça um nota. entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.

"""
x = int(input("Digite"))
while x < 0 or x > 10:
    x = int(input("Digite"))
    print(x, " Numero invalido")
"""

#2. Supondo que a população de um pais " A " seja ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população " B " seja 200000 habitantes com uma taxa de crescimento de 1.5% Faça um programa que calcule e
# escreva o número de anos necessários para que a população do pais " A " ultrapasse ou iguale a população do pais " B ".
# mantidas as taxas de crescimento.

"""
a = 80000
b = 200000
cont = 0
while a <= b:
  a += a * 1.03
  b += b * 1.015
  cont += 1
print("Para ultrapassar ou igualar B, levará o tolta de ", cont, " anos")
"""


#-----------------------------------------------------

#Data 28/04/2020

#1
"""
a = 90000000
b = 2000000000
cont = 0
while a <= b:
  a += a * 1.03
  b += b * 1.015
  cont += 1
print("Para ultrapassar ou igualar B, levará o tolta de ", cont, " anos")
"""

#2 Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada amassa inicial, em gramas,
#fazer um algoritmo que determine o tempo necessário para que essa massa se torne menor do que 0,5 grama.
#Escreva a massa inicial, a massa final e o tempo calculadoem horas, minutos e segundos.

def m_radiotivo():
    massa_i = 25
    massa_f = 
    
        
