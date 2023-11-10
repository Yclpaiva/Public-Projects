def pesquisaremlista(lista,valor):
    local = None
    for elemento in range(len(lista)):
        if lista[elemento] == valor:
            local = elemento
            return elemento
    if local == None:
        False
'''
lista = [1,5,8,5,3,5,6]
valoraprocurar = 2
if pesquisaremlista(lista,valoraprocurar) != None:
    print(f'valor encontrado: {pesquisaremlista(lista,valoraprocurar)}')
    print(f'{lista[pesquisaremlista(lista,valoraprocurar)]}')
else:
    print('valor não encontrado')
'''
