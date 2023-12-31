import sqlite3
import os

connection = sqlite3.connect('db.db')
cursor = connection.cursor()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def modificar_table():
    try:
        table = str(input('digite o comando para table ser adicionada: '))
        cursor.execute(table)
        print('Executado com Sucesso!')
        connection.commit()
    except sqlite3.Error as error:
        print(f'Erro ocorrido, referência: {error}')
        
def atualizar_db():
    try:
        connection.commit()
        clear_terminal()
        print('Atualizado com sucesso\n')
    except sqlite3.Error as error:
        print(f'Erro ocorrido, referência: {error}')      
          
def formulario_aluno():
        nome = str(input('Qual o nome do aluno? '))
        idade = int(input('Qual a idade? '))
        try:nota_geral = float(input('Qual a nota? '))
        except ValueError:nota_geral = 0
        return nome,idade,nota_geral
    
def adicionar_aluno():
    try:
        comando_sql = ('INSERT INTO Alunos (nome, idade, nota_geral) VALUES (?, ?, ?)')
        dados_aluno = (formulario_aluno())
        cursor.execute(comando_sql,dados_aluno)
        atualizar_db()
    except sqlite3.Error as error:
        print(f'Erro ocorrido, referência: {error}')
        
def selecionar_nome_aluno():
    while True:
        id_aluno = receber_id_do_user()
        try:
            cursor.execute(f'SELECT nome FROM alunos WHERE id = ?',(id_aluno,))  
            nomealuno = cursor.fetchone()
            if nomealuno is not None:
                return(id_aluno, nomealuno[0])
            else:
                print('id invalido')
        except sqlite3.Error as error:
            print(f'Erro ocorrido no sqlite3, referência: {error}')
        
def receber_id_do_user():
    while True:
        try:
            id_aluno = int(input('Digite o ID do aluno: '))
            return id_aluno 
        except ValueError:
            print('O valor digitado é invalido, digite um número')
            
def receber_confirmacao_delecao(selecao):
    while True:
        confirmar = input('Confirme a deleção do aluno, digite o nome do aluno completo(digite "cancelar" para cancelar deleção): ')
        if confirmar == selecao:
            return True
        elif confirmar == 'cancelar': 
            return False
        else:
            print('deleção não confirmada')
            
def deletar_aluno():
    try:
        id_aluno, selecao = selecionar_nome_aluno()
        print(selecao)
        if receber_confirmacao_delecao(selecao) == True:
            cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
            atualizar_db()
        else:
            print('não deletado')
    except sqlite3.Error as error:
        print(f'Erro ocorrido, referência: {error}')
        
def receber_notas():
    notas = []
    for nota in range(4):
        notas.append(float(input(f'Digite a nota da {nota+1} unidade: ')))
    return sum(notas)/4

def atualizar_nota():
    id = receber_id_do_user()
    nota_geral = receber_notas()
    cursor.execute('UPDATE alunos SET nota_geral = ? WHERE id = ?',(nota_geral, id))
    atualizar_db()
    