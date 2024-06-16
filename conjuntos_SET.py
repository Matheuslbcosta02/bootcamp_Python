#CONJUNTOS SET -> coleção que não possui objetos repetidos, útil para eliminar itens duplicados, etc.
#podemos declarar set com "set()" ou  {}
print(set([1,2,3,1,3,4]))

#igual o comando list vai iterar e cada letra irá virar um elemento do conjunto, mas diferente do list o set não garante a ordem!!!!
print(set("abacaxi"))
print(set(("palio","gol","celta","palio",)))
print({20,21,22,23,20,23})
print()
#Conjuntos em python não suportam indexação, e muito menos fatiamento, para acessar um dado no conjunto precisa coverter o set em lista
numeros = {1,2,3,4,4,5}
numeros = list(numeros)
print(numeros[0])
print()
#Interar conjuntos -> FOR

carros = {"gol","celta","palio","gol"}
for carro in carros:
    print(carro)

print()
#FOR com enumerate
sequencia = {"casa","parede","teto"}
for indice, itens in enumerate(sequencia):
    print(f"{indice}:{itens}")

print()

#MÉTODOS DA CLASSE SET
conjunto_a = {1,2,3}
conjunto_b = {3,4,5}

#union -> unir conjuntos
a = conjunto_a.union(conjunto_b)
print(a)
#intersection -> intersecção
a = conjunto_a.intersection(conjunto_b)
print(a)
#difference -> tirar a diferença
a = conjunto_a.difference(conjunto_b)
b = conjunto_b.difference(conjunto_a)
print(a)
print(b)
#symmetric_difference -> todos os elementos que não estão na intersecção
a = conjunto_a.symmetric_difference(conjunto_b)
print(a)
#issubset -> ver se um conjunto é subconjunto do outro, vai retornar um valor booleano
conjunto_a = {1,2,3}
conjunto_b = {2,4,1,3,5}
a = conjunto_a.issubset(conjunto_b)
print(a)
b = conjunto_b.issubset(conjunto_a)
print(b)
#issuperset -> ao contrário do issubset, é pra ver se é superset. vai retornar valor booleano
a = conjunto_a.issuperset(conjunto_b)
print(a)
b = conjunto_b.issuperset(conjunto_a)
print(b)
#isdisjoint -> ver se um conjunto é disjunto do outro, ou seja, eles não se tocam não existe intersecção. vai retornar valor booleano
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8}
conjunto_c = {1,0}
a = conjunto_a.isdisjoint(conjunto_b)
print(a)
b = conjunto_a.isdisjoint(conjunto_c)
print(b)
#add -> adicionar elementos no set
conjunto = {1,2,3}
conjunto.add(25)
print(conjunto)
#clear -> limpar set
conjunto.clear()
print(conjunto)
#copy -> copiar set
conjunto = {1,2,4}
conjunto_copiado = conjunto.copy()
print(conjunto_copiado)
#Discard -> descartar um elemento do set, se passar um valor que não existe no set, ele apenas ignora e segue o programa
conjunto = {1,2,4}
conjunto.discard(4)
conjunto.discard(23)
print(conjunto)
#pop -> vai retirar sempre o valor que estiver na frente
conjunto = {1,2,3,4,5,6}
conjunto.pop()
print(conjunto)
conjunto.pop()
print(conjunto)
#remove -> remover um elemento do set, diferente do discard é que se você passar um valor que não existe no set, vai dá erro no programa
conjunto = {1,2,3}
conjunto.remove(3)
print(conjunto)

#Len -> tirar o tamanho do conjunto
teste = {3,2,4,5,7,8,9}
tamanho = len(teste)
print(tamanho)

#in -> verificar se um objeto está no conjunto, vai retornar um valor booleano
teste = {1,2,3,4,5}
a = 1 in teste
print(a)
b = 10 in teste
print(b)