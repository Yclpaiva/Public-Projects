n = int(input('digite um número: '))
lista = range(1,n)
resultado = 1
for _ in lista:
    resultado += resultado*_
    print(resultado)