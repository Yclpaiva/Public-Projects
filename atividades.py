import sys

def positivo():
    numero = int(input('Qual o número? '))
    if numero >= 0 :
        print('o número é positivo')
    else:
        print('o número é negativo')


def maiornota():
    numero = float(input('Qual a nota? '))
    numero2 = float(input('Qual a nota 2? '))
    if numero > numero2:
        print(numero)
    else:
        print(numero2)


def media():
    lista = []
    for _ in range(4):
        lista.append(float('Diga uma nota: '))
    resultado = sum(lista)/(len(lista))
    print(resultado)
    if resultado >= 6:
        print('aprovado')
    else:
        print('reprovado')




if len(sys.argv) == 1 or len(sys.argv) > 3:
    exit()
if sys.argv[1] == 'maiornota':
    maiornota()
elif sys.argv[1] == 'positivo':
    positivo()
elif sys.argv[1] == 'media':
    media()