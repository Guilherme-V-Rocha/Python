"""
    JOgo da velha
    Autor: joão Vitorino da Silva Faccin Coelho
    E-mail: j.vitorino2008@gmail.com
    Curso: Técnico em Informática integrado ao Ensino Médio.
    Ano: 1
"""
import random

def cria_matriz():
    tamanho_matriz = 3
    elemento = "."
    matriz = []
    matriz_cria = []
    for b in range (tamanho_matriz):
        matriz_cria = []
        for a in range (tamanho_matriz):
            matriz_cria.append(elemento)
        matriz.append(matriz_cria)
    return matriz

def exibe_matriz(matriz):
    linhas = len(matriz)
    colunas = len (matriz[0])
    for a in range (linhas):
        print("")
        for b in range(colunas):
            print(matriz[a][b],end=" ")

def matriz_instrucao ():
    matriz = cria_matriz()
    matriz [0][0] = 7
    matriz [0][1] = 8
    matriz [0][2] = 9
    matriz [1][0] = 4
    matriz [1][1] = 5
    matriz [1][2] = 6
    matriz [2][0] = 1
    matriz [2][1] = 2
    matriz [2][2] = 3
    matriz_instrucao = matriz
    return matriz_instrucao

def intrucao():
    print('\n',"O numero corresponde ao local que deve ser colocado o simbolo")

def um (matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [2][0] = jogador
    return matriz

def dois(matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [2][1] = jogador
    return matriz

def tres(matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [2][2] = jogador
    return matriz

def quatro(matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [1][0] = jogador
    return matriz

def cinco(matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [1][1] = jogador
    return matriz

def seis(matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [1][2] = jogador
    return matriz

def sete(matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [0][0] = jogador
    return matriz

def oito(matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [0][1] = jogador
    return matriz

def nove(matriz_jogo,jogador):
    matriz = matriz_jogo
    matriz [0][2] = jogador
    return matriz

def resultado(matriz,estado_jogo):
    m = matriz
    vencedor = 0
    if matriz [0][0] == matriz [0][1] and matriz [0][1] == matriz [0][2]  :#linha 0
        vencedor = matriz [0][0]
        estado_jogo = False
    elif matriz [1][0] == matriz [1][1] and matriz [1][1] == matriz [1][2]:#linha 1
        vencedor = matriz [1][0]
        estado_jogo = False
    elif matriz [2][0] == matriz [2][1] and matriz [2][1] == matriz [2][2]:#linha 2
        vencedor = matriz [2][0]
        estado_jogo = False
    elif matriz [0][0] == matriz [1][0] and matriz [1][0] == matriz [2][0]:#coluna 0
        vencedor = matriz [0][0]
        estado_jogo = False
    elif matriz [0][1] == matriz [1][1] and matriz [1][1] == matriz [2][1]:#coluna 1
        vencedor = matriz [0][1]
        estado_jogo = False
    elif matriz [0][2] == matriz [1][2] and matriz [1][2] == matriz [2][2]:#coluna 2
        vencedor = matriz [0][2]
        estado_jogo = False
    elif matriz [0][0] == matriz [1][1] and matriz [1][1] == matriz [2][2]:#diagonal 1
        vencedor = matriz [0][0]
        estado_jogo = False
    elif matriz [0][2] == matriz [1][1] and matriz [1][1] == matriz [2][0]:#diagonal 2
        vencedor = matriz [0][2]
        estado_jogo = False
    return vencedor,estado_jogo

def jogabilidade():
    matriz = matriz_instrucao ()
    m = matriz_instrucao ()
    intrucao()
    estado_jogo = True
    batata = 0
    vence = resultado(matriz,estado_jogo)
    lista_jogadas = [" "]
    cont = 0
    numeros_disponiveis=[1,2,3,4,5,6,7,8,9]
    while estado_jogo == True :
        if cont >= 9 :
            estado_jogo = False
            print("Deu velha")
            break
        exibe_matriz(matriz)
        jogador_x = int(input("Digite a posição da sua jogada (jogador X):")) # jogador X
        jogador = "X"
        print('\n')
        for verifica in range (len(numeros_disponiveis)-1):
            compara=numeros_disponiveis[verifica]
            if jogador_x == compara:
                del(numeros_disponiveis[verifica])
        print("Disponiveis: ",numeros_disponiveis)
        if jogador_x == 1:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado  ")
                estado_jogo = False
                break
            else:
                jogada = um(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        elif jogador_x == 2:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = dois(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        elif jogador_x == 3:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = tres(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        elif jogador_x == 4:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = quatro(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        elif jogador_x == 5:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = cinco(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        elif jogador_x == 6:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = seis(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        elif jogador_x == 7:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = sete(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        elif jogador_x == 8:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = oito(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        elif jogador_x == 9:
            if jogador_x in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = nove(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_x)
        vence,estado_jogo = resultado(matriz,estado_jogo)
        if vence == "X" or vence == "O":
            print("o jogador",jogador,"venceu")
            return batata
        exibe_matriz(matriz)
        print('\n')
        cont += 1
        if cont >= 9 :
            estado_jogo = False
            print("Deu velha")
            break
        #
        if cont >= 9 :
            estado_jogo = False
            print("Deu velha")
            break
        jogador_o =random.choice(numeros_disponiveis)             #jogador O
        for verifica in range (len(numeros_disponiveis)-1):
            compara=numeros_disponiveis[verifica]
            if jogador_o == compara:
                del(numeros_disponiveis[verifica])
        print("Disponiveis: ",numeros_disponiveis)
        jogador = "O"
        if jogador_o == 1:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado  ")
                estado_jogo = False
                break
            else:
                jogada = um(matriz,jogador_o)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        elif jogador_o == 2:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = dois(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        elif jogador_o == 3:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = tres(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        elif jogador_o == 4:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = quatro(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        elif jogador_o == 5:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = cinco(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        elif jogador_o == 6:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = seis(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        elif jogador_o == 7:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = sete(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        elif jogador_o == 8:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = oito(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        elif jogador_o == 9:
            if jogador_o in lista_jogadas:
                print ("Jogada incorreta o jogo sera encerrado ")
                estado_jogo = False
                break
            else:
                jogada = nove(matriz,jogador)
                matriz_jogo = jogada
                lista_jogadas.append (jogador_o)
        vence,estado_jogo = resultado(matriz,estado_jogo)
        if vence == "X" or vence == "O":
            print("o jogador",jogador,"venceu")
        cont += 1
        if cont >= 9 :
            estado_jogo = False
            print("Deu velha")
            break
    exibe_matriz(matriz)

def main():
    jogabilidade()
main()
