#MÉTODOS da classe list

#append -> adicionar elemento na lista
lista = []
lista.append(8)
print(lista)

#clear -> limpar lista
lista.clear()
print(lista)

#copy -> copiar lista/// lista é um objeto mutável se fizermos alterações mais na frente vai mudar a lista original,
#para evitar isso usamos o copy -> vai criar uma cópia com os mesmos elementos, mas não é a mesma lista elas terão instâncias diferentes (id)
#teremos uma nova lista2, se alterarmos lista2, a lista original não vai mudar

lista_original = [30,45]
lista2 = lista_original.copy()
print(lista2)
print(id(lista2),id(lista_original))

#count -> vai contar quantas vezes determinado objeto aparece na lista
lista_count = [30,1,20,30]
print(lista_count.count(30))
print (lista_count.count(1))

#extend -> juntar listas, em vez de adicionar um por um com append, podemos usar esse
linguagens = ["c","python","java"]
linguagens.extend(["js","csharp"])
print(linguagens)

#index -> qual a primeira ocorrência de um objeto na lista
lista_index = [1,2,4,6,7,8,4]
teste = ["c","java","swift","java"]
print(lista_index.index(4))
print(teste.index("java"))

#pop -> vai tirando sempre o elemento do final da lista por padrão, ou podemos alterar isso e passar o índice
linguagens = ["c","python","java"]
linguagens.pop()
print(linguagens)
print()
linguagens = ["c","python","java"]
linguagens.pop(0)
print(linguagens)

#remove -> tirar elemento da lista, ao invés de passar o índice como em pop, em remove passamos o objeto em sí nos parâmetros
linguagens = ["c","python","java"]
linguagens.remove("python")
print(linguagens)
#se tiver elementos repetidos ele vai retirar a 1° ocorrência desse elemento

#reverse -> fazer o espelhamento da lista
linguagens = ["c","python","java"]
linguagens.reverse()
print(linguagens)

#sort -> ordena a lista em ordem alfabética
linguagens = ["c","python","java"]
linguagens.sort()
print(linguagens)

#espelhar lista já ordenada alfabeticamente
linguagens = ["c","python","java"]
linguagens.sort(reverse=True)
print(linguagens)

#ordenar lista de acordo com o tamanho do elemento
linguagens = ["c","python","js","java"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

#espelhar lista já ordenada por tamanho de elemento
linguagens.sort(key=lambda x:len(x),reverse=True)
print(linguagens)

#LEN -> ver tamanho de um objeto, pode ser string, lista, etc...
linguagens = ["c","python","java"]
print(len(linguagens))

#SORTED -> ordenar iteráveis em ordem alfabética igual o sort/// só que tem passar ele no print
linguagens = ["c","python","java"]
print(sorted(linguagens))

#também podemos ordenar por tamanho de elemento ou espelhar a lista com o sorted
linguagens = ["c","python","java"]
print(sorted(linguagens,key=lambda x:len(x)))


linguagens = ["c","python","java"]
print(sorted(linguagens,key=lambda x: len(x),reverse=True))

