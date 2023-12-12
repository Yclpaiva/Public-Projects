import random

randint= random.randint

import csv


def carregar_dados_do_csv(caminho_do_csv):
    listapalavras = []
    with open(caminho_do_csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        i = 0
        for linha in leitor_csv:
            nome = linha[0]
            definicao = linha[1]
            listapalavras.append(nome) 
            listapalavras.append(definicao)
            i += 1
    return listapalavras

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
# Exemplo de uso
caminho_do_csv = 'palavras e dicas.csv'

# Agora listapalavras é um dicionário com os dados do CSV
def selecionarPalavra(randint):
    listapalavras = carregar_dados_do_csv(caminho_do_csv)
    posicao = randint(0,(len(list(listapalavras))))
    if par_ou_impar(posicao) == 'Par':
        posicao = posicao
    else:
        posicao -= 1
    palavra, dica = (listapalavras[posicao],listapalavras[posicao+1])
    return palavra, dica



print()