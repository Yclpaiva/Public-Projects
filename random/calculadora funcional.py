def adicao(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    if n2 == 0:
        return 'Operação inválida, divisão por 0'
    else:
        return n1/n2
    
n1 = float(input('diga o numero 1: '))
n2 = float(input('diga o numero 2: '))
operacao = input('diga a operação: ')

if operacao == 'adição':
    print(adicao(n1,n2))
if operacao == 'subtração':
    print(subtracao(n1,n2))
if operacao == 'multiplicação':
    print(multiplicacao(n1,n2))
if operacao == 'divisão':
    print(divisao(n1,n2))
if operacao not in ['adição','subtração','multiplicação','divisão']:
    print('operação inválida')