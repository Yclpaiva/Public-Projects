saldo = 0
extrato = []
qntSaques = 0
while True:
    print("1. Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Extrato")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Saldo: {saldo}")

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
        
