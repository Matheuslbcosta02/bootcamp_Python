#RANGE é uma função built-in do python usado para gerar sequência de n° inteiros.
#range tem início INCLUSIVO e fim EXCLUSIVO
#range (start,stop,step)
#start e step são opcionais, stop é obrigatório!
#range (stop)
#list(range(stop)) converte em lista

for numero in range(0,11):
    print(numero,end=" ")

    
    #exibir tabuada de um número selecionado pelo usuário:
print("\n\n")
numero_tabuada = int(input("digite um número para visualiar a sua tabuada: "))
for numero in range (0,(numero_tabuada * 10 + 1),numero_tabuada):
    print (numero,end=" ")  
