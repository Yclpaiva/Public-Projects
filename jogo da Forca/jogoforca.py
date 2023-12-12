from forcaAscii import forcavazia, cabeca, corpo, pernas
from selecionarPalavra import selecionarPalavra, randint
from funcoes import limparchat, palavrasEncontradasAtualizadas, verificarVitoria, fimDeJogo, continuarJogo, atualizarForca
import os

iniciarJogo = True


    
    
while iniciarJogo == True:
    limparchat()
    erros = 0
    palavra, dica = selecionarPalavra(randint)
    forcaASCII = [forcavazia[0],forcavazia[1],cabeca[0],corpo[0],pernas[0],forcavazia[3]]
    copiapalavra = list(palavra)
    palavrasEncontradas = ['_' for i in range(len(palavra))]
    
    print(*forcaASCII,sep= '\n')
    palavrasEncontradasAtualizadas()
    
    
    while True:
        letra = str(input('\ndigite uma letra: '))
        if letra in palavra:
            if letra in copiapalavra:
                print('tem!')
                valoriteravel = 0
                
                for _ in range(int(palavra.count(letra))):
                    posicao = copiapalavra.index(letra)
                    copiapalavra[posicao] = '*'
                    palavrasEncontradas[posicao] = f'{letra}'

                limparchat()
                print(*forcaASCII,sep= '\n')
                print(f'\nA palavra aparece: {palavra.count(letra)} vezes.')
                palavrasEncontradasAtualizadas()
                
                if verificarVitoria() == True:
                    fimDeJogo()
                    iniciarJogo = continuarJogo()
                    break
                
            else:
                limparchat()
                print(*forcaASCII,sep= '\n')
                palavrasEncontradasAtualizadas()
                
        else:
            limparchat()
            erros += 1
            atualizarForca(erros)
            print(*forcaASCII,sep= '\n')
            palavrasEncontradasAtualizadas()
            ('não tem!')
            
            if erros == 6:
                fimDeJogo()
                iniciarJogo = continuarJogo()
                break
                

    
