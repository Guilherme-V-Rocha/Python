#1. Faça um programa que lê 10 números de ponto flutuante para um vetor e, em seguida, exiba todos oselementos na tela.

"""
def ledez():
    lista = []
    x = 0
    while x < 10:
        x += 1
        numero = float(input("Digite ai"))
        lista += [numero]
    print(lista)
ledez()
"""

#2. Faça um programa que lê 10 números inteiros, armazenando em um vetor o quadrado de cada número lidoe, em seguida,
#exiba todos os elementos na tela.

"""
def ledez():
    lista = []
    x = 0
    while x < 10:
        x += 1
        numero = int(input("Digite ai"))
        lista += [numero ** 2]
    print(quadrado)
ledez()
"""

#3. Faça um programa que lê valores inteiros positivos até que preencha um vetor de 5 posições, entretanto, antes de armazenar o valor,
#deve­se verificar se ele é maior que 0.

"""
def ledez():
    lista = []
    x = 0
    r = False
    while x != 5:
        x += 1
        numero = int(input("Digite ai: "))
        if numero > 0:
            lista += [numero]
            r = True
        else:
            numero < 0
            numero = int(input("Digite ai: "))
    print(lista, r)
ledez()
"""

#4. Dado um vetor de inteiros, faça uma função para cada item (Não é permitido o uso de slice):

#a) retornar em ordem inversa.

"""
def invertido():
    numero = [1,2,3,5,6,7,8,9,10]
    lista_inversa = []
    tamanho = len(numero) -1 
    for x in range(tamanho, -1, -1):
        lista_inversa += [numero[x]]
    print(lista_inversa)
invertido()
"""

#b) retornar somente os pares.

"""
def pares():
    numero = [1,2,3,5,6,7,8,9,10]
    lista_pares = []
    tamanho = len(numero)
    
    for x in range(tamanho):
        if numero[x] % 2 == 0:
            lista_pares += [numero[x]]
    print(lista_pares)
pares()
"""

#c) retornar a soma dos elementos ímpares.

"""
def impar():
    numero = [1,2,3,5,6,7,8,9,10]
    lista_impar = []
    soma = 0
    tamanho = len(numero)
    for x in range(tamanho):
        if numero[x] % 2 != 0:
            soma += numero[x]
            lista_impar += [soma]
    print(lista_impar)
impar()
"""

#d) calcular a média dos elementos.

"""
def media_p():
    numero = [1,2,3,5,6,7,8,9,10]
    tamanho = len(numero)
    soma = 0
    divide = 0
    for x in range(tamanho):
        soma += numero[x]
        divide = soma / numero[x]
    print(divide)
media_p()
"""

#e) retornar o maior valor e sua posição no vetor.

"""
def maior_v():
    numero = [1,2,3,5,10,7,8,9,6]
    maior = 0
    tamanho = len(numero)
    for x in range(tamanho):
        if numero[x] > maior:
            maior = numero[x]
    print(maior)
maior_v()
"""

#f) retornar o menor valor e sua posição no vetor.

"""
def menor_v():
    numero = [10,2,3,5,1,7,8,9,6]
    menor = numero[0]
    tamanho = len(numero)
    for x in range(tamanho):
        if numero[x] < menor:
            menor = numero[x]
    print(menor)
menor_v()
"""

#g) retornar os elementos repetidos.

"""
def repetido():
    numero = [1,2,3,6,6,7,8,9,6,5,5,5]
    tamanho = len(numero) - 1
    repetir = []
    x = 0
    cont = 0
    while x < tamanho:
        x += 1
        for i in range(tamanho):
            if numero[i] == numero[x]:
                cont += 1
        if cont > 1:
            repetir += [numero[x]]
        cont = 0
    print(repetir)
repetido()
"""

#h) retornar os elementos não repetidos.

"""
def n_repetido():
    numero = [1,2,3,6,6,7,8,9,6,5,5,5]
    tamanho = len(numero) - 1
    repetir = []
    x = 0
    cont = 0
    while x < tamanho:
        x += 1
        for i in range(tamanho):
            if numero[i] == numero[x]:
                cont += 1
        if cont == 1:
            repetir += [numero[x]]
        cont = 0
    print(repetir)
repetido()
"""

#i) exibir a frequência de cada elemento.

"""
def frquentai():
    numero = [1,2,3,6,6,7,8,9,6,5,5,5]
    tamanho = len(numero)
    freq = []
    cont = 0
    x =0
    while x < tamanho - 1:
        x += 1
        for i in range(tamanho):
            if numero[x] == numero[i]:
                cont += 1
        if numero[x] not in freq:
            freq += [numero[x]]
            print("Numeros: ",freq,"Frequencia: ",cont)
        cont = 0
frequentai()
"""

