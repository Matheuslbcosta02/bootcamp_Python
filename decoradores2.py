#funções decoradas com argumentos -> usar *args e **kwargs
#pricipal uso de decoradores -> adicionar funcionalidades a uma função ou classe existente sem modificar sua estrutura
def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)

    return envelope

@duplicar
def aprender(tecnologia):
    print(f"estou aprendendo {tecnologia}")

aprender('python')

#poderia passar com o nome tecnologia direto lá em cima, mas se tiver alterações no código fica complicado. args e kwargs é melhor

#retornando valores de funções decoradas, envelope está guardando o valor de nossa função decorada

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)  #estams retornando o valor da função passada no argumento

    return envelope #agora envelope irá retornar o valor de nossa função decorada

@duplicar
def aprender(tecnologia):
    print(f"estou aprendendo {tecnologia}")
    return tecnologia.upper() #esse é o valor de nossa função decorada //// esse valor será retornado pelo envelope agora

resultado = aprender('python')
print(resultado)


#introspecção é a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução
#com decorador nossos objetos perdem essa introspecção
#para corrigir -> import functools e coloca @functools.wraps(nome_do_parametro_do_decorador) antes de definir envelope

# import functools
#def duplicar (func):
# @functools.wraps(func)
# def envelope(*args,**kwargs) ....