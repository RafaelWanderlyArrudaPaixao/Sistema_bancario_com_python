menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        
        else:
            print('Operação falhou! O valor informado é inválido.')
    
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Oeração falhou! O valor do saque excedeu o limite.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques diários excedido.')

        elif valor >0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operaão falhou! O valor informado é inválido.')

    elif opcao == 'e':
        print()
        print('*'*20,'Extrato','*'*20)
        print()
        print('Não foram realizados movimentações.' if not extrato else extrato)
        print()
        print(f'Saldo: R$ {saldo:.2f}')
        print()
        print('*'*49)

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')


