def menu():
    menu = ''' **************SISTEMA BANCÁRIO**************
    Seja bem-vindo ao nosso banco! Selecione uma opção para prosseguir:
    [S] SAQUE
    [D] DEPÓSITO
    [E] EXTRATO
    [NU] CRIAR NOVO USUÁRIO
    [NC] CRIAR NOVA CONTA
    [LC] LISTAR CONTAS DO BANCO
    [Q] SAIR
    \n
    '''
    return input(menu).upper()

def depositar(saldo_conta,deposito,extrato,/):
    if deposito > 0 :
        saldo_conta += deposito
        print("Depósito realizado com sucesso!")
        extrato += f"depósito: R${deposito:.2f}\n"
    else:
        print("Valor digitado errado!")
    
    return saldo_conta, extrato

def sacar(*, saldo_conta , saque , extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = saque > saldo_conta
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif saque > 0:
        print("Saque realizado com sucesso!")
        extrato += f"Saque: R${saque:.2f}\n"
        numero_saques = numero_saques + 1
        saldo_conta -= saque

    else:
        print("Valor informado é inválido!")

    return saldo_conta, extrato

def mostrar_extrato(saldo_conta,/,*,extrato):
    print("\n**************EXTRATO**************\n")
    print ("Não foram realizadas movimentações.") if extrato == (''' ''')  else print(extrato)
    print(f"\nSALDO: R${saldo_conta:.2f}")
    print("*************************************")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF, somente os números:")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF cadastrado no nosso Banco!")
        return
    
    nome = input("Informe o seu nome completo:")
    data_nascimento = input("Informe sua data de nascimento no formato -- dd/mm//aa : ")
    endereco = input("Informe o seu endereço no formato -- logradouro,número,bairro,cidade,sigla do estado : ")

    usuarios.append({"cpf":cpf,"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco})
    print("Usuário criado com sucesso! Seja-bem vindo(a) ao nosso banco. :)")

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o seu CPF, somente os números:")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("Conta criada com sucesso! Seja bem-vindo(a) ao nosso banco! :)")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    

    print("Esse CPF ainda não está cadastrado no banco. Primeiramente crie um usuário, para em seguida poder criar uma conta em nosso banco.")

def mostrar_contas(contas):
    for conta in contas:
        listar_contas = print(f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)

def main():
    saldo_conta = 0
    saque = 0 
    deposito = 0
    extrato = ''' '''   
    usuarios = []
    contas = []
    limite = 500
    numero_saques = 1
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_conta = 0

    while True:
        opcao = menu()

        if opcao == 'D':
            print("Você selecionou a opção depósito.")
            deposito = float(input("Digite o valor do seu depósito:"))
            saldo_conta,extrato = depositar(saldo_conta,deposito,extrato)

        elif opcao == 'S':
            print("Você selecionou a opção saque.")
            saque = float(input("Digite o valor que você gostaria de sacar: "))
            saldo_conta,extrato = sacar(saldo_conta=saldo_conta, saque=saque, extrato=extrato,
                                        limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 'E':
            mostrar_extrato(saldo_conta,extrato=extrato)

        elif opcao == 'NU':
            print("Você selecionou a opção Criar novo usuário.")
            criar_usuario(usuarios)

        elif opcao == 'NC':
            print("Você selecionou a opção para criar uma nova conta.")
            numero_conta += 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)


        elif opcao == 'LC':
            print("Você selecionou a opção para listar as contas do nosso banco.")
            mostrar_contas(contas)    

        elif opcao == 'Q':
            print("Obrigado por utilizar o nosso banco, até breve! :) \n\n")
            break

        else:
            print("Opção selecionada é inválida. Por gentileza, digite novamente.")

main()










