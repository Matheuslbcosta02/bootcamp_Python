#geradores são tipos especiais de iteradores
#preferível usar quando é algo mais simples, algo mais complexo usar iteradores
#a execução de um gerador é pausada usando o "yield" não usamos return

def meu_gerador (numeros: list[int]):
    for numero in numeros:
        yield numero * 2

#usando gerador
for i in meu_gerador(numeros=[1,2,3]):
    print(i)

