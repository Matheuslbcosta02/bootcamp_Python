#FORMATAR CASAS DECIMAIS EM PYTHON
#manualmente na string:  {variavel :,.Xf} onde X é o número de casas decimais que você deseja que apareçam
variavel = 90 * 2
print(f"{variavel:,.2f}")

#Nós podemos utilizar a função round:
#A função round em Python é uma função embutida que permite arredondar um número para um determinado número de casas decimais.
#1- Arredondar para o inteiro mais próximo// 2- Arredondar para uma casa decimal específica// 3- Arredondar para a casa decimal mais próxima
numero = 3.4514
arredondar_inteiro_proximo = round(numero)
print(arredondar_inteiro_proximo)
#----------------------------------------------------------------
#quando o número da última casa decimal descartada for maior que 4, ocorre o aumento da casa decimal que foi arredondada
#caso a última casa decimal descartada for um número menor ou igual a 4 a casa decimal arredonda é mantida
numero = 3.4567
arredondar_casa_decimal_especifica = round(numero,2)
print(arredondar_casa_decimal_especifica) #Nesse caso será 3.46 pois a última casa descartada é a 3° e o número é 6

numero = 3.4547
arredondar_casa_decimal_especifica = round(numero,2)
print(arredondar_casa_decimal_especifica) #Nesse caso será 3.45 pois a última casa descartada é a 3° e o número é 4

#----------------------------------------------------------------
numero = 2.345
arredondar_casa_decimal_proximo = round(numero,1)
print(arredondar_casa_decimal_proximo) 

#Nós também podemos utilizar a função Decimal do módulo decimal
from decimal import Decimal

exemplo = Decimal('100.0')*5
print(exemplo)

exemplo2 = Decimal('100.00')*5
print(exemplo2)

exemplo3 = Decimal('100.000')*5
print(exemplo3)

exemplo4 = Decimal('100.0000')*5
print(exemplo4)
#ele vai conservar o número de casas decimais passadas no parâmetro da função Decimal entre aspas ""