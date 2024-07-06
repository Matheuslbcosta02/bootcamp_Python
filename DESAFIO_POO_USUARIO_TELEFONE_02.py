# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
  def __init__(self,nome,saldo):
    self._nome = nome
    self._saldo = saldo
    
  @property
  def nome(self):
    return self._nome
    
  @property
  def saldo(self):
    return self._saldo
    
  @nome.setter
  def nome(self,nome):
    self._nome = nome
    
  @saldo.setter
  def saldo(self,saldo):
    self._saldo = saldo
  
  def verificar_saldo(self):
    if self._saldo < 10 :
      return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
      
    elif self._saldo >= 50 :
      return "Parabéns! Continue aproveitando seu plano sem preocupações."
  
    else:
      return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

#objeto plano da classe PlanoTelefone será criado e passado para a criação do objeto da classe UsuarioTelefone
# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
        
    def verificar_saldo(self):
      #acessando o método verificar_saldo do objeto plano da classe PlanoTelefone
      return self.plano.verificar_saldo()

# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  
#passa o objeto plano_usuario da classe PlanoTelefone para a criação do objeto usuario
# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)