import time
lista_precos = [500,1000,2000,5000,50,300,1250,1500]
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
  
  
def cod3():
    imposto = []
    for preco in lista_precos:
        if preco > 1000:
            imposto.append(preco*1.5)
    print(imposto)
    
def cod4():
    imposto = [preco * 1.5 for preco in lista_precos if preco > 1000]
    print(imposto)
    
cod4()