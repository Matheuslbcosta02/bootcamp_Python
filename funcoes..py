
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
        divisores.sort()
        return a, divisores
    else:
        return
    
numero = 2

while numero > 1:
    try:
        numero = int(input("Digite o número para verificar se ele é primo: "))
        resposta, lista = verificar_primo(numero)
        print(f"Os divisores do número {numero} são: ")
        print(lista)
    except:
        print("Houve um erro, você precisa digitar um número que seja válido.")
else:
    print(f"Por definição números primos são valores inteiros maiores do que 1, o valor {numero} não pode ser verificado.")
