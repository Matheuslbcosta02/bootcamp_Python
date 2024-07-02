#iterador -> objeto que tem um n° contável de valores que podem ser iterados.
#iterador -> sua classe precisa ter dois métodos especiais para ser uma classe iterável, para ser possível a iteração no seu objeto
# __iter__()                  __next__()
# comando readline() vai identificando as linhas e lendo 
# comando raise StopIteration -> finalizar o laço// sinalizar para o iterador
#método __iter__() -> retorna objeto iterador para a classe
#método __next__() -> retorna o próximo ítem da sequência
class MeuIterador:
    def __init__ (self,numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__ (self):
        return self
    
    def __next__ (self):
        try:
            numero = self.numeros [self.contador]
            self.contador +=1
            return numero * 2
        
        except IndexError:
            raise StopIteration
        
#usando iterador
for i in MeuIterador (numeros = [3,6,9]):
    print (i)
