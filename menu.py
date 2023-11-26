from os import system
from calculadora import calc
import time
from historico import history



def menu():
    opcao = "1"
    system("cls")
    while opcao != "3":
        print ("----------------------------------------------------------\n")
        print ("\tBem vindo a Calculadora Orientada a Objeto\n")
        opcao = input ("\nDeseja fazer uma operação?\n1 - Sim\n2 - Não\t\n:::  ")
        if opcao == '2':
            opcao = input ("\nDeseja Verificar o historico?\n1 - Sim\n2 - Não\t\n:::  ")

            if opcao == '2':
                print("\n\nFechando o Programa.\n")
                print ("----------------------------------------------------------\n")
                system("pause")
                opcao = "3"
                exit()

            elif opcao == '1':
                history()

            else :  
                print("\n\nNão entendi.\nFechando o Programa.\n")
                print ("----------------------------------------------------------\n")
                system("pause")
                opcao = "3"
                exit()
        elif opcao == '1':
            calc()
        else :  
            print("\n\nNão entendi.\nFechando o Programa.\n")
            print ("----------------------------------------------------------\n")
            system("pause")
            opcao = "3"
            exit()