#estruturas condicionais permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

maior_idade = 18
idade_especial = 17

idade = int(input("Insira sua idade: "))

#estrutura condicional
#elif é como se fosse um else if
if idade >= maior_idade:
    print("Pode tirar CNH.")
elif idade == idade_especial:
    print("Pode fazer aulas teóricas, mas não pode realizar aulas práticas!")
else:
    print("Não pode tirar CNH.")        