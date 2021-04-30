import math

"""
Professora: Juliana G. Souza
Aluno: Guilherme Vieira Rocha
Turma: 1° Periodo - TADS
Data: 10/03/2020
Lista 1 - Comandos sequencias e funcoes
"""

#1.Faça um algoritmo que receba um nome, endereço e telefone de uma pessoa e apresente na tela:

"""
def nome(n):
    nome_1 = n
    return nome_1
def endereco(e):
    endere = e
    return endere
def telefone(t):
    tele = t
    return tele
def main():
    nome2 = str(input("Digite um nome: "))
    endereco2 = str(input("Digite um endereco: "))
    telefone3 = float(input("Digite um telefone: "))
    r_nome = nome(nome2)
    r_endereco = endereco(endereco2)
    r_telefone = telefone(telefone3)
    print(r_nome, r_endereco, r_telefone)
    print("O seu nome é ", r_nome , "teu endereco é " , r_endereco , "é o numero do seu telefone é " , r_telefone)
main()   
"""

#2.Faça uma função que calcule a área de um triângulo retângulo.
#Sabe-seque área = (base * altura) / 2. Faça uma função main para ler os valores da base e da altura do usuário.

"""
def triangulo_retangulo(b,h):
    base = b
    altura = h
    calculo = (base * altura) / 2
    return calculo
def main():
    base1 = float(input("Digite o valor da base: "))
    altura1 = float(input("Digite o valor da altura: "))
    resultado = triangulo_retangulo(base1, altura1)
    print(resultado)
    print("O resultado é : ", resultado)
main()
"""
    
#3.Elabore uma função que calcule a área de um círculo. Sabe-se que Área= π*R2, onde R é o raio do círculo (fornecido pelo usuário) e π é o valor de PI(3,1415).
#Os valores de entrada devem ser informados pelo usuário.
"""def circulo(a):
    calculo = math.pi * a ** 2
    return calculo
def main():
    raio = float(input("Digite o valor do raio: "))
    resultado = circulo(raio)
    print(resultado, "cm²")
main()
"""

#4.Dado   um   conjunto   de   valores   (individuais)   que   representam   a quantidade diária de chuva (em polegadas) que caiu na última semana
#(segunda a sexta) em Campo Mourão, faça uma função para converter a quantidade total de chuva da semana em milímetros.
#Sabe-se  que 1 polegada corresponde a 25,4 milímetros.
"""
def polegadas(seg,terca,quarta,quinta,sexta, total):
  polegada = 24.5 *  total
  calcula = (seg * polegada) + (terca * polegada) + (quarta * polegada) + (quinta * polegada) + (sexta * polegada)
  return polegada
def main():
   segunda = float(input("Digita quantidade de chuva do dia: "))
   terca = float(input("Digita quantidade de chuva do dia: "))
   quarta = float(input("Digita quantidade de chuva do dia: "))
   quinta = float(input("Digita quantidade de chuva do dia: "))
   sexta = float(input("Digita quantidade de chuva do dia: "))
   total = float(input("Digite a quantidade de chuva da semana"))
   resultado = polegadas(segunda, terca, quarta, quinta, sexta)
   print(resultado)
main()
"""

#5.Em   épocas   de   pouco   dinheiro,   os   comerciantes   estão   procurandoaumentar as suas vendas oferecendo desconto.
#Faça uma função quepossa receber um valor de um produto e que escreva o novo valor,sabendo-se que foi aplicado um desconto de 9,5%.

"""
def desconto(pro):
    recebe = pro
    valor = (9.5 * prod) / 100
    meu_preco = valor - pro
    return meu_preco
def main():
  produto = float(input("Digite o valor do produto"))
  resultado = desconto(produto)
  print(resultado)
main()
"""

