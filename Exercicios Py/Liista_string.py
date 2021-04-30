import math
import os

"""
Professora: Juliana G. Souza
Aluno: Guilherme Vieira Rocha
Turma: 1° Periodo - TADS
Data: 01/06/2020
"""

#1. Faça uma função que retorne a quantidade de espaços em uma frase.
   
"""
def q_espaco(frase):
    c_espaco = 0
    for x in frase:
        if x == " ":
            c_espaco += 1
    return c_espaco
print(q_espaco("A batata nasceu morrendo de dor"))
"""

#2. Faça uma função que recebe uma frase e retorne a quantidade de palavras. Considere que as palavras estão separadas por espaço e não há pontuação.

"""
def q_palavras(frase):
    cont_palavra = 1
    for x in frase:
       if x == " ":
           cont_palavra += 1
    return cont_palavra
print(q_palavras("batata nasceu morrendo de dor enquanto chorava de água esparramada"))
"""

        
#3. Faça uma função que recebe uma frase e retorne o percentual de vogais.

"""
def per_vogais(frase_i):
    tamanho = len(frase_i)
    cont_vogais = 0
    for x in frase_i:
      if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
          cont_vogais += 1
      else:
          cont_vogais += False
    percentual = (tamanho * cont_vogais) / 100
    return percentual
print(per_vogais("A batata nasceu morrendo de dor enquanto chorava de água esparramada"))
"""

#4. Faça uma função que recebe duas strings e retorne a string de maior tamanho.

"""
def quevenceu(frase,frase1):
    tan = len(frase)
    tan1 = len(frase1)
    if tan > tan1:
        x = "A texto 1 é maior que o texto 2"
    elif tan1 > tan:
        x = "texto 2 é bem maior que o text 1 "
    else:
        tan == tan1
        x = "os dois texto possuem o mesmo tamanho"
    return x
print(quevenceu("A batata moleu", "Mentira que a batata moleu"))
"""

#5. Faça uma função que recebe uma palavra e verifique se é palíndromo. Um palíndromo significa que a leitura da palavra ao contrário é idêntica a palavra.

"""
def vouve_Te_aviso(frase):
    inverte_ai = frase[::-1]
    x = False
    if frase == inverte_ai:
        x = True
    return x
print(vouve_Te_aviso("ata"))
"""

#6. Faça uma função que recebe um número e retorne o número invertido.

"""
def to_invertendo(numenor):
    ja_inverti = numenor[::-1]
    return ja_inverti
print(to_invertendo("45"))
"""

#7. Faça uma função que recebe uma frase e verifique se a quantidade de abre parênteses "(" é igual aquantidade de fecha parênteses ")" .
#Desafio: Modifique a função para verificar se os parênteses "combinam" corretamente.

"""
def vou_contar_parenteses(frase):
    contador = 0
    contador1 = 0
    #parente = "("
    #parente1 = ")"
    r = False
    for x in frase:
       if x == "(":
        contador += 1
       elif x == ")":
        contador1 += 1
       else:
           contador == contador1
           r = True
    return r
print(vou_contar_parenteses("AAAAAAA(AAAAAAAAAAA(AAAAAAAAAA)AAAAAAAAA)"))
"""
#8. Faça uma função que recebe um número romano e transforme em um número decimal.

"""
def numenor_romano(frase):
    if frase == "I":
        x = float(1)
    elif frase == "II":
        x = float(2)
    elif frase == "III":
        x = float(3)
    elif frase == "IV":
        x = float(4)
    elif frase == "V":
        x = float(5)
    elif frase == "VI":
        x = float(6)
    elif frase == "VII":
        x = float(7)
    elif frase == "VIII":
        x = float(8)
    elif frase == "IX":
        x = float(9)
    elif frase == "X":
        x = float(10)
    return x
print(numenor_romano("IV"))
"""

#9. Faça uma função que receba uma palavra e um sufixo. Verifique se a palavra contém o sufixo informado.
#Exemplos: palavra = "dominando" sufixo = "ando" --> Resposta: True, palavra = "dominando" sufixo = "indo" --> Resposta: False.

