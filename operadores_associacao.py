# operadores usados para verificar se um objeto está presente em uma sequência
#esses operadores são case sensitive, ou seja, letras maiúsculas e minúsculas fazem diferença
curso = "curso de Python"
frutas = ["laranja", "uva"]
saques = [1550, 100]

#verificando se a string Python está na string curso
print ("Python" in curso)

#colocando letra minúscula
print ("python" in curso)

#veriicando se maçã está na lista frutas
print ("maçã" in frutas)

#verificando se maçã não está na lista frutas
print ("maçã" not in frutas)

#verificando se 200 está em saques
print (200 in saques)

#verificando se 100 está em saques
print (100 in saques)