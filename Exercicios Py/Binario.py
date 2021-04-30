import math

"""
Aluno: Guilherme V. Rocha
Professora: Juliana G. Souza
Turma: 1° Periodo - TADS
Atividade EAD 3
"""


def bina():
   decimal = int(input("Digite um numero: "))
   binario = 0
   while decimal != 0:
      binario = decimal % 2
      decimal = decimal // 2
      print(binario)
bina()
