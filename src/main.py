from gastos import registrar_gasto, listar_gastos
from dividas import registrar_divida, listar_dividas

def menu():
    while True:
        print("\n=== CONTROLE FINANCEIRO ===")
        print("1. Registrar gasto")
        print("2. Listar gastos")
        print("3. Registrar dívida")
        print("4. Listar dívidas (com total restante e parcelas)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            registrar_divida()
        elif opcao == "4":
            listar_dividas()
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