#6.Sabendo-se que para fazer um bolo se utilizam de 4 ovos, ½ Kg defarinha, 200 g de açúcar, 2 latas de creme de leite e 1 litro e ½ de leite,calcule e apresente o custo total do bolo solicitando ao usuário asseguintes informações: preço da dúzia de ovos, do kg de farinha e doaçúcar, da lata de creme de leite e do litro de leite.

"""
def receita(o,f,a,c,l):
   ovo = 4 / o
   farinha = 0.5 / f
   acucar = 200 / a
   creme_leite = 2 / c
   leite = 1.5 / l 
   calculo = ovo + farinha + acucar + creme_leite + leite
   return calculo
def main():
   ovo1 = float(input("Digite o valor do ovo: "))
   farinha1 = float(input("Digite o valor do farinha: "))
   acucar1 = float(input("Digite o valor acucar: "))
   creme_leite1 = float(input("Digite o valor do creme de leite: "))
   leite1 = float(input("Digite o valor do leite: "))
   resultado= receita(ovo1, farinha1, acucar1, creme_leite1, leite1)
   print(resultado)

main()
"""

#7.Faça um algoritmo que leia o preço de um produto, calcule e mostre onovo preço, sabendo-se que este sofreu um desconto de 10%.

"""
def novo_produto (x):
    valor = x
    desconto = 10
    calcula = (valor * desconto)/100
    resu = valor - calcula
    return resu 
def main():
    new_pro = float(input("Digite o valor: "))
    resultado = novo_produto(new_pro)
    print(resultado)
main()
"""

#8.Escrever um algoritmo que lê o nome de um vendedor, o seu salário fixo,o total de vendas por ele efetuada (em reais) e o percentual que eleganha sobre o total de vendas. Calcular o salário total do vendedor,apresentando o seu nome e esse salário.

"""
def calcula_salario(nome,salario_fixo,tolta_vendas,percentual):
     nome_vendedor = nome
     calcula_salario = (tolta_vendas * percentual) / 100
     salario = salario_fixo + calcula_salario
     return salario 
def main():
    nome_vendedo = str(input("Digite seu nome: "))
    salario = float(input("Digite o seu salario fixo: "))
    t_vendas = float(input("Digite o total de vendas: "))
    percentuaal = float(input("Digite o percentual de vendas: "))
    resultado = calcula_salario(nome_vendedo, salario, t_vendas, percentuaal)
    print("o senhor ",nome_vendedo, "o seu salario total é: ", resultado)
main()
"""

#9.Escreva um algoritmo que recebe as dimensões (em metros) de um terreno retangular e em seguida as dimensões de uma casa(também em metros e
#retangular) sobre este terreno. Em seguida calcule e apresentea área livre do terreno, em metros quadrados e em porcentagem.

"""
def dimensoes(l,c,d,a):
    d_terreno = l * c
    d_casa = d * a
    valor = d_terreno - d_casa
    total_terreno = (valor * 100)/ d_terreno
    return valor, total_terro
def main():
    terreno_altura = float(input("Digite a altura do terreno retangular: "))
    terreno_base = float(input("Digte a base do terreno retangular: "))
    casa_altura = float(input("Digite a altura da casa: "))
    casa_base = float(input("Digite a base da casa: "))
    resultado = dimensoes(terreno_altura,terreno_base,casa_altura,casa_base)
    print("A area livre do terreno será de ",resultado ,"m² e a porcentagem será de ",dimensoes(total_terreno))
main()
"""

#10.Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária. Esse trabalhador emitiu dois cheques e agora deseja saber seu
#saldo atual. Sabe-se que cada operação bancária de retirada da conta, paga-se um “imposto” 0,38%. Considere que o saldo inicial da conta antes do
#depósito estava zerado.

"""
def banco(deposito,emite_cheque1,emite_cheque2):
  imposto = 0.0038
  calcular = emite_cheque1 * imposto
  calcula = emite_cheque2 * imposto
  valor = (emite_cheque1 - calcular) + (emite_cheque2 - calcula)
  result = deposito - valor
  saldo = deposito 
  return saldo, result
def main():
  df = float(input("DIGITE O VALOR: "))
  f = float(input("DIGITE O VALOR: "))
  d = float(input("DIGITE O VALOR: "))
  retirad = banco(df,f,d)
  print("O primeiro valor mostra o saldo dele antes e outro valor mostra o saldo atual: ", retirad)
main()
"""

