def capitalize_decorator(func): 
    def wrapper(): 
        return func().upper() 
    return wrapper 

@capitalize_decorator 
def greet(): 
    return "hello" 

print(greet())

#pricipal uso de decoradores -> adicionar funcionalidades a uma função ou classe existente sem modificar sua estrutura