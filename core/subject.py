"""
O Objetivo desse arquivo é relacionado as matérias - add, remove, tempo...
"""
from core.timer import time_count

subject=[]

size_subject=len(subject)

def add_subject():
    user_add_subject=input("Adicione uma Matéria: ")
    subject.append(user_add_subject)

def rm_subject():

    for i in range(size_subject):
        print(f"{i}-{subject[i]}")

    user_rm_subject=int(input("Remova uma Matéria(escolha seu indice): "))

    try:
    
        for i in range(size_subject):
            if user_rm_subject==subject[i]: # percorre a lista
                subject.pop(i)
            else:
                print("Não encontrado")

    except ValueError:
        print("Try again")