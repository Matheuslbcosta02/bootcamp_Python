#funções em python -> bloco de código identificado por nome que pode receber parâmetros ou não. Código mais legível e reaproveitamento de código
#Programar de maneira estruturada -> é programar baseado em funções. Funções podem retornar vários valores em python.

def exibir_mensagem():
    print("Olá mundo")

exibir_mensagem()
#--------------------------------

def exibir2(nome):
    print(f"Olá {nome}")

exibir2(nome = "Theu1") 
#OU
exibir2("Theu2")
#--------------------------------

def exibir3(nome = "Marte"):
    print(f"Olá {nome}")

exibir3()
#OU
exibir3(nome = "Theu3")    
#--------------------------------

#Toda função python retorna None por padrão
def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor , sucessor 


print(calcular_total([10,20,34]))
print(retornar_antecessor_sucessor(10))

#none
def func():
    print("olá")

print(func())
#--------------------------------
def carro(marca,modelo,ano,placa):
    print(f"carro: {marca}/{modelo}/{ano}/{placa}")

print(carro("fiat","palio",1999,"abc-1234"))
print(carro(marca = "fiat",modelo = "palio" , ano = 1999, placa = "abc-1234"))

# INDICAR QUE É UM DICIONÁRIO -> ** (DOIS ASTERÍSTICOS) kwargs
print(carro(**{"marca":"fiat","modelo":"palio","ano":1999,"placa":"abc-1234"}))
#--------------------------------

# ARGS E KWARGS -> quando *args o método recebe os valores como tupla ///// quando **kwargs o método recebe os valores como dicionário
def exibir_poema(data,*args,**kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

print(exibir_poema("sexta,26 ago,2022","Zen of python","beautiful is better than ugly",autor = "Tim Peters",ano = 1995))

# O NOME ARGS E KWARGS pouco importa, o interpretador vai olhar o asterístico *,**,ou sem.
#--------------------------------

#para melhor legibilidade e desempenho -> restringir a forma que os argumentos serão passados
#argumentos podem ser passados por posição, por posição e nome, ou por nome.
#def f(pos1,pos2, /, pos_or_kwd, *,kwd1,kwd2)
#antes do / só por posição, 
# depois do / pode ser posição ou keyword ,
#  depois do * só por keyword
def carro(modelo,ano,/,marca,motor):
    print(modelo,ano,marca,motor)

print(carro("palio",1999, marca="fiat",motor="1.0" ))

def carro2(*,modelo,ano,marca,motor):
    print(modelo,ano,marca,motor)

print(carro2(modelo = "palio",marca="fiat",ano=1999,motor="1.0"))   
#--------------------------------

#Em python tudo é objeto, funções também são objetos o que as tornam OBJETOS DE PRIMEIRA CLASSE
#Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados(lista,tupla,dicionário)
#Além de poder usar funções como valor de retorno(closures)
def somar(a,b):
    return a+b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"o resultado é {resultado}")

print(exibir_resultado(10,10,somar))

def sub (a,b):
    return a- b

op = somar
print(op(1,20))
#--------------------------------
#ESCOPO LOCAL E GLOBAL
#Para usar objetos globais utilizamos a palavra chave global -> NÃO É UMA BOA PRÁTICA, EVITAR!
#alterações feitas localmente em objetos imutáveis serão perdidas com o fim do bloco, agora mutáveis não.
salario = 2000
def salario_bonus(bonus):
    global salario
    salario +=bonus
    return salario
print(salario_bonus(500))

#Se pegar um objeto mutável como uma lista -> mesmo após o fim do bloco as alterações não serão perdidas