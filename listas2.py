#acessar dados da lista com índices. Primeiro índice é sempre zero.
frutas = ["uva","pera","laranja"]
print(frutas[0])
print(frutas[1])

#ou podemos usar índices negativos -> vai de trás para frente. O último objeto é sempre -1, e assim por diante...
print(frutas[-1])
print(frutas[-2])


#LISTAS ANINHADAS -> armazenar uma lista dentro de outra lista. É muito útil para criar matrizes (estruturas bidimensionais) tabelas
#para acessar essas matrizes usamos dois índices -> linha e coluna   ###COLOCAR VÍRGULA após a linha!!
matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"]
]
print (matriz[0])
print (matriz[0][0])
print (matriz[0][-1])
print (matriz[-1][-1])

#FATIAMENTO ->  [start:stop:step] ou [start:] ou [:stop]
lista = ["p","y","t","h","o","n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])

#imprimir cópia
print(lista[::])

#espelhar
print(lista[::-1])
