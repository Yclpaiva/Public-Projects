def contarvogais(palavra):
    vogais = 0
    for i in palavra:
        if i in 'aeiou':
            vogais += 1
    return vogais

def substituicao(palavra,substituir):
    palavra = str(palavra)
    for i in palavra:
        if i in 'aeiou':
            palavra = palavra.replace(i,substituir)
    return palavra

palavra = input('Qual palavra você deseja? ')
substituir = input('pelo que você quer substituir as vogais?')
print(substituicao(palavra,substituir))