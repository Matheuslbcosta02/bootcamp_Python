# operadores identidade são operadores usados para comparar se dois objetos ocupam a mesma posição na memória

curso = "testando um curso"

#nome_curso recebe o que está na variável curso
nome_curso = curso   

saldo , limite = 200 , 200

saldo2 , limite2 = 500, 800

#verificar se curso e nome_curso ocupam a mesma região na memória
print (curso is nome_curso)

# verificar se curso e nome_curso NÃO ocupam a mesma região na memória 
print (curso is not nome_curso)

#verificar se saldo e limite ocupam a mesma região na memória
print (saldo is limite)

#verificar se saldo2 e limite2 ocupam a mesma região na memória
print (saldo2 is limite2)