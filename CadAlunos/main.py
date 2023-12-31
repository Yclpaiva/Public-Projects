import funcoes

#conexão com banco de dados de alunos


#criar tabela de dados de alunos
def menu():
    while True:
        print('Sistema CadAlunos')
        print('1-Cadastrar Aluno, 2-Deletar Aluno, 3-Atualizar notas')
        valor = int(input(''))
        if valor == 1:
            funcoes.adicionar_aluno()
        if valor == 2:
            funcoes.deletar_aluno()
        if valor == 3:
            funcoes.atualizar_nota()
        
def main():
    menu()


if __name__ == '__main__':
    main()