#11.Escreva um algoritmo para um caixa de banco, que recebe um valor inteiro R
#e determina o menor número de notas de 100, 50, 20, 10, 5, 2 e
#1 reais necessários para pagar a quantia R.

"""
def caixa_de_banco(inteiro_real):
    nota100 = inteiro_real // 100
    sobra100 = inteiro_real - nota100 * 100
    nota50 = inteiro_real // 50
    sobra50 = inteiro_real - nota50 * 50
    nota20 = inteiro_real // 20
    sobra20 = inteiro_real - nota20 * 20
    nota10 = inteiro_real // 10
    sobra10 = inteiro_real - nota10 * 10
    nota5 = inteiro_real // 5
    sobra5 = inteiro_real - nota5 * 5
    nota2 = inteiro_real // 2
    sobra2 = inteiro_real - nota2 * 2
    nota1 = inteiro_real // 1
    sobra1 = inteiro_real - nota1 * 1
    notas = nota10,nota50,nota20,nota10,nota5,nota2,nota1
    return  notas
def main():
    numero = int(input("Digite um valor: "))
    result = caixa_de_banco(numero)
    print("numero de notas : ", result)
main()
"""

#12.Elabore um algoritmo que leia o número de horas trabalhadas e o valor do salário mínimo. Calcule e
#escreva o salário a receber seguindo as regras abaixo:
#a)A hora trabalhada vale 1/25 do salário mínimo
#b)O salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
#c)O imposto equivale a 3% do salário bruto;
#d)O salário a receber equivale ao salário bruto menos o imposto.

"""
def horas_(v_salario):
       h_trabalhada = 25
       h_d_trabalho = v_salario / valor
       salario_bruto = h_trabalhada * h_trabalhadas
       s_imposto = s_bruto * (3/100)
       salario_receber = sala_bruto - s_imposto
       return salario_receber
def main():
    s_minimo = float(input("Digite o salario minimo: "))
    resultado = horas_(s_minimo)
    print(": ", resultado)
main()
"""

#13.Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o
#valor do novo salário.

"""
def funcionario(s_mensal, reajuste):
    valor = (s_mensal * reajuste) / 100
    calcule = s_mensal + valor
    return calcule
def main():
    s_mensal = float(input("Digite o salario mensal: "))
    reajuste = float(input("Digite o percentual do reajuste: "))
    resultado = funcionario(s_mensal, reajuste)
    print("O valor do novo salario é ", resultado)
main()
"""

#14.Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa
#de sua irmã. Dados: Distância da casa de Maria até sua irmã: 520 kmSeu carro percorre 12 km com um litro de combustível.
#Ela   abastece   sempre   no   mesmo   posto,   onde   o   preço   do combustível é R$ 3,75 o litro.

"""
def percorre(distancia,litro,posto):
    valor = distancia / litro
    calcule = (distancia / litro) * posto
    return calcule, valor
def main():
    distancia = float(input("Digite a distancia: "))
    litro = float(input("Quantos Litro faz rodando: "))
    posto = float(input("Valor do gasolina por litro: "))
    resultado = percorre(distancia, litro, posto)
    print(resultado)
main()
"""

#15.Sabe-se que em uma sala de aula, 40% das pessoas são do sexo masculino. 20% das mulheres são maiores de idade e 80% dos
#homens são menores de idade.
#Solicitando ao usuário a quantidade de alunos na sala, a presente a quantidade de mulheres menores de idade e a quantidade de
#homens maiores de idade.

