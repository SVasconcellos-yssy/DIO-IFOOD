saldo_atual = 1000
extrato = ''
LIMITE_SAQUES = 3
saques = 0


texto_boas_vindas = '''

### Bem-vindo ao banco Nosso Dinheiro! ###

O que deseja fazer hoje? 

[1] - Depositar
[2] - Sacar
[3] - Verificar extrato
[4] - Sair

'''

while True:
    print(texto_boas_vindas)
    acao_usuario = input()


    if int(acao_usuario) == 1:
        deposito = float(input('Certo, agora digite o valor a ser depositado:'))
        print(deposito) 

        if deposito > 0:
            saldo_atual += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'

            print('O valor foi depositado com sucesso.')
        else:
            print('O valor informado esta incorreto. Tente novamente')


    elif int(acao_usuario) == 2:
        valor_sacado = float(input('Certo, digite a quantidade que deseja sacar:'))

        excedeu_saldo = valor_sacado > saldo_atual
        excedeu_limite = valor_sacado > 500
        excedeu_saques = saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor_sacado > 0:
            saldo_atual -= valor_sacado
            extrato += f'Saque: R$ {valor_sacado:.2f}\n'
            saques += 1
            print('O valor foi sacado com sucesso.')

        elif valor_sacado > saldo_atual:
            print('Saldo insuficiente para o saque.')

        else:
            print('Valor informado é invalido.')

    elif int(acao_usuario) ==3:
        print('\n===========EXTRATO=============')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo_atual:.2f}')
        print('=================================')

    elif int(acao_usuario) == 4:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")








