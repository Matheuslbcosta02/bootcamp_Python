#percorrer lista -> usar comando FOR
carros2 = ["fox","f50","punto"]

for carro2 in carros2:
    print(carro2)

print()
#FUNÇÃO ENUMERATE -> saber o índice do elemento dentro do laço 
carros = ["gol","celta","palio"]

for indice , carro in enumerate(carros):
     print(f"{indice}:{carro}")

print()

#compreensão de listas -> criar uma nova lista com base em uma existente (filtro)

#APPEND
numeros = [1,30,21,45]
pares = []
for numero in numeros:
     if numero % 2 == 0:
          pares.append(numero)
print(pares)
print()          

#Instrução de compreensão  [o que vai retornar na lista//a iteração FOR///filtro (opcional)]
numeros2 = [30,40,21,35,36,68]
pares2 = [numero2 for numero2 in numeros2 if numero2 % 2 == 0] 
print(pares2)
print ()

#Modificar valores usando o append
numeros3 = [2,3,4,5]
quadrado = []
for numero3 in numeros3:
     quadrado.append(numero3 ** 2)
print(quadrado)
print()

#Modificar valores usando a instrução de compreensão
numeros4 = [4,5,8,9]
quadrado2 = [numero4 ** 2 for numero4 in numeros4]
print(quadrado2)
print()
