#ENCAPSULAMENTO -> código mais dinâmico e seguro, não expõe diretamente dados do atributo
#MODIFICADORES DE ACESSO -> diferente de java, c++, etc... python não tem palavra reservada para definir nível de acesso aos atributos e
#métodos da classe.
#----------------------------CONVENÇÃO----------------------------------- Isso vale para atributos e métodos:
#privado -> underline antes do nome da variável
#público -> só escreve o nome
#Se for privado -> não devemos manipular o seu valor ou invocar método fora do escopo da classe
class Conta:
    def __init__(self,nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar (self, valor):
        self._saldo += valor

    def sacar (self, valor):
        self._saldo -= valor

    #CORRETO -> verificar se a pessoa tem acesso para ver o saldo, ter um atributo ou método dentro da classe para exibir não diretamente fora.
    #Se fizermos print(conta._saldo) vai funcionar, o interpretador python não impede, mas está errado!! atributo privado

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0001",200)
#depositar nesse exemplo é público, então podemos fazer esse método fora da classe
conta.depositar(100)
#atributo nro_agencia é público, podemos fazer isso aqui fora da classe
print(conta.nro_agencia)

print(conta.mostrar_saldo())

#PROPERTIES -> criar atributos gerenciados(ou computados) em classes. Podemos usar propriedades quando formos modificar sua implementação
#interna sem alterar a API pública da classe.
# @ -> decorador (uma função que executa antes da sua função)

#property -> precisa para retornar valor
#setter -> precisa para modificar, fazer uma atribuição
#deleter -> para poder deletar

class Foo:
    def __init__ (self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x (self, value):
        self._x  += value

    @x.deleter
    def x (self):
        self._x = 0


foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)

print()
print()
class Pessoa:
    def __init__ (self,nome,ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

        #VAMOS DEFINIR UMA PROPRIEDADE PARA LER O NOME E DEFINIR UMA PROPERTY PARA PEGAR A IDADE DA PESSOA

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade (self):
        _ano_atual = 2024

        return _ano_atual - self._ano_nascimento
    

pessoa = Pessoa("Theu", 2002)

print (f"nome:{pessoa.nome} \t idade: {pessoa.idade}")

