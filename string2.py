#formas de interpolar variáveis em strings

#old style % bem semelhante com a linguagem C  %d %i inteiro// %f float e tem como regular as casas decimais/// %s string ... etc
nome = "julio"
idade = 28
altura = 1.67
print("Meu nome é %s eu tenho %d anos e minha altura é %f" %(nome,idade,altura))
print("Meu nome é %s eu tenho %d anos e minha altura é %.2f" %(nome,idade,altura))
print("Meu nome é %s eu tenho %i anos e minha altura é %f" %(nome,idade,altura))
print()

#método FORMAT
print("Meu nome é {} eu tenho {} anos e minha altura é {}".format(nome,idade,altura))

#essa forma com números é bom se você tiver variáveis repetidas, além de não precisar escrever na ordem dentro do format.
print("Meu nome é {1} eu tenho {0} anos e minha altura é {2}, repetindo meu nome é {1}".format(idade,nome,altura))

#essa forma com format é mais indicada, fica muito mais legível o código
print("Meu nome é {name} eu tenho {age} anos e minha altura é {height}, repetindo meu nome é {name}".format(age=23,name="juli",height=1.65))

#podemos usar também um dicionário é tipo uma struct da linguagem C
dados ={"nome2":"Theu", "idade2":22, "altura2":1.70}
print("Meu nome é {nome2} eu tenho {idade2} anos e minha altura é {altura2}".format(**dados))
print()

#método F-STRING  
# código mais legível e limpo
print(f"meu nome é {nome} eu tenho {idade} anos e minha altura é {altura}")

#formatar string com f-string ajustar casas decimais de um float ou adicionar espaços também
PI = 3.14159
print(f"valor de PI: {PI:.2f}")
print(f"valor de PI: {PI: 10.2f}")