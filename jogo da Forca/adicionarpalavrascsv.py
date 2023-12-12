import csv

data = {
    'python': '"Uma linguagem de programação poderosa"',
    'computador': '"Máquina que processa dados"',
    'elefante': '"Um animal de grande porte com tromba"',
    'praia': '"Lugar onde a areia encontra o mar"',
    'abacaxi': '"Uma fruta tropical com casca espinhosa"',
    'programacao': '"Atividade de escrever códigos de computador"',
    'girafa': '"Um animal com pescoço longo"',
    'ocelote': '"Um felino selvagem da América"',
    'chocolate': '"Doce feito de cacau"',
    'montanha': '"Elevação natural da superfície terrestre"'
}

# Nome do arquivo CSV
csv_file = 'palavras e dicas.csv'

# Abre o arquivo CSV em modo de escrita
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    # Cria um objeto CSV para escrever no arquivo
    writer = csv.writer(file)

    # Escreve o cabeçalho do CSV (opcional)
    writer.writerow(['Palavra', 'Definição'])

    # Escreve os dados no arquivo CSV
    for palavra, definicao in data.items():
        writer.writerow([palavra, definicao])

print(f'O arquivo CSV "{csv_file}" foi criado com sucesso.')
