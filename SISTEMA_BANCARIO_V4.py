from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class ContaIterador:
    def __init__(self,contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True

        else:
            print("\nOperação falhou! O valor informado é inválido. Tente novamente :)")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nOperação falhou! O valor informado é inválido. Tente novamente :)")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n Operação falhou! O valor do saque excede o limite. :(")

        elif excedeu_saques:
            print("\n Operação falhou! Número máximo de saques excedido. :(")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                
                
            }
        )

    def gerador_transacoes(self, tipo_transacao = None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    
    @abstractmethod
    def registrar(self,conta):
        pass

class Deposito(Transacao):
    def __init__ (self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
   
class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor (self):
        return self._valor

    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []
        

    def realizar_transacao(self,conta,transacao):
       transacao.registrar(conta)
    
    def adicionar_conta(self,conta):
        self.contas.append(conta)
    
class pessoaFisica(Cliente):
    def __init__(self,cpf,nome,data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        super().__init__(endereco)

def log_transacao(funcao):
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        print(f"{datetime.now()}: {funcao.__name__.upper()}")
        return resultado
    
    return envelope


def menu():
    menu = ''' **************SISTEMA BANCÁRIO**************
    Seja bem-vindo ao nosso banco! Selecione uma opção para prosseguir:
    [S] SAQUE
    [D] DEPÓSITO
    [E] EXTRATO
    [NU] CRIAR NOVO USUÁRIO
    [NC] CRIAR NOVA CONTA
    [LC] LISTAR CONTAS DO BANCO
    [Q] SAIR
    \n
    '''
    return input(menu).upper() 

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]  

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao) 

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado! ")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerador_transacoes(tipo_transacao="saque"):
        
        tem_transacao = True
        extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    for transacao in conta.historico.gerador_transacoes(tipo_transacao="deposito"):
        
        tem_transacao = True
        extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = pessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\nCliente criado com sucesso!")  

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado, primeiramente cadastre um novo usuário e logo em seguida poderá criar uma conta!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(str(conta))

def main(): 
    clientes = []
    contas = []
    while True:
        opcao = menu()

        if opcao == 'D':
            print("Você selecionou a opção depósito.")
            depositar(clientes)

        elif opcao == 'S':
            print("Você selecionou a opção saque.")
            sacar(clientes)

        elif opcao == 'E':
            exibir_extrato(clientes)

        elif opcao == 'NU':
            print("Você selecionou a opção Criar novo usuário.")
            criar_cliente(clientes)


        elif opcao == 'NC':
            print("Você selecionou a opção para criar uma nova conta.")
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)


        elif opcao == 'LC':
            print("Você selecionou a opção para listar as contas do nosso banco.")
            listar_contas(contas)    

        elif opcao == 'Q':
            print("Obrigado por utilizar o nosso banco, até breve! :) \n\n")
            break

        else:
            print("Opção selecionada é inválida. Por gentileza, digite novamente.")

main()