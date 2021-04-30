"""
Aluno: João Vitorino da Silva Faccin Coelho
Curso: TADS 1° periodo
Materia: Algoritimos
Lista: 8 - matrizes
"""
def ex1a(m):
    soma=0
    cont=0
    for i in m:
        for j in i:
            soma+=j
            cont+=1
    media=soma/cont
    return media
#print(ex1a([[1,2,3],[4,5,6],[7,8,9]]))

def ex1b(m):
    lista=[]
    for i in m:
        soma=0
        cont=0
        for j in i:
            soma+=j
            cont+=1
        media=soma/cont
        lista.append(media)
    return lista    
#print(ex1b([[1,2,3],[4,5,6],[7,8,9]]))

def ex1c(m):
    lista=[]
    for i in range(len(m)):
        soma=0
        cont=0
        for j in range (len(m[i])):
            soma+=m[j][i]
            cont+=1
        media=soma/cont
        lista.append(media)
    return lista   
#print(ex1c([[1,2,3],[4,5,6],[7,8,9]]))

def ex1d(m):
    linha=0
    coluna=0
    elemento=m[0][0]
    for i in range(len(m)):
        for j in range (len(m[i])):
            compara=m[i][j]
            if compara<elemento:
                elemento=compara
                linha=i
                coluna=j
    return elemento,linha,coluna
#print(ex1d([[9,2,3],[4,6,0],[7,8,9]]))

def ex1e(m):
    linha=0
    coluna=0
    elemento=m[0][0]
    for i in range(len(m)):
        for j in range (len(m[i])):
            compara=m[i][j]
            if compara>elemento:
                elemento=compara
                linha=i
                coluna=j
    return elemento,linha,coluna
#print(ex1e([[1,2,3],[4,5,6],[7,8,9]]))

def ex1f(m):
    maior=0
    identificacao=0
    for i in range(len(m)):
        soma=0
        for j in range(len(m[i])):
            soma+=m[i][j]
            if soma>maior:
                maior=soma
                identificacao=i
    return identificacao
#print(ex1f([[1,2,3],[4,100,6],[7,8,9]]))

def ex1g(m):
    menor=100*100
    identificacao=0
    for i in range(len(m)):
        soma=0
        for j in range (len(m[i])):
            soma+=m[j][i]
        if soma<menor:
            menor=soma
            identificacao=i     
    return identificacao   
#print(ex1g([[-1,0,3],[-1,0,6],[-1,0,-100]]))

def ex1h(m):
    identificacao=0
    maior=0
    for i in range(len(m)):
        soma=0
        for j in range(len(m[i])):
            soma+=m[i][j]
            if soma>maior:
                maior=soma
                identificacao=i
    lista=m[identificacao]
    y=lista[0]
    for x in lista:
        if x<y:
            y=x
    return y
#print(ex1h([[1,2,3],[4,5,6],[7,8,9]]))

def ex1i(m):
    soma=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                soma+=m[i][j]
    return soma
#print(ex1i([[1,2,3],[4,5,6],[7,8,9]]))

def ex1j(m):
    soma=0
    cont=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i+j == len(m[0])-1:
                soma+=m[i][j]
                cont+=1
    soma=soma/cont
    return soma
#print(ex1j([[1,2,3],[4,5,6],[7,8,9]]))

def ex1k(m):
    soma=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i+j < len(m[0])-1:
                soma+=m[i][j]
                print(m[i][j])
    return soma 
#print(ex1k([[1,2,3],[4,5,6],[7,8,9]]))

def ex2a(m):
    soma=0
    cont=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i%2 == 0:
                soma+=m[i][j]
                cont+=1
    soma=soma/cont
    return soma
#print(ex2a([[1,2,3],[4,5,6],[7,8,9]]))

def ex2b(m):
    soma=0
    cont=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j%2 != 0:
                soma+=m[i][j]
                cont+=1
    soma=soma/cont
    return soma
#print(ex2b([[1,2,3],[4,5,6],[7,8,9]]))


