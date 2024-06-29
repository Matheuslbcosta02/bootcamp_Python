#métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe
#por convenção o 1° argumento que os métodos de classe recebem é o "cls" para apontar para a classe e não self que é de instância
#usamos geralmente para criar métodos de fábrica (métodos que retornam instâncias daquela classe)
# ------ Usar o decorador @classmethod para transformar o método em método de classe

#métodos estáticos não recebem um 1° argumento explícito, ele também é um método vinculado à classe e não ao objeto da classe
#esse método não pode acessar e nem modificar o estado da classe 
#ele não recebe um argumento para apontar para uma referência explícita, ele pode receber nenhum argumento ou n argumentos
#onde esses n argumentos serão valores, não é nenhuma referência para classe ou objeto em sí
#usamos geralmente para criar funções utilitárias (validar algo por exemplo)
#-------- usar o decorador @staticmethod para decorar que o método é estático

class Pessoa:
    def __init__(self,nome = None,idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2024 - ano
        return cls(nome,idade)
    
    @staticmethod
    def maior_idade(idade):
        a = idade >= 18
        if a:
            return "Maior de idade"
        else:
            return "menor de idade"
        

p = Pessoa.criar_data_nascimento(2000,3,21,"gui")
print(p.nome,p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(21))
print(Pessoa.maior_idade(8))