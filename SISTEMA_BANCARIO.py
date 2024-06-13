saldo_conta = 0
saque = 0 
deposito = 0

extrato = ''' '''               

menu = ''' **************SISTEMA BANCÁRIO**************
Seja bem-vindo ao nosso banco! Selecione uma opção para prosseguir:
[S] SAQUE
[D] DEPÓSITO
[E] EXTRATO
[Q] SAIR
\n
'''
numero_saques = 1
limite_saques = 3

opcao = input(menu).upper()
print(opcao)

while True:
    if opcao == 'S' :
        print("Você selecionou a opção saque.")
        if (numero_saques <= limite_saques):
            saque = float(input("Digite o valor que você gostaria de sacar: "))
            if saque <= saldo_conta:
                if saque > 0 and saque <=500:
                    print("Saque realizado com sucesso!")
                    extrato += f"Saque: R${saque:.2f}\n"
                    numero_saques +=1
                    saldo_conta -= saque
                    opcao = input(menu).upper()
                elif saque<0:
                    print("Valor digitado errado!")
                    saque -= saque
                    opcao = input(menu).upper()    
                else:
                    print("Valor digitado é maior do que o seu limite de R$ 500.00 por saque.")
                    saque -= saque
                    opcao = input(menu).upper()
            else:
                print("Você não possui saldo suficiente!")
                print("CONSULTE SEU EXTRATO!")
                saque -= saque
                opcao = input(menu).upper()
        else:
            print("Você atingiu o limite de 3 saques diários!")
            opcao = input(menu).upper()           

    elif opcao == 'D':
        print("Você selecionou a opção depósito.")
        deposito = float(input("Digite o valor do seu depósito:"))
        if deposito > 0 :
            print("Depósito realizado com sucesso!")
            extrato += f"depósito: R${deposito:.2f}\n"
            saldo_conta += deposito
            opcao = input(menu).upper()
        else:
            print("Valor digitado errado!")
            opcao = input(menu).upper()

    elif opcao == 'E':
        print("Você selecionou a opção extrato.")
        print("\n**************EXTRATO**************\n")
        print ("Não foram realizadas movimentações.") if extrato == (''' ''')  else print(extrato)
        print(f"\nSALDO: R${saldo_conta:.2f}")
        print("*************************************")
        opcao = input(menu).upper()

    elif opcao =='Q':
        print("Obrigado por utilizar o nosso banco! Até breve. :)")
        break

    else:
        print("Opção selecionada é inválida. Por gentileza, digite novamente.")
        print()
        opcao = input(menu).upper() 




