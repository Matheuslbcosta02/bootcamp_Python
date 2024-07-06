# TODO: Crie uma classe UsuarioTelefone. 
class UsuarioTelefone:
  # TODO: Defina um método especial `__init__`, que é o construtor da classe.
  def __init__(self,nome,numero,plano):
    self._nome = nome
    self._numero = numero
    self._plano = plano
    
  @property
  def nome(self):
    return self._nome
        
  @nome.setter
  def nome(self,nome):
    self._nome = nome
        
  @property
  def numero(self):
    return self._numero
        
  @numero.setter
  def numero(self,numero):
    self._numero = numero
        
  @property
  def plano(self):
    return self._plano
        
  @plano.setter
  def plano(self,plano):
    self._plano = plano
        
      
  # O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
  
  
          
      # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
        
  
      # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
  def __str__(self):
    return f"Usuário {self._nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome,numero,plano)
print(usuario)