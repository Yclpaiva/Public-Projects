import sqlite3


#conexão com banco de dados de alunos
connection = sqlite3.connect('db.db')
cursor = connection.cursor()

#criar tabela de dados de alunos
def modificar_table():
    try:
        table = str(input('digite o comando para table ser adicionada: '))
        cursor.execute(table)
        print('Executado com Sucesso!')
        connection.commit()
    except sqlite3.Error as error:
        print(f'Erro ocorrido, referência: {error}')
        
def finalizar_operacoes():
        connection.commit()
        connection.close()
        print('Adicionado com sucesso')
        
def formulario_aluno():
        nome = str(input('Qual o nome do aluno? '))
        idade = int(input('Qual a idade? '))
        try:nota_geral = float(input('Qual a nota? '))
        except ValueError:nota_geral = 0
        return nome,idade,nota_geral
    
def inserir_aluno():
    try:
        comando_sql = ('INSERT INTO Alunos (nome, idade, nota_geral) VALUES (?, ?, ?)')
        dados_aluno = (formulario_aluno())
        cursor.execute(comando_sql,dados_aluno)
        finalizar_operacoes()
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
            id_aluno = int(input('Digite o ID do aluno a ser deletado: '))
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
            finalizar_operacoes()
        else:
            print('não deletado')
    except sqlite3.Error as error:
        print(f'Erro ocorrido, referência: {error}')
        
def main():
    inserir_aluno()


if __name__ == '__main__':
    main()