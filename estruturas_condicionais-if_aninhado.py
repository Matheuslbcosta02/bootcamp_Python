conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

#if aninhado
if conta_normal:
    if saldo>saque:
        print("saque realizado com sucesso!")
    elif saque < (saldo + cheque_especial):
        print("Saque realizado com cheque especial.")
    else:
        print("Saldo insuficiente.")

elif conta_universitaria:
    if saldo>saque:
        print("saque realizado com sucesso!")
    elif saque < (saldo + cheque_especial):
        print("Saque realizado com cheque especial.")
    else:
        print("Saldo insuficiente.")

else:
    print("Sistema não reconhceu o seu tipo de conta! Fale com o seu gerente.")                               