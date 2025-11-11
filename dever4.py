while True:

    try:

        razao_pa = int(input("Digite o valor da razão da Progressão Aritmética: "))
        numero_elementos_PA = int(input("Digite o valor de números que você deseja visualizar da Progressão Aritmética: "))
        elementos_PA = {}
        a1 = 0
        somatorio_PA = 0
        lista_teste = []

        for i in range(1,numero_elementos_PA+1):
            elemento_PA = a1 + (i - 1) * razao_pa
            elementos_PA[i] = elemento_PA
            lista_teste.append(elemento_PA)
            somatorio_PA += elemento_PA

        for a, i in elementos_PA.items():
            print(f"a{a} = {i}", end = ", ")

        print()
        print(f"Somatório da Progressão Aritmética é: {somatorio_PA}")

        for a, i in enumerate(lista_teste):
            print(f"a{a+1} = {i}", end = "@@@ ")
        if True:
            break     
    except:
        print("Houve um erro, você precisa digitar números inteiros")
