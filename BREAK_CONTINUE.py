#Break vai parar a execução, acaba o laço.
#continue vai pular a execução, volta para o começo, e o que estiver embaixo é ignorado naquela repetição que foi pulada.

#quando chegar no 10 o laço será encerrado com o BREAK
for numero in range(20):
    if numero == 10:
        break
    print(numero, end = " ")

print("\n\n")

#quando chegar no 10 o laço irá pular o 10, mas vai continuar até o final com o CONTINUE
for numero2 in range(20):
    if numero2 == 10:
        continue
    print(numero2, end = " ")    

print ("\n\n")

#exibir somente número ímpar
for numero_impar in range (20):
    if numero_impar % 2 == 0:
        continue
    print (numero_impar, end = " ")
#Sempre que o resto da divisão dos números do range por 2 for exatamente igual a zero, o if será atendido e irá cair dentro dessa estrutura
# condiconal, ou seja o CONTINUE será ativado e o print logo abaixo será ignorado, ele vai pular esse print e retornará para o início do laço
# de repetição FOR. Os números que tiverem o resto da divisão por 2 igual a zero não serão impressos na tela para o usuário.    