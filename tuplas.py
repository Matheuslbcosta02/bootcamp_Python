#tuplas são muito parecidas com listas, a principal diferença é que tuplas são imutáveis
#Usar tuplas sempre que quisermos ter garantia que o valor não será alterado.
#Tentar alterar o valor de uma tupla irá gerar um erro.
#criar tuplas ou com a classe tuple/// ou colocando valores separados por víruglas entre parênteses

frutas = ("laranja","pera","uva",)
#BOA PRÁTICA EM TUPLAS -> colocar vírgula antes do parênteses que fecha a tupla para não confudir o interpretador com parênteses de precedência
print()
#tuple é igual o list vai pegar e o elemento python e colocar na tupla com cada letra sendo um elemento p,y,t,h,o,n
letras = tuple("python")
print(letras)
numeros = tuple([1,2,3,4])
print(numeros)
pais = ("Brasil",)

#Acesso direto é com índices
print(frutas [0])
print(frutas[-1])

#TUPLAS ANINHADAS -> tuplas podem armazenar todos os tipos de objetos, inclusive tuplas que armazenam tuplas
#com isso podemos criar estruturas bidimensionais (tabelas), para acessar informar os índices [linha][coluna]
matriz = (
    (1,"a",2),
    ("b",3,4),
    (6,5,"c"),
)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#FATIAMENTO --> [start:stop:step]
tupla = ("p","y","t","h","o","n",)
print(tupla [2:])
print(tupla [:2])
print(tupla [1:3])
print(tupla [0:3:2])

#cópia
print(tupla[::])

#espelhamento
print(tupla[::-1])

##Iterar tuplas --> FOR
carros = ("gol","celta","palio",)
for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")

# MÉTODOS DA CLASSE TUPLE -> tuplas são muito limitadas pelo fato de serem imutáveis, então tem poucos métodos.
#().count -> contar quantas vezes um elemento aparece nela
cores = ("vermelho","azul","verde","azul",)

print(cores.count("vermelho"))
print(cores.count("azul"))

#().index -> saber em qual posição está o objeto na tupla
print(cores.index("azul"))
print(cores.index("vermelho"))
print(cores.index("verde"))

#LEN -> Saber o tamanho da tupla
print(len(cores))

# FUNÇÃO ISINSTANCE -> função que retorna um valor booleano true or false, indicando se o objeto é ou não do tipo indicado
# Não é tupla -> vai sair falso --->> *COLOCAR VÍRUGLA* BOA PRÁTICA PARA TUPLAS
carrosteste = ("celta")
print(isinstance(carrosteste,tuple))

#Nesse caso vai sair verdadeiro -> VÍRGULA
carroteste = ("gol",)
print(isinstance(carroteste,tuple))
