lista = [0, 1, 2, 5, 7, 10]
print(type(list(enumerate(lista))[1]))
for i, valor in enumerate(lista):
    print(f'i = {i}')
    print(f'value = {valor}')