"""
def sala(x):
    s_masculino = (x * 40) / 100
    s_feminino = (x * 60) / 100
    valor = (s_feminino * 80) / 100
    valor1 = (s_masculino * 20) / 100
    return valor1, valor
def main():
    x = float(input("Digite a quantidade de alunos da sala: "))
    resultado = sala(x)
    print("Quantida de homem de maiores e mulher de menor é: ", resultado)
main()
"""

#16.Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos.
#Calcular e escrever o percentual que cada uma dessas quantidades representa em relação ao total de eleitores, bem como o
#percentual de pessoas que não votaram.

"""
def eleitor(voto_b, voto_n, voto_v,eleitores):
     voto_branco = 100 * (voto_b / eleitores)
     votos_nulo = 100 * (voto_n / eleitores)
     voto_valido = 100 * (voto_v / eleitores)
     nao_voto = votos_nulo + voto_branco
 
     return voto_valido, nao_voto
def main():
    voto_b = float(input("Voto branco: "))
    voto_n = float(input("Voto nulo: "))
    voto_v = float(input("Voto valido: "))
    eleitores = float(input("Quantidade de eleitores: "))
    print(eleitor(voto_b, voto_n, voto_v, eleitores))
main()
"""

#17.Numa loja de eletrodomésticos, compras à vista têm um desconto de 10% e no pagamento a prazo (em três parcelas) tem um
#acréscimo de 5%. #Faça um algoritmo que leia o valor da compra, calcule e escreva o valor à vista, o valor à prazo total e de
#cada parcela.

"""
def pagamento(valor_parcela):

    calcular = (valor_parcela * 10)/100
    desconto = (valor_parcela - calcular) * 3
 
    valor = (5 * valor_parcela) / 100
    acrescimo = (valor_parcela + valor) * 3
    
    return valor_parcela, desconto, acrescimo
def main():
    x = float(input("Digite o valor da parcela"))
    result = pagamento(x)
    print("O valor a vista e a prazo e valor de cada parcela estão em ordem: ")
main(0)
"""

#18.Lidas as seguintes informações: salário do funcionário, quantidade de anos em que o funcionário trabalha na empresa e o
#número de filhos, calcule o salário atual do funcionário baseado no seguinte cálculo:
    #5 % de adicional sobre o valor do salário a cada 5 anos de trabalho
    #1% de adicional sobre o valor do salário a cada ano de trabalho
    #3 % de adicional sobre o valor do salário por cada filho

"""
def funcionario(salario_atual, q_anos, q_filhos):
    quantidade_ano = (q_anos * 0.05) + (q_anos * 0.01) + (q_filhos * 0.003)
    salario = salario_atual * quantidade_ano
    salario_atual = salario + salario_atual
    return salario_atual
def main():
    x = float(input("Digite o salario atual: "))
    a = int(input("Quantos anos trabalha na empresa: "))
    b = int(input("Quantos filhos: "))
    result = funcionario(x,a,b)
    print("Salario Atual: ",result)
main()
"""

#19.Em uma padaria, o padeiro quer saber qual o custo de fabricação do pão-francês e sobre esse valor obter um lucro de 30%.
#Considerando-se que uma receita para fazer 100 pães, leva farinha, água e fermento, escreva um algoritmo que lê a quantidade de
#quilos de farinha, o valor do quilo de farinha, a quantidade de litros de água, o valor de 1 litro de água, a quantidade de gramas
#de fermento, o valor do grama de fermento, o número de quilowatts de horas de luz gastos para fazer os pães, o valor do quilowatt/hora
#e o percentual do imposto que o padeiro paga pelo pão. O algoritmo deve calcular e escrever o preço de custo e de venda de um pão francês.

