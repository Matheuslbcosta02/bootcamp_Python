class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#kw -> keyword --- substituir os argumentos da classe pai, pois pode confundir. Argumentos passados apenas por chave = valor
#só deixa os argumentos específicos da classe filho
#SUPER -> palavra reservada para trazer implementação(s) da classe pai super().__init__(**kw) ou uma função específica return super().função()
#Herança -> capacidade da classe filha herdar características e comportamentos da classe pai (classe base)
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass

#Herança múltipla
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
print(Gato)

#MRO -> VER qual ordem o interpretador python vai buscar os atributos e métodos da classe
print(Ornitorrinco.__mro__)
#OU
print(Ornitorrinco.mro())