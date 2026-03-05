"""
O Objetivo desse arquivo é relacionado as matérias - add, remove, tempo...
"""
from core.timer import time_count

subject=[]


def show_subject():
    if not subject:
        print("Nenhuma matéria cadastrada.")
    else:
        for i, sub in enumerate(subject): #enumerate() enumera a lista em -> (i(indice),sub(valor)) 
            print(f"{i} - {sub}")

def add_subject():
    
    show_subject()

    user_add_subject=input("Adicione uma Matéria: ")
    subject.append(user_add_subject)


def rm_subject():

    show_subject()

    try:

        user_rm_subject=int(input("Remova uma Matéria(escolha seu indice): "))
        subject.pop(user_rm_subject)

    except ValueError,IndexError:
        input("Tente novamente - Pressione alguma tecla")
        rm_subject()

    
def main_subject():
    add_subject()
    print('...')
    rm_subject()