"""
def receita(q_farinha, v_quilo_farinha, q_agua, v_agua, g_fermento, v_g_fermento, hora_quilowatts, valor_quilowatts, imposto):
    valor = (q_farinha * v_quilo_farinha) + (q_agua * v_agua) + (g_fermento * v_g_fermento) + (hora_quilowatts * valor_quilowatts)
    calcula = (valor * imposto) / 100
    calcula1 = valor + (valor * 0,3)
    return calcula, calcula1
def main():
    q_farinha = float(input("Digite a quantidade de farinha: "))
    v_quilo_farinha = float(input("Digite o preco da farinha: "))
    q_agua = float(input("Digite a quantidade de agua: "))
    v_agua = float(input("Digite o preco da agua: "))
    g_fermento = float(input("Digite a quantidade de fermento: "))
    v_g_fermento = float(input("Digite o preco do fermento: "))
    hora_quilowatts = float(input("Digite o numero usado de energia: "))
    valor_quilowatts = float(input("Digite o valor da energia: "))
    imposto = float(input("Digite o imposto: "))
    result = receita(q_farinha, v_quilo_farinha, q_agua, v_agua, g_fermento, v_g_fermento, hora_quilowatts, valor_quilowatts, imposto)
    print(result)
main()
"""

#20.Um hotel com 75 apartamentos deseja fazer uma promoção especial definal de semana,
#concedendo um desconto de 25% na diária. Com isto,espera aumentar sua taxa de ocupação de 50% para 80%. Faça um algoritmo que leia o
#valor da diária (valor normal),
#calcule e imprima os seguintes dados:

#a)o valor da diária promocional;

"""
def hotel(diaria):
    promacao = diaria - ((diaria * 25) / 100)
    promacao = promacao * 75
    return promacao
def main():
    diaria = float(input("Digite o valor da diaria normal: "))
    promacao = hotel(diaria)
    print("O a diaria com promoção é de: ", promacao)
main()
"""

#b)o   valor   total   arrecadado   com   80%   de   ocupação   e   diária promocional;

"""
def hotel(diaria):
    promacao = diaria - ((diaria * 25) / 100)
    valor_total80= promacao * (80 * 75)
    return valor_total80
def main():
    diaria = float(input("Digite o valor da diaria normal: "))
    promacao = hotel(diaria)
    print("O a diaria com promoção é de: ", promacao)
main()
"""

#c)o valor total arrecadado com 50% de ocupação e diária normal;

"""
def hotel(diaria):
    c = diaria * (50 * 75)
    return c
def main():
    diaria = float(input("Digite o valor da diaria normal: "))
    promacao = hotel(diaria)
    print("O a diaria com promoção é de: ", promacao)
main()
"""

#d)Para os dados que você informou, qual é mais rentável (normal ou promocional)? (Pesquise sobre o comando Se para fazer esse Item).

"""
def hotel(diaria):
    promacao = diaria - ((diaria * 25) // 100)
    valor_total80= promacao * (0.8 * 75)
    c = diaria * (0.50 * 75)
    return valor_total80, c
def main():
    diaria = float(input("Digite o valor da diaria normal: "))
    resultado = hotel(diaria)
    print("O primeiro valor é do 80% com desconto e segundo é de 50% sem desconto: ", resultado)
main()
"""

#21.Nas ilhas Weblands, a moeda oficial é o Bit, havendo notas de B$ 50,00,B$ 10,00, B$ 5,00 e B$ 2,00.
#Escreva um programa para controlar um caixa automático: dado o valor desejado pelo cliente, o programa deve determinar o número de cada uma das notas,
#de modo a totalizar esse valor, minimizando a quantidade de cédulas entregues. Por exemplo, seo valor desejado for B$ 50,00, basta uma nota de B$ 50,00; se o
#valor desejado for B$ 72,00 é necessário entregar uma nota de B$ 50,00, duas de B$ 10,00 e uma nota de B$ 2,00.
#O programa deve pedir ao usuário o valor desejado, e deve responder com o número de cada uma das notas disponíveis.
#Considere que o cliente informará sempre valores que não utiliz em moedas de 1 bit.

"""
def contador(valor):
    nota50 = valor // 50
    nota10 = valor // 10
    nota5 = valor // 5
    nota2 = valor // 2
    return nota50, nota10, nota5, nota2
def main():
    x = float(input("Digite um valor: "))
    resultado = contador(x)
    print("A sua respectivas notas de 50, 10 ,5 ,2 ", resultado)
main()
"""

