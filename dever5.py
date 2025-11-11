A = 0
B = 1

c = A + B
i = 1
lista_fibonacci = [0,1]
N = int(input("Digite quantos números você deseja visualizar da sequência de Fibonacci: "))

while i <= N - 2:
    c = A + B
    lista_fibonacci.append(c)
    A = B
    B = c
    i += 1

print(f"Sequência de Fibonacci com {N} termos que você desejou visualizar.")
print()
for a, i in enumerate(lista_fibonacci):
    print(f"a{a+1} = {i}", end = " ,  ")
