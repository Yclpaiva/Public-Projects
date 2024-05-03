from typing import Type


qnt_contas = 1
clientes = [{'cpf': 12345678900, 'nome': 'Yuri', 'nascimento': '01/01/2000', 'endereço': 'rua 1, 123, bairro 1, cidade 1, estado 1', 'conta': [{'numero': '0001', 'saldo': 0, 'extrato': []}]},]

def criar_cliente(cpf, nome, nascimento, endereço):
    global qnt_contas
    qnt_contas += 1
    clientes.append({
                    'cpf': cpf,
                    'nome': nome,
                    'nascimento': nascimento,
                    'endereço': endereço,
                    'conta': [],
                    })
    print('\ncliente criado!\n')

def criar_conta(index):
    global qnt_contas
    numero = qnt_contas
    saldo = 0
    extrato = []
    clientes[index]['conta'].append({
                                'numero': str(numero).zfill(4),
                                'saldo': saldo,
                                'extrato': extrato,
                                    })
    print('\nConta criada!\n')


def saque(cpf, numero, valor):
    for cliente in clientes:
        if cpf == cliente['cpf']:
            for conta in cliente['conta']:
                if numero == conta['numero']:
                    if valor > conta['saldo']:
                        return '\nSaldo insuficiente\n'
                    conta['saldo'] += valor
                    conta['extrato'].append(valor)
                    return '\nSaque realizado com sucesso\n'
            else:
                return '\nConta não encontrada\n'
    else:
        return '\nCliente não encontrado\n'


def extrato():
    pass

def deposito(cpf, numero, valor):
    for cliente in clientes:
        if cpf == cliente['cpf']:
            for conta in cliente['conta']:
                if numero == conta['numero']:
                    conta['saldo'] += valor
                    conta['extrato'].append(valor)
                    return '\nDepósito realizado com sucesso\n'
            else:
                return '\nConta não encontrada\n'
    else:
        return '\nCliente não encontrado\n'

while True:
    print("1. criar cliente")
    print("2. criar conta")
    print("3. deposito")
    print("4. saque")
    print("5. saldo")
    print("6. extrato")
    opcao = int(input("Escolha uma opção: "))
    
    
    match(opcao):
        case 1:
            nome = input('Digite o nome do cliente: ')
            cpf = int(input('Digite o cpf do cliente: '))
            nascimento = input('Digite a data de nascimento do cliente: ')
            print('\nformato do endereço: logradouro, número, bairro, cidade, estado\n')
            endereço = input('Digite o endereço do endereço do cliente: ')
            for cliente in clientes:
                if cpf == cliente['cpf']:
                    print('Cliente já cadastrado\n pulando a criação\n')
                    break
            criar_cliente(cpf, nome, nascimento, endereço)

        case 2:
            key = int(input('Digite o cpf do cliente: '))
            for index, cliente in enumerate(clientes):
                if key == cliente['cpf']:
                    print('Cliente encontrado\n')
                    criar_conta(index)
                    break
            else:
                print('Cliente não encontrado\n')
                break
            
        case 3:
            cpf = int(input('digite o cpf do cliente: '))
            numero = input('digite o número da conta: ')
            for cliente in clientes:
                if cpf == cliente['cpf']:
                    print('Cliente encontrado\n')
                    for conta in cliente['conta']:
                        if numero == conta['numero']:
                            print('Conta encontrada\n')
                            valor = float(input("Digite o valor do deposito: "))
                            print(deposito(cpf, numero, valor))
                            break
                    else:
                        print('Conta não encontrada\n')
                        break
        case 4:
            cpf = int(input('digite o cpf do cliente: '))
            numero = input('digite o número da conta: ')
            print(clientes)
            for cliente in clientes:
                print(cliente)
                if cpf == cliente['cpf']:
                    print('Cliente encontrado\n')
                    for conta in cliente['conta']:
                        if numero == conta['numero']:
                            print('Conta encontrada\n')
                            valor = -1*(float(input("Digite o valor do saque: ")))
                            print(saque(cpf, numero, valor))
                            break
                    else:
                        print('Conta não encontrada\n')
                        break

        case 5:
            cpf = int(input('digite o cpf do cliente: '))
            numero = input('digite o número da conta: ')
            for cliente in clientes:
                if cpf == cliente['cpf']:
                    print('Cliente encontrado\n')
                    for conta in cliente['conta']:
                        if numero == conta['numero']:
                            print('Conta encontrada\n')
                            print(f"Saldo: R${conta['saldo']:.2f}\n")
                            break
                    else:
                        print('Conta não encontrada\n')
                        break
        case 6:
            cpf = int(input('digite o cpf do cliente: '))
            numero = input('digite o número da conta: ')
            for cliente in clientes:
                print(cliente['cpf'])
                if cpf == cliente['cpf']:
                    print('Cliente encontrado\n')
                    for conta in cliente['conta']:
                        if numero == conta['numero']:
                            print('Conta encontrada\n')
                            print("Extrato")
                            for valor in conta['extrato']:
                                print(f'R${valor:.2f}')
                            print(f"Saldo: R${conta['saldo']:.2f}\n")
                            break
                        else:
                            print('Conta não encontrada\n')
                        break
                else:
                    print('Cliente não encontrado\n')
                    break
        case _:
            print("Opção inválida")
            break
"""
 elif opcao == 2:
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato.append(valor)

    elif opcao == 3:
        if qntSaques >= 3:
            print("Limite de saques diários atingido")
            continue
        else:
            valor = float(input("Digite o valor do saque: "))
            if valor <= 500:
                if valor >= saldo:
                    print("Saldo insuficiente")
                    continue
                else:
                    saldo -= valor
                    extrato.append(-valor)
                    qntSaques += 1

            else:
                print("Valor máximo de saque é R$ 500,00")
                continue

    elif opcao == 4:
        print("Extrato")
        for valor in extrato:
            print(f'R${valor:.2f}')
        print(f"Saldo: R${saldo:.2f}")

    elif opcao == 5:
        break

    elif opcao == 0:
        qnt_saques = 0

    else:
        print("Opção inválida")
    """    
