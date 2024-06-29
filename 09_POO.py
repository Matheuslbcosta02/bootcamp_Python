#interfaces -> definir o que uma classe deve fazer. padrão, um contrato.
#interface -> definir um contrato onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas.
#em python não temos a palavra reservada interface como em java, em python usamos CLASSES ABSTRATAS para criar contratos.
#classes abstratas não podem ser instanciadas.
#por padrão python não oferece classes abstratas
#classes abstratas são criadas com o módulo abc (abstract base class)
#abc decora métodos da classe base como abstratos e em seguida registra métodos concretos como implementações da base abstrata
#-------- usar decorador @abstractmethod para tornar um método abstrato
#Quando dizemos que um método é abstrato a classe filha é OBRIGADA a implementar esses métodos , isso deixa código mais padronizado
#Segurança maior para fazer polimorfismo

from abc import ABC , abstractmethod , abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

#Também é possível forçar propriedades dentro da classe abstrata
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligado")

    def desligar(self):
        print("desligado")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("ligado")

    def desligar(self):
        print("desligado")

    @property
    def marca(self):
        return "LG"

p0 = ControleTV()
p0.ligar()
p0.desligar()
print(p0.marca)
print()
p1 = ControleArCondicionado()
p1.ligar()
p1.desligar()
print(p1.marca)
