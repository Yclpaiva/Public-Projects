def tarefa1():
    '''1-Faça um Programa que peça dois números e imprima a soma.'''
    num1 =int(input("Informe  1 número: "))
    num2 =int(input("Informe 1 número: "))
    print(num1+num2)

def tarefa2():
    '''2-Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''
    num1 =float(input("Informe  1 número: "))
    num2 =float(input("Informe 1 número: "))
    num3 =float(input("Informe 1 número: "))
    num4 =float(input("Informe 1 número: "))
    total = (num1+num2+num3+num4)/4
    print("Sua média foi:" +str(round(total,2)))

def tarefa3():
    '''3- Faça um Programa que converta metros para centímetros.'''
    metros = int(input("Informe o valor em metros: "))
    centimetros = metros*100
    print (f"Seu valor em centimetros é: {centimetros}")

def tarefa4():
    '''
4- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.

faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Líquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
    ganhohora= float(input("Qual o valor que você ganha por hora?: "))
    horasmes= float(input("Qual o número de horas trabalhadas por mês?: "))
    salariobruto = round(ganhohora*horasmes,2)
    ir = round(salariobruto*0.11,2)
    inss = round(salariobruto*0.08,2)
    sindicato = round(salariobruto*0.05,2)
    liquido = round(salariobruto - (ir+inss+sindicato),2)

    print(f"Seu salário bruto: R${salariobruto}")
    print(f"Seu valor pago para o imposto de renda: R${ir}")
    print(f"Seu valor pago ao inss: R${inss}")
    print(f"Seu valor pago ao sindicato: R${sindicato}")
    print (f"Seu salário líquido: R${liquido}")

def tarefa5():
    '''
5-Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
    import math
    metrosareapintada = float(input("Qual a área a ser pintada em m2?: "))
    COBERTURA = 3
    LATATINTA = 18
    VALORLATA = 80
    litrosusado = metrosareapintada/COBERTURA

    qntlatasusada = math.ceil(litrosusado/LATATINTA)
    precopago = round(qntlatasusada*VALORLATA)

    print (f"A sua quantidade de latas usadas foi: {qntlatasusada}")
    print (f"A seu preço pago total foi de: R${precopago}")
