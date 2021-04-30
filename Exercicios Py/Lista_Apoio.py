#Lista de apoio

def avaliacao(nota1, nota2, nota3):
    media = (nota1+nota2+nota3)/3
    if media >= 7:
        s = "Aprovado"
    elif media >= 5:
        s = "Recuperação"
    else:
        s = "reprovado"
    return media, s
def main():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    m, s = avaliacao(n1,n2,n3)
    print("A media é: ",m)
    print("A situacao do aluno é: ",s)
main()    

def diagnostico(espirro, coriza, dor_cabeca, temperatura):
    if (espirro = "s") and (coriza == "s") and (dor_cabeca == "n") and ((temperatura > 37) or (temperatura < 36.5)):
      d = "pneumonia"
    elif (espirro == "s") and (coriza == "s") and (dor_cabeca == "n") and ((temperatura > 37) and (temperatura <= 36.5)):
      d = "resfriado"
    elif (espirro == "s") and (coriza == "s") and (dor_cabeca == "s") and ((temperatura >= 37) and (temperatura <= 36.5)):
      d = "bronquite"
    else:
        
