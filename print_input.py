nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(type(nome))
print(type(idade))


print(nome,idade)
print(nome,idade, end = '...\n')
print(nome,idade, sep="--")
print(nome,idade,sep="#")
print(nome,idade,sep="##",end="**\n")