import textwrap

def menu():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios= []
contas = []

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input('Informe o CPF:')

     usuario = filtrar_usuario(cpf, usuarios)

     if usuario: 
         print("\n=== Conta criada com sucesso! ===")
         return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
     
     print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados =[usuario for usuario in usuarios if['cpf'] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf= input('Informe o CFP (somente numeros):')
    usuario= filtrar_usuario(cpf, usuarios)

    if usuario:
         print("\n@@@ Já existe usuário com esse CPF! @@@")
         return
    
    nome = input('Informe o nome:')
    data_nascimento= input('Informe a data de nascimento (dd-mm-aaaa)')
    endereco = input('Informe o endereço: (logradouro, nr - bairro - cidade/sigla estado):')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print('===usuário criado com sucesso!===')

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
     

def deposito(saldo, valor, extrato):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def saque(*saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)
       

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = saque(saldo= saldo, valor= valor, extrato= extrato, limite= limite, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES  )

    elif opcao == "e":
         extrato(saldo, extrato=extrato)
    
    elif opcao == "nu":
            criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)
       

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
     
