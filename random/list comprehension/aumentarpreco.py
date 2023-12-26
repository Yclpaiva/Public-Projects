import time
lista_precos = range(100000001)
start_time = time.time()
#cod1

def cod1():
    nova_lista_precos = []
    for preco in lista_precos:
        nova_lista_precos.append(preco * 2)
    #print(nova_lista_precos)
    import time
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")
    
#cod1 em list comprehension
def cod2():
    nova_lista_precos2  = [preco * 2 for preco in lista_precos]
    #print(nova_lista_precos2)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")
    
cod2()
