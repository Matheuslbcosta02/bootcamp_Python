#Polimorfismo -> ter muitas formas, uma função sendo usada para diferentes tipos
#Mesmo método com comportamento diferente

class Passaro:
    def voar (self):
        print("voando")

class Pardal(Passaro):
    def voar (self):
        super().voar()

class Avestruz(Passaro):
    def voar (self):
        print("Avestruz não voa")

#Polimorfismo -> plano_de_voo quer um objeto que tenha o método voar, o método plano de voo terá comportamentos diferentes dependendo do objeto
#Método polimórfico pode se comportar de diferentes formas
#NÃO É POSSÍVEL TER POLIMORFISMO SEM HERANÇA

def plano_de_voo (passaro):
    passaro.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
p1 = Pardal()
p2 = Avestruz()
plano_de_voo(p1)
plano_de_voo(p2)