def soma_linhas(m):
    acu=0
    soma=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            elemento=m[i][j]
            soma+=elemento
        if i == 0:
            acu=soma
        if soma != acu:
            return False
        soma=0
    return acu  
def soma_colunas(m):
    soma=0
    acu=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            elemento=m[j][i]
            soma+=elemento
        if i == 0:
            acu=soma
        if soma != acu:
            return False
        soma=0
    return acu  
def soma_diadonal_secundaria(m):
    soma=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i+j == len(m[0])-1:
                soma+=m[i][j]
    return soma

def ex3(m):
    if len(m)==len(m[0]):
        soma_linha=soma_linhas(m)
        soma_coluna=soma_colunas(m)
        soma_diadonal_pri=ex1i(m)
        soma_diadonal_secun=soma_diadonal_secundaria(m)
        if soma_linha == soma_coluna and soma_coluna == soma_diadonal_pri and soma_diadonal_pri == soma_diadonal_secun:
            return True
        else:
            return False
    else:
        return False
#print(ex3([[4,9,2],[3,5,7],[8,1,6]]))
#print(ex3([[1,2,3],[4,5,6],[7,8,9]]))

def comp_linhas(m):
    comp=""
    for i in range(len(m)):
        for j in range(len(m[i])):
            elemento=m[i][j]
            comp+=elemento
        if comp == "xxx": 
            msg="Na linha ",i," tem uma sequenia de ",comp[0]
            return msg
        elif comp == "ooo":
            msg="Na linha ",i," tem uma sequenia de ",comp[0]
            return msg
        comp=""
    return False         
def comp_colunas(m):
    comp=""
    for i in range(len(m)):
        for j in range(len(m[i])):
            elemento=m[j][i]
            comp+=elemento
        if comp == "xxx": 
            msg="Na coluna ",i," tem uma sequenia de ",comp[0]
            return msg
        elif comp == "ooo":
            msg="Na coluna ",i," tem uma sequenia de ",comp[0]
            return msg
        comp=""
    return False
def comp_diagonal_principal(m):
    comp=""
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                comp+=m[i][j]
    if comp == "xxx" or comp == "ooo": 
        msg="Na diagonal principal tem uma sequenia de ",comp[0]
        return msg
    return False      
def comp_diadonal_secundaria(m):
    comp=""
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i+j == len(m[0])-1:
                comp+=m[i][j]
    if comp == "xxx" or comp == "ooo": 
        msg="Na diagonal secundaria tem uma sequenia de ",comp[0]
        return msg
    return False

def ex4(m):
    linhas=(comp_linhas(m))
    colunas=comp_colunas(m)
    diagonal_principal=comp_diagonal_principal(m)
    diagonal_secundaria=comp_diadonal_secundaria(m)
    if linhas != False:
        print (linhas)
    elif colunas != False:
        print(colunas)
    elif diagonal_principal != False:
        print(diagonal_principal)
    elif diagonal_secundaria != False:
        print(diagonal_secundaria)
    else:
        print("Não á nenhuma combinação possivel")
#(ex4([["x","o","s"],["o","x","o"],["x","x","z"]]))

def ex5(m):
    iguais=0
    for i in range(len(m)):
        aux=[]
        for j in range(len(m)):
            elemento=m[j][i]
            aux.append(elemento)
        cont=len(aux)
        y=0
        for x in aux:
            if x == aux[0]:
                y+=1
        if y == cont:
            iguais+=1
        y=0
    return iguais
#print("O numero de colunas formadas por um mesmo valor é de: ",ex5([[5,8,3],[1,3,6],[1,3,9]]))
def inserir_notas(materia,bimestre,nota,matriz):
    materia=materia.lower()
    if materia == "al":
        materia = 1
    elif materia == "mat":
        materia = 2
    elif materia == "por":
        materia = 2
    else:
        print("Comando não encontrado. ERRO")
        return matriz
    matriz[materia][bimestre]=nota
    return matriz
