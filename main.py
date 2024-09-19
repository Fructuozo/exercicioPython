menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo =+ valor
            extrato += f'Depósito no valor de R$ {valor:.2f}\n'

        else:
            print('peração falhou! Informe um valor válido.')

    elif opcao == "2":
        valor = float(input('Informe o valor que deseja sacar: '))

        execeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = valor > numero_saque >= LIMITE_SAQUE

        if excedeu_saque:
            print('Operação falhou! Você não tem saldo suficiente')

        elif excedeu_limite:
            print('Operação falhou! Número máximo de saques')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'

        else:
            print('Operação falhou! O valor informado é inválido.')



    elif opcao == "3":
        print('-=' * 20)
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Seu saldo é de: R${saldo:.2f}')
        print('-=' * 20)

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente aa operaçao desejada.")