x = 'Morango'

def fruta():
    print('eu gosto de',x)
    


def fruta2():
    x = 'Maçã'
    print('eu gosto de',x)

def minha_funcao():
    global z
    z = 'uva'
    
def fruta3():
    print('eu gosto de',z)
    
    
fruta()
fruta2()

#a função da variavel global precisa ser chamada 
minha_funcao()
fruta3()