saldo = 2500
saque = int(input("informe o valor que você deseja sacar: "))


#if ternário tem a primeira parte o retorno caso expressão seja verdadeiro///segunda:expressão lógica///terceira:retorno caso contrário
status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")
