
def verificar_primo(valor):
    if valor > 1:
        divisores = [1]
        for i in range(numero, 1, -1):
            
            resto = numero%i
            if resto == 0:
                divisores.append(i)


        if len(divisores) > 2:
            a = print(f"{valor} Não é um número primo.")
        else:
            a = print(f"{valor} É um número primo.")
        return a
    else:
        return None
    
numero = 2

while numero > 1:
    try:
        numero = int(input("Digite o número para verificar se ele é primo: "))
        verificar_primo(numero)
    except:
        print("Houve um erro, você precisa digitar um número.")
else:
    print(f"Por definição números primos são valores inteiros maiores do que 1, o valor {numero} não pode ser verificado.")