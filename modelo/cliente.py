class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []   

    def realizar_transacao(self, conta, transacao):
         
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento