#while é usado para repetir um bloco de código várias vezes.
#faz sentido usar o while quando não sabemos o número de vezes que vamos executar aquele bloco.
#while parece o if, testa e executa, só que o if é somente uma vez, o while vai até a condição de parada for atendida.

opcao = -1

while opcao !=0:
    opcao = int(input("[1] sacar\t [2] extrato\t [0] sair \t :"))
    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("exibindo extrato...")
    elif opcao == 0:
        print("Obrigado por usar nosso sistema bancário, até breve!  :)")
    else:
        print("erro.")        