"""
def tovendo(palavra, sufixo):
    if sufixo in palavra:
        resposta = True
    else:
        resposta = False
    return resposta
print(tovendo("dominando", "ando"))
"""

#10. Faça um programa que simule o jogo de forca. O jogo consiste em fornecer uma palavra secreta e a quantidade de caracteres (você escolhe a palavra).
#O usuário deve tentar adivinhar as letras e errar no máximo 7 vezes. O oitavo erro implica no enforcamento.

"""
def ovoTedeforca():
    palavra_secreta = "MACACOS"
    chances = 0
    tamanho = len(palavra_secreta)
    acerto = 0
    v = ""
    while acerto < tamanho and chances < 8:
        letra = str(input("Digite a letra: "))
        if letra in palavra_secreta:
            acerto += 1
            print("PARABÉNS...")
        else:
            chances += 1
            print("ERROU BIXO")
    if acerto == tamanho:
        print("tu ganhou: ", palavra_secreta)
    else:
        chances == 8
        print("ERROU BIXU teje enforcado")
ovoTedeforca()
"""
#11. Faça uma função que receba um nome completo e devolva a inicial de cada nome em maiúsculo e o restante das letras em minúsculo.

"""
def q_espaco(nome):
    nomeM = nome[0].upper()
    tamanho = len(nome)
    for x in range(1,tamanho,1):
        if nome[x] == " ":
            nomeM += " "
            nomeM += nome[x + 1].upper()
        else:
            nomeM += nome[x]
    return nomeM
print(q_espaco("guilherme vieira rocha"))
"""

#12. Faça uma função que retorne a última vogal de uma string. Caso não haja vogais, deve ser retornado o valor None. Desconsidere os acentos.

"""
def retornando(palavra):
    vogal = ""
    for x in palavra:
        if x == "a" or x == "A":
            vogal = "a"
        elif x == "e" or x == "E":
            vogal = "e"
        elif x == "i" or x == "I":
            vogal = "i"
        elif x == "o" or x == "O":
            vogal = "o"
        elif x == "u" or x == "U":
            vogal = "u"
        else:
            vogal = None
    return vogal
print(retornando("Guilherme Vieira Rochu"))
"""

#13. Faça uma função que recebe uma data no formato "dd/mm/ano" e verifique se é válida.

"""
def voEverifico(data):
    r = False
    teste = data[:2]
    teste1 = data[3:5]
    teste2 = data[6:]
    if teste <= "31":
        if teste1 <= "12":
            if teste2 <= "2021":
                r = True
    return r
print(voEverifico("31/12/2002"))
"""

#14. Faça uma função que substitua um determinado caracter por outro em uma string. A função deve receber a string, o caracter a ser substituído e o novo
#caracter. Por exemplo, em "agua", substituir todos os "a" por "e", produz "egue".

"""
def trocas(frase):
    t = "e"
    troca = ""
    tamanho = len(frase)
    for x in range(0, tamanho):
        letras = frase[x]
        if letras == "a":
            troca += t
        else:
            troca += letras
    return troca
print(trocas("agua"))
"""

#15. Faça uma função que elimine espaços em branco à esquerda e direita de uma variável do tipo string.

"""
def obtelariti(palavra):    
    corta = ""
    for x in palavra:
        if x != " ":
            corta += x
    return corta
print(obtelariti(" batata a"))
"""

#16. Faça uma função que devolva a maior palavra em uma frase. Considere que a frase contém apenas as pontuações: vírgulas(,) e . ponto final (.).

"""
def maior_palavra(frase):
    tamanho = len(frase)
    maior = frase[0]
    letra = ""
    i = 0
    for x in range(tamanho):
        if frase[x] == " " or frase[x] == "," or frase[x] == ".":
            i += 1
            maior += frase[i : x + 1]
            letra += maior
    return maior, letra
print(maior_palavra("batatata, ratatatata"))
"""
