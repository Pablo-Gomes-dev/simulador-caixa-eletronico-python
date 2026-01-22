ARQUIVO_SALDO = "saldo.txt"


def carregar_saldo():
    try:
        with open(ARQUIVO_SALDO, "r") as f:
            return float(f.read())
    except FileNotFoundError:
        return 0.0
    except ValueError:
        return 0.0


def salvar_saldo(saldo):
    with open(ARQUIVO_SALDO, "w") as arquivo:
        arquivo.write(f"{saldo}")


def consultar_saldo(saldo):
    print(f"\nSaldo atual: R$ {saldo:.2f}")


def depositar(saldo):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor <= 0:
            print("Valor inválido. O depósito deve ser maior que zero.")
            return saldo

        saldo += valor
        salvar_saldo(saldo)
        print("Depósito realizado com sucesso.")
        return saldo

    except ValueError:
        print("Entrada inválida. Por favor, Digite um numero.")
        return saldo


def sacar(saldo):
    try:
        valor = float(input("Informe o valor do saque: R$ "))
        if valor <= 0:
            print("Valor inválido.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            salvar_saldo(saldo)
            print("Saque realizado com sucesso.")
        return saldo

    except ValueError:
        print("Entrada inválida. Digite um numero.")
        return saldo


def exibir_menu():
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")


def main():
    saldo = carregar_saldo()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consultar_saldo(saldo)

        elif opcao == "2":
            saldo = depositar(saldo)

        elif opcao == "3":
            saldo = sacar(saldo)

        elif opcao == "4":
            print("Encerrando o sistema. Obrigado por utilizar.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
