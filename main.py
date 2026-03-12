from modelo import PessoaFisica, ContaCorrente, Deposito, Saque

def menu():
    text = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [nu] Novo Usuário
    [q] Sair
    => """
    return input(text)

def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            # Exemplo simplificado de lógica de depósito
            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            
            # Aqui buscaríamos a conta do usuário na lista de contas
            if contas:
                conta = contas[0] # Teste com a primeira conta
                cliente = usuarios[0]
                cliente.realizar_transacao(conta, transacao)
            else:
                print("\n@@@ Nenhuma conta encontrada! @@@")

        elif opcao == "nc":
            # Exemplo de criação de usuário e conta
            
            cliente = PessoaFisica(
                cpf="12345678900", 
                nome="Guilherme", 
                data_nascimento="01-01-2000", 
                endereco="Rua das Flores, 123 - Londrina/PR"
            )
            usuarios.append(cliente)
            
            numero_conta = len(contas) + 1
            conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
            contas.append(conta)
            cliente.adicionar_conta(conta)
            
            print("\n=== Conta criada com sucesso! ===")

        elif opcao == "e":
            if not contas:
                print("\n@@@ Nenhuma conta encontrada! @@@")
                continue
                
            conta = contas[0]
            print("\n================ EXTRATO ================")
            transacoes = conta.historico.transacoes

            extrato = ""
            if not transacoes:
                extrato = "Não foram realizadas movimentações."
            else:
                for transacao in transacoes:
                    extrato += f"\n{transacao['tipo']}:\t\tR$ {transacao['valor']:.2f}"

            print(extrato)
            print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            break

if __name__ == "__main__":
    main()