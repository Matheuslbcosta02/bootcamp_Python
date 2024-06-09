#operadores lógicos são usados em conjunto com os operadores de comparação

#operador E
print (3 > 5 and 5==5)
print (3>2 and 2<4)

#operador OU
print (3 > 5 or 5 == 5)
print (3>6 or 6>8)

#operador not
print (not 100 > 150)

#lista é uma sequência de objetos, e string é uma sequência de caracteres, em python sequência vazia é considerado falso
contatos = []
print (not contatos)
print (not "saque 1500")
print (not "")