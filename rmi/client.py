# saved as greeting-client.py
import Pyro4

# use name server object lookup uri shortcut
tft = Pyro4.Proxy("PYRONAME:example.champion")


def menu():
    print("======== MENU =========")
    print("| 1 - Sistema         |")
    print("| 2 - Características |")
    print("| 3 - Champions       |")
    print("| 4 - Itens           |")
    print("| 5 - Aprimoramentos  |")
    print("| 0 - Sair            |")
    print("=======================")

    opcao = input("Opção desejada: ")
    print(" ")

    if opcao == "1":
        print("Ampliações de Herói")
        print(" ")
        print(tft.sistemas())
        print(" ")
        menuRetorno()
        # subMenuAprimoramentos()

    elif opcao == "2":
        print("Origens")
        print(" ")
        print(tft.caracteristicas())
        print(" ")
        menuRetorno()

    elif opcao == "3":
        print("Champions")
        print(" ")
        print(tft.champions())
        print(" ")
        menuRetorno()

    elif opcao == "4":
        print("Itens")
        print(" ")
        print(tft.itens())
        print(" ")
        menuRetorno()

    elif opcao == "5":
        print("Aprimoramentos")
        print(" ")
        print(tft.aprimoramentos())
        print(" ")
        menuRetorno()

    elif opcao == "0":
        print("Saindo...")
        exit()

    else:
        print("Opção inexistente, escolha novamente.")
        menu()


def menuRetorno():
    print("========== MENU ===========")
    print("| 1 - Voltar para o Inicio |")
    print("| 0 - Sair                |")
    print("===========================")

    opcao = input("Opção desejada: ")
    print(" ")

    if opcao == "1":
        menu()

    elif opcao == "0":
        print("Saindo...")
        exit()

    else:
        print("Opção inexistente, escolha novamente.")
        menuRetorno()


"""
def subMenuAprimoramentos():
    print("Novos Aprimoramentos")
    print(" ")

    print("==================== MENU ===================")
    print("| 1 - Ver todos os aprimoramentos de Heróis |")
    print("| 2 - Voltar                                |")
    print("| 0 - Sair                                  |")
    print("=============================================")

    opcao = input("Opção desejada: ")
    print(" ")

    if opcao == "1":
        print(tft.allAprimoramentos())
        print(" ")
        menuRetorno()
"""


menu()
