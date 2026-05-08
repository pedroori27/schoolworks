import security as s
import screen as sc

def show_menu():
    while True:
        print("\n=== BANCO MENU ===")
        print("1 - Ver Saldo")
        print("2 - Deposito")
        print("3 - Saque")
        print("4 - Sair")
        opcao = int(input("Escolha a Opção Desejada: "))
        match opcao:
            case 1:
                see_salary()
            case 2:
                deposit()
            case 3:
                sac()
            case 4:
                s.logout()
                break
            case _:
                print("Opção Inválida!")




# função de ver o saldo

def see_salary():
    print(f"Seu saldo é: R$ {s.activeuser[3]:.2f}")

# função de depósito

def deposit():
    cash = s.activeuser[3]
    value = float(input("Digite o valor do depósito: "))
    if value > 0:
        cash += value
        s.activeuser[3] = cash
        print("Depósito concluído com sucesso!")
    else:
        print("Valor Inválido.")

        # funcão de saque, provavelmente vai ser complementar as tranferências

def sac():
    cash = s.activeuser[3]
    value = float(input("Digite o valor do saque: "))
    if value <= cash and value > 0:
        cash -= value
        s.activeuser[3] = cash
        print("Saque concluído com sucesso!")
    else:
        print("Valor inválido ou Insuficiente.")




# Programa principal
if __name__ == "__main__":
    # Supondo que o login seja feito no módulo de segurança ou em outro lugar
    show_menu()