#22.A chance de acertar a Mega Sena com apenas um cartão de seis dezenas é de uma em 50.063.860. Ganha o prêmio principal quem acertar as seis dezenas,
#mas também são   pagos   os   acertadores   da   quina   (cincodezenas) e da quadra (quatro). A premiação paga o corresponde aapenas 46% do dinheiro arrecadado
#com as apostas e é dividida da seguinte maneira:35% para os acertadores de Sena.19% para os acertadores da quina.12% para os acertadores da quadra.
#Faça um algoritmo que a partir do dinheiro arrecadado, calcule e exiba o valor   da   premiação   (46%   do   dinheiro   arrecadado).   Em   seguida   o
#algoritmo também deverá exibir quanto ganharia os acertadores da Mega Sena (Sena, Quina e Quadra).

"""
def mega_sena(arrecadado,sena,quina,quadra):
    arrecadado = (500630860 * 0,46)
    sena = (arrecadado * 35) / 100
    quina = (arrecadado * 19) / 100
    quadra = (arrecadado * 12) / 100
    return arrecadado, sena, quina, quadra
    print("Total arrecadado : ", arrecadado, "Ganhador da Sena levou: ", sena, "da quina levou: ", quina, "e da quadra levou: ", quadra)
"""

#23.Um programa para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o número de notas de cada valor que deve ser
#disponibilizado para o cliente que realizou o saque.
#Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor fossem distribuídas em número mínimo possível.
#Por exemplo, se a quantia solicitada fosse R$ 87,00, o programa deveria indicar uma nota de R$ 50,00, três notas de R$ 10,00, uma nota de R$5,00 e
#uma nota de R$ 2,00.
#Escreva um programa que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.
#Considere que o cliente informará sempre valores que não utilizem moedas de 1 real.

"""
def caixa_eletronico(valor):
    nota100 = valor//100
    nota50 = valor // 50
    nota10 = valor // 10
    resto10 = valor - nota10 * 10
    nota5 = valor  // 5
    nota2 = valor  // 2
    return nota100, nota50, nota10, nota5, nota2
def main():
    x = float(input("Digite o valor: "))
    result = caixa_eletronico(x)
    print("As Quantidades de notas de 100, 50, 10, 5, 2 séra: ", result)
main()
"""

#24.Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não é suficientemente longa. Assumindo que seja possível medir sua sombra e a do
#prédio no chão, e que você lembre da sua altura, faça um algoritmo para ler os dados necessários e calcular a altura do prédio.

"""
def medir_predio(sombra_minha, sombra_predio, altura_minha):
    calcular = (sombra_minha/sombra_predio) * altura_minha
    return calcular
def main():
    x = float(input("Digita o tamanho da sua sombra: "))
    x1 = float(input("Digita o tamanho da sombra do predio: "))
    x2 = float(input("Digita a sua altura: "))
    resultado = medir_predio(x, x1, x2)
    print("A altura do predio é: ", resultado)
main()
"""

#25.Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média
#dos exercícios que fazem parte da avaliação.Calcular a média de aproveitamento, usando a fórmula:
#MA = (Nota1 + Nota2 * 2 + Nota3 * 3 + ME) / 7

"""
def m_aproveitamento(nota1, nota2, nota3, exercicios):
    ma = ((nota1 + nota2 * 2) + nota3 * 3 + exercicios) // 7
    return ma
def main():
    x = float(input("Digite a primeira nota: "))
    a = float(input("Digite a segunda nota: "))
    b = float(input("Digite a terceira nota: "))
    c = float(input("Digite a nota dos exercicios: "))
    resultado = m_aproveitamento(x, a, b, c)
    print("Aprovado ser for acima de 7.0 APROVADO, se for abaixo de 7.0 REPROVADO", resultado)
main()
"""

