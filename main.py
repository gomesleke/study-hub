import os
from core.timer import main_timer


def clear():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")

    
def selection():
    print("Selecione:\n")
    print("1-Começar Estudos")
    print("2-Relatório")
    print("3-Histórico")
    print("4-Metas")
    print("5-Configurações")
    print("6-Sair")


def menu():

    clear()

    print("============")
    print("\nSTUDY TRACKER (CLI)\n")
    print("============\n")

    selection()


def main():
    menu()
    



if __name__=="__main__":
    main()