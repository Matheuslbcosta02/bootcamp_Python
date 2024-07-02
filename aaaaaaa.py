def capitalize_decorator(func): 
    def wrapper(): 
        return func().upper() 
    return wrapper 

@capitalize_decorator 
def greet(): 
    return "hello" 

print(greet())
print()
print()
it = iter([1, 2, 3]) 
print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it))