#5. Faça um programa que lê 7 números inteiros para um vetor, e em seguida, exiba os elementos que são primos.

"""
def sete_i():
    numero = [1,2,3,5,6,7]
    tamanho = len(numero)
    primos = []
    cont = 0
    for x in range(tamanho):
        for i in range(tamanho):
            if numero[x] % numero[i] == 0:
                cont += 1
        if cont == 2:
            primos += [numero[x]]
        cont = 0
    print(primos)
sete_i()
"""

#6. Dado dois vetores distintos de tamanhos aleatórios, retorne um lista com os elementos que estão contidos em ambos os vetores,
#ou seja, faça a intersecção dos vetores.

"""
def comparates():
    numero = [1,2,3,6,6,7,8,9,6,5,5,5]
    numero1 = [1,12,13,16,17,18,10,9,9]
    tamanho = len(numero)
    lista_nova = []
    for x in range(tamanho):
        if numero[x] in numero1:
            lista_nova += [numero[x]]
    print(lista_nova)
comparates()
"""

#7. Dado dois vetores distintos de tamanhos aleatórios, retorne uma lista com os elementos de ambos, sem que ocorra a repetição de um mesmo elemento,
#ou seja, faça a união dos vetores.
"""
def uniao_e_tudo():
    numero = [1,2,3,6,6,7,8,9,6,5,5,5]
    numero1 = [1,12,13,16,17,18,10,9,9]
    tamanho = len(numero)
    lista_nova = []
    uniao = []
    for x in range(tamanho):
        lista_nova = numero1
        lista_nova += [numero[x]]
        tamanho1 = len(lista_nova)
        for i in range(tamanho1):
            if lista_nova[i] not in uniao:
                uniao += [lista_nova[i]]
    print(uniao)
uniao_e_tudo()
"""
#8. Dado um vetor de inteiros, faça uma função para verificar se a sequência é palíndromo (se lida aocontrário resulta na sequência original).

"""
def palindromo():
    numero = [1,0,1]
    inverso = numero[::-1]
    if numero == inverso:
        r = inverso
    else:
        r = "Não é palindromo"
    print(r)
palindromo()
"""

#9. Faça uma função que calcule os dígitos verificadores do CPF. O CPF é composto por 11 dígitos, sendoque os dois últimos são os
#dígitos de verificação. Supondo que os dígitos do CPF sejam representados pora b c d e f g h i ­ d1 d2, para o cálculo de d1 faz­se:

#d1 = (a x 1) + (b x 2) + (c x 3) + (d x 4) + (e x 5) + (f x 6) + (g x 7) +  (h x 8)  + (i x 9)A soma  d1 deve ser operada com
#módulo 11 (resto da divisão por  11), e o resultado representa o dígito verificador, se o resultado for 10, toma­se por 0.
#d2 =(a x 0) + (b x 1) + (c x 2) + (d x 3) + (e x 4) + (f x 5) + (g x 6) +  (h x 7)  + (i x 8) + (d1 x 9)
#A soma d2 deve ser operada com módulo 11 (resto da divisão por 11), e o resultado representa o dígito verificador, se o resultado for 10, toma­se por 0.

"""
def verificador():
    cpf = [0,6,7,1,7,3,2,1,9]
    digito1 = []
    digitos_v = []
    d1 = (cpf[0] * 1) + (cpf[1] * 2) + (cpf[2] * 3) + (cpf[3] * 4) + (cpf[4] * 5) + (cpf[5] * 6) + (cpf[6] * 7) +  (cpf[7] * 8)  + (cpf[8] * 9)
    digito = d1 % 11
    if digito == 10:
        digito = 0
    d2 = (cpf[0] * 0) + (cpf[1] * 1) + (cpf[2] * 2) + (cpf[3] * 3) + (cpf[4] * 4) + (cpf[5] * 5) + (cpf[6] * 6) +  (cpf[7] * 7)  + (cpf[8] * 8) + (digito * 9)
    digito1 = d2 % 11
    if digito1 == 10:
        digito1 = 0
    digitos_v = [digito,digito1]
    print("Os digitos verficador é:", digitos_v)
verificador()
"""

#10. Faça uma função que receba um vetor e verifique se os elementos estão em ordem decrescente. A função deve retornar um valor True ou False.

"""
def descrescente():
    numero = [1,2,3,6,6,7,8,9,6,5,5,5,5]
    tamanho = len(numero)
    l_numero = numero[0]
    r = True
    while r != False:
        for x in range(tamanho):
            if numero[x] < l_numero:
                l_numero = numero[x]
            else:
                r = False
    print(r)
descrescente()
"""
