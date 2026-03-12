from abc import ABC, abstractmethod

# Esta é a Interface do diagrama (itálico)
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# Implementação do Saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
         
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
             
            conta.historico.adicionar_transacao(self)

# Implementação do Deposito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            
            conta.historico.adicionar_transacao(self)