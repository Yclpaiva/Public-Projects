from jogoforca import forcaASCII, erros, copiapalavra,palavrasEncontradas,dica
from forcaAscii import forcavazia, cabeca, corpo, pernas
from selecionarPalavra import selecionarPalavra, randint
import os

def limparchat():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def atualizarForca(quantidadeErros):
    if quantidadeErros == 1:
        forcaASCII[2] = cabeca[1]
    elif quantidadeErros <= 4:
        forcaASCII[3] = corpo[erros-1]
    elif quantidadeErros <= 6:
        forcaASCII[4] = pernas[erros-4]
        
def verificarVitoria():
    contador = 0
    for i in copiapalavra:
        if i != '*':contador += 1
    if contador != 0:return False
    if contador == 0:return True
    
def fimDeJogo():
    if verificarVitoria() == True:
        print('\nVocê venceu!')
    else:
        print('\nVocê perdeu!')

def continuarJogo():
    while True:
        continuar = str(input('Deseja Continuar o jogo? s/n: ')).lower()
        if continuar == 's':
            return True
        if continuar == 'n':
            return False
        if continuar != ('s' or 'n'):
            print('Valor digitado inválido')
            
def palavrasEncontradasAtualizadas():
    print(' '.join(palavrasEncontradas),f'    {dica}')