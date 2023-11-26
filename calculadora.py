from os import system
from historico import hist
from historico import op_his
from historico import valor1
from historico import valor2

num=[0,0]

def nume():
        print("\nDigite dois números para a operação:")
        num[0]=(float(input("Primeiro número: ")))
        num[1]=(float(input("Segundo número: ")))
        
def calc():
    op=input('\nDigite qual operação:\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n:::  ')
    
    if op == '1':
        nume()
        mat()
    elif op == '2':
        nume()
        sub()
    elif op == '3':
        nume()
        div()
    elif op == '4':
        nume()
        mul()
    else:
        print("\nNão entendi.\nPoderia repetir.")
        system('pause')
        calc()



def mat():
    resul = num[0] + num[1]
    print("A soma dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num[0])
    valor2.append(num[1])
    op_his.append("1")


def sub():
    resul = num[0] - num[1]
    print("A subtração dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num[0])
    valor2.append(num[1])
    op_his.append("2")

def div():
    resul = num[0] / num[1]
    print("A divisão dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num[0])
    valor2.append(num[1])
    op_his.append("3")

def mul():
    resul = num[0] * num[1]
    print("A multiplicação dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num[0])
    valor2.append(num[1])
    op_his.append("4")