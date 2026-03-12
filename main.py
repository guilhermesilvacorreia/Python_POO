import textwrap
from modelos import PessoaFisica, ContaCorrente, Deposito, Saque

def menu():
    menu_text = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [nu]\tNovo Usuário
    [lc]\tListar Contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_text))

def filtrar_cliente(cpf, usuarios):
    usuarios_filtrados = [u for u in usuarios if u.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    return cliente.contas[0]

def depositar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, usuarios)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, usuarios)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def criar_cliente(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    cliente_existente = filtrar_cliente(cpf, usuarios)

    if cliente_existente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    usuarios.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, usuarios)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("\n=== Conta criada com sucesso! ===")

def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(usuarios)
        elif opcao == "s":
            sacar(usuarios)
        elif opcao == "nu":
            criar_cliente(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)
        elif opcao == "e":
            # Aqui você pode implementar a lógica de extrato similar ao depositar
            pass 
        elif opcao == "q":
            break

if __name__ == "__main__":
    main()