def calc_media(matriz):
    medias=[]
    for i in range (1,4,1):
        cont=0
        for j in range (1,5,1):
            cont+=matriz[i][j]
        media=cont/4
        medias.append(media)
    return matriz,medias
def calc_falta_passar(matriz):
    falta=[]
    for i in range(1,4):
        cont=0
        for j in range (1,5):
            cont+=matriz[i][j]
        precisa=24-cont
        if precisa<0:
            precisa=0
        falta.append(precisa)
    return matriz,falta
def notas_abaixo_media(matriz):
    cont=0
    for i in range(1,4):
        for j in range (1,5):
            elemento=matriz[i][j]
            if elemento < 6:
                cont+=1
                print("Nota baixa em: ",matriz[i][0])
                print("Você não esta dentro da media.","\n","A media passa e vc fica","\n")
    if cont == 0:
        print("Parabens, vc não tem notas abaixo da media")
def ex7():
    nome="João"
    m=[[nome,"1°","2°","3°","4°"],["Algoritimos",10,8,9,8],["Matematica",0,0,0,0],["Portugues",0,0,0,0]]
    for i in m:
        print(i)
    print("\n")
    """
    m=inserir_notas("mat",3,5,m)

    m,media=calc_media(m)
    materias=["Algoritimos","Matematica","Portugues"]
    print(materias)
    print("Medias: ",media,"\n")

    m,falta=calc_falta_passar(m)
    materias=["Algoritimos","Matematica","Portugues"]
    print(materias)
    print("Precisa para passar: ",falta,"\n")
    
    notas_abaixo_media(m)
    """
    for i in m:
        print(i)
#ex7()

#Funcão para a criação da matriz (sera usada apenas uma vez)
def cria_matriz(tamanho_matriz):
    elemento = 0
    matriz = []
    matriz_cria = []
    for b in range (tamanho_matriz):
        matriz_cria = []
        for a in range (tamanho_matriz):
            matriz_cria.append(elemento)
        matriz.append(matriz_cria)
    return matriz

def ex8():
    m=cria_matriz(5)
    for i in m:
        print(i)
    print("Escolha a linha e coluna para que as posições ao redor sejam preenchidas com (1)")
    l=int(input("Linha: "))-1
    c=int(input("Coluna: "))-1
    tl=len(m[0])-1
    tc=len(m)-1
    if not(l >= 0 and l <= tl and c >= 0 and c <= tl):
        print("Posição invalida")
    elif l == 0 and c == 0:
        m[l+1][c]=1
        m[l+1][c+1]=1
        m[l][c+1]=1
    elif l == tl and c == tc:
        m[l][c-1]=1
        m[l-1][c-1]=1
        m[l-1][c]=1
    elif l == tl and c == 0:
        m[l-1][c]=1
        m[l-1][c+1]=1
        m[l][c+1]=1
    elif l == 0 and c == tc:
        m[l][c-1]=1
        m[l+1][c-1]=1
        m[l+1][c]=1
    elif l>0 and l<tl and c == 0:
        m[l+1][c+1]=1
        m[l][c+1]=1
        m[l-1][c+1]=1
        m[l+1][c]=1
        m[l-1][c]=1
    elif l>0 and l<tl and c == tc:
        m[l-1][c-1]=1
        m[l][c-1]=1
        m[l+1][c-1]=1
        m[l-1][c]=1
        m[l+1][c]=1
    elif l == 0 and c>0 and c <tc:
        m[l+1][c]=1
        m[l+1][c-1]=1
        m[l][c-1]=1
        m[l][c+1]=1
        m[l+1][c+1]=1
    elif l == tl and c>0 and c <tc:
        m[l][c-1]=1
        m[l-1][c-1]=1
        m[l-1][c]=1
        m[l-1][c+1]=1
        m[l][c+1]=1
    else: 
        m[l-1][c]=1
        m[l-1][c-1]=1
        m[l-1][c+1]=1
        m[l][c+1]=1
        m[l][c-1]=1
        m[l+1][c-1]=1
        m[l+1][c]=1
        m[l+1][c+1]=1
    for i in m:
        print(i)
ex8()




