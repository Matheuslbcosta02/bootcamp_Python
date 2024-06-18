#Dicionário -> Conjunto não-ordenado de pares chave:valor  , chave é um valor imutável
#declarar com chaves { } ou com o dict
pessoa = {"nome":"Theu","idade":28}
pessoa = dict(nome = "Theu", idade = 28)

#Acessar dados e modificar ou criar nova chave, se a chave já existir ela vai ter o valor sobreescrito.
pessoa["nova_chave"] = "testando"
print(pessoa["nome"])
pessoa["nome"] = "Theus"

#Dicionários aninhados -> dicionários podem armazenar qualquer tipo de objeto em python, inclusive outros dicionários, pode ter vários
contatos = {
    "theu@gmail.com":{"nome":"Theu","extra":{"a":1}}
}
extra = contatos["theu@gmail.com"]["extra"]["a"]
print(extra)

#Iterar dicionários -> FOR
teste = {
    "tuti@gmail.com":{"nome":"tuti","telefone":"3333-1111"},
    "caio@gmail.com":{"nome":"caio","telefone":"2222=3333"},
    "julia@gmail.com":{"nome":"julia","telefone":"1111-2344"},
}
for chave in teste:
    print(chave,teste[chave])

print()

# A MELHOR FORMA É USANDO O MÉTODO ITEMS !!!
for chave2 , valor in teste.items():
    print(chave2, valor)

# MÉTODOS DA CLASSE DICT
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
#clear -> limpar dicionário
contatos.clear()
print(contatos)

#copy -> copiar um dicionário
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
copia = contatos.copy()
copia["gui@gmail.com"] = {"nome":"Guizao"}
print(copia)

#fromkeys -> criar chaves com valor NONE (sem nada) ou você criar e passar um valor padrão
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
a = contatos.fromkeys(["nova_chave","outra_chave"])
b = contatos.fromkeys(["chave_default","outrachave_default"],"VAZIO")
print(a)
print(b)
print()

#get -> acessar valores em um dicionário quando não tem certeza se existe aquela chave, o get evita o KEYERROR acessando diretamente
contatos2 = {
    "a":{"nome":"gui","telefone":"3333-1111"},
    "nova_chaves":{"nome":"THEU"},
}
#acessando diretamente uma chave que não existe -> keyerror 
#contatos["chave_inexistente"] -> programa interrompido, keyerror
#com o get não dá problema ele retorna none ou um valor padrão que você passar, caso a chave não exista, se existe ele retorna a chave e o valor
print(contatos2.get("a",{}))
print(contatos2.get("chave"))
print(contatos2.get("chavee","não encontrado"))
print(contatos2.get("chaveee",{}))
print(contatos2.get("nova_chaves"))
print()

#items -> retorna uma lista de tuplas, muito útil para iterar com o comando FOR
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
print(contatos.items())
print()

#keys -> retorna todas as chaves do dicionário , já o values retorna os valores
contatos2 = {
    "a":{"nome":"gui","telefone":"3333-1111"},
    "nova_chaves":{"nome":"THEU"},
}
print(contatos2.keys())
print()

#pop -> remover uma chave do dicionário, e ainda pode informar um valor padrão, caso ele não ache a chave, se ele achar ele retorna o valor
# encontrado para remoção.
contatos2 = {
    "a":{"nome":"gui","telefone":"3333-1111"},
    "nova_chaves":{"nome":"THEU"},
}
print(contatos2.pop("a"))
print(contatos2.pop("a",{}))
print(contatos2.pop("chave_inexistente","valor default"))
print()

#popitem -> ele vai retirando na sequência, sem precisar informar chave. Se tiver vazio vai dá erro - KEYERROR
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
print(contatos.popitem())
print()

#setdefault -> criar chave com valor passado, caso a chave já exista ele vai respeitar o que já está no dicionário
#setdefault -> maneira mais elegante para colocar valor em um dicionário, para não ficar precisando verificar se tem aquela chave ou não
contatos = {"nome":"gui","telefone":"3333-1111"}
contatos.setdefault("nome","nãovaimudar")
contatos.setdefault("idade" , 30)
print(contatos)
print()
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
contatos["gui@gmail.com"].setdefault("nome", "nãomuda")
contatos["gui@gmail.com"].setdefault("idade", 25)
print(contatos)
print()

#update -> atualizar o dicionário
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
contatos.update({"novo":"teste"})
contatos.update({"gui@gmail.com":{"nome":"THEU"}})
print(contatos)
print()

#values -> retorna valores do dicionário , já o keys retorna as chaves
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
print(contatos.values())
print()

#in -> verificar se uma chave existe ou não no dicionário, vai retorar valor booleano
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
print("gui@gmail.com" in contatos)
print("meugui@gmail.com" in contatos)
print("telefone" in contatos["gui@gmail.com"])
print()

#del -> tirar algo do dicionário
contatos = {
    "gui@gmail.com":{"nome":"gui","telefone":"3333-1111"}
}
del contatos["gui@gmail.com"]["telefone"]
print(contatos)

#DEL NOME_DICIONÁRIO -> apaga o dicionário inteiro
del contatos
