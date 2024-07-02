#podemos definir funções dentro de outras funções, além de poder retornar funções de funções também
#podemos usar funções como valores de retorno

def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


op = calculadora("+")
print(op(2, 2))
op = calculadora("-")
print(op(2, 2))
op = calculadora("*")
print(op(2, 2))
op = calculadora("/")
print(op(2, 2))

#podemos usar funções como parâmetros em outras funções também. exemplo:
def mensagem(funcao):
    return funcao

def oi():
    return f"oiiii"

print(mensagem(oi()))
#----------------------------- exemplo 2:
#--------------------------------
def mensagem2(funcao2,frase):
    return funcao2(frase)

def oi2(frase):
    return f"{frase}"


print(mensagem2(oi2,'olá amigo'))



