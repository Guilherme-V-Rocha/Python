#1. faça uma função que some números até que um valor negativo seja digitado.

"""
def soma():
    x = float(input("Digite um numero: "))
    somar = 0
    while x >= 0:
        somar +=  x
        x = float(input("Digite um numero: "))
    print("Você digitou um numero negativo a soma total é de :"somar)
soma()
"""

#2. Faça uma função que recebe um número real e devolva se ele também é um inteiro.
def real_inteiro():
    x = float(input("Digite um numero real: "))
    inteiro = int(x)
    if x == inteiro or x != x:
      print("O numero digitado não é real ou inteiro")
    print(x,inteiro)
real_inteiro()
#3. Faça uma função que recebe tês nomes e devolva um nome composto juntado os três.

#4. Faça uma função que lê nomes de frutas e devolva uma única string com todos os nomes lidos separados por vírgula.

#5. Faça uma função para converter um número interio positivo em binário. Dicas: Use While,
#conversão de inteiro para string e concatenação.




"""
def soma_imp(n1,n2):
    n1 = n1
    soma = 0
    while n1 < n2:
        n1 += 1
        if n1 % 2 != 0 and n1 % 3 != 0:
            soma += n1
    return soma
print(soma)

def soma_imp(n1,n2):
    soma = 0
    for aux in range(n1, n2+1)
      if aux % 2 != 0:
          if aux % 3 != 0:
              soma += aux
    return soma
"""

"""
def media(n):
    soma = 0
    n = 0
    contador = 0
    while n < 5:
        n = float ()
"""

def media():
    soma = 0
    somaf = 0
    cont = 0
    contf = 0
    for valor in range(5):
        nome = input("Dgiye")
        genero = input("")
        idade = int(input(""))
        if genero == "H":
            soma += idade
            cont += 1
        else:
            genero =="M":
            contf += 1
            somaf += idade
    media = soma / cont
    mediaf = somaf / contf
    return media, mediaf
           
           
