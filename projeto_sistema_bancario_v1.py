menu = '''
    Opções:
           [1] Depósito
           [2] Saque
           [3] Extrato
           [0] Sair

    Digite a sua opção -> '''
print()

saldo = 0
extrato = ''
numero_de_saques = 0
LIMITE_DE_SAQUES_DIARIOS = 3
VALOR_LIMITE_SAQUE_DIARIO = 500

while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Informe o valor do depósito: "))
        print()

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print()
            print(extrato)

        else:
            print("Valor inválido, tente novamente!".center(30,))

    elif opcao == '2':
        valor = float(input("Informe o valor do saque: "))
        print()

        if numero_de_saques >= LIMITE_DE_SAQUES_DIARIOS:
            print("Limites de saques diários já foi atingido!".center(30,))

        elif valor > VALOR_LIMITE_SAQUE_DIARIO:
            print("Valor máximo por saque -> R$ 500.00".center(30,))

        elif valor > saldo:
            print("Saldo insuficiente para completar a operação!".center(30,))
        
        elif valor > 0:
            numero_de_saques += 1
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            print(extrato)
       
        else:
            print("Valor inválido, tente novamente!".center(30,))

    elif opcao == '3':
        print()
        print("EXTRATO".center(30,'='))
        print(f" Saldo: R$ {saldo:.2f} ".center(30,'='))
        print()

    elif opcao == '0':
        print()
        print(" Tenha um ótimo dia! ".center(30,))
        print()
        break

    else:
        print("Operação inválida. Selecione novamente uma das opções.".center(30,))
