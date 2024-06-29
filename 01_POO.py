#paradigma de programação -> estilo de programção
#POO -> Classes e objetos
#classe -> define características e comportamentos de um objeto
#Objeto -> podemos usá-lo e ele possue as características e comportamentos definidos na classe

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor 
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor 

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def buzinar(self):
        print("Plim plim")

    def correr(self):
        print("vruuumm") 

    #REPRESENTAÇÃO DA CLASSE
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#variáveis -> características que são atributos da classe
#comportamentos da classe são definidos pelos métodos
#Métodos são funções dentro de uma classe, a diferença é que precisamos passar um argumento, que por convenção chama-se SELF

b1 = Bicicleta("verde","caloi", 2022, 600) 

b1.buzinar()
b1.correr()
b1.parar()

#mesma coisa que 
#Bicicleta.buzinar(b1) \\\\\ Bicicleta.correr(b1) \\\\\\ Bicicleta.parar(b1)
#NÃO PODE DEFINIR O NOME DO MÉTODO IGUAL AO DO ATRIBUTO -> ERRO

print(b1.cor)
print(Bicicleta.__str__)

#CONSTRUTORES DE DESTRUTORES
#MÉTODO CONSTRUTOR -> Executado quando nova instância da classe é criada, nesse método inicializamos o método do nosso objeto
#MÉTODO CONSTRUTOR -> def __init__ (self, ...)

#MÉTODO DESTRUTOR -> Executado quando a instância do objeto é destruída.
#Não é muito comum em python, como por exemplo é em C++, pois em python temos um coletor de lixo que gerenciar a memória
#MÉTODO DESTRUTOR -> def __del__ (self)

