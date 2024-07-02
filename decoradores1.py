#decoradores serve para checagem de segurança, personalização de comportamento em outra função, etc...

def meu_decorador(funcao):
    #inner function
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope

def ola_mundo():
    print("olá mundo")

#para decorar a função -> atribui um novo valor a função, sendo esse valor o decorador com a função que será decorada  passada como parâmetro:
ola_mundo = meu_decorador(ola_mundo)
ola_mundo() #chamando a função decorada

#----------------------------------------- maneira melhor de decorar é utilizando o @"nome_da_função_decoradora" antes de declarar a função
#que você quer decorar

@meu_decorador
def ola_mundo2():
    print("olá mundo 2 sendo decorado")

ola_mundo2()
#pricipal uso de decoradores -> adicionar funcionalidades a uma função ou classe existente sem modificar sua estrutura