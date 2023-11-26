from os import system

hist = []
op_his = []
valor1 = []
valor2 = []


def history():
    i = int(len(hist))
    a = 1
    while (i > 0):
            print()
            if op_his[i-1] == '1':
                print("A " + str(a) + "° conta o resultado da soma de " + str(valor1[i-1]) + " + " + str(valor2[i-1]) + " = " + str(hist[i-1]))
            if op_his[i-1] == '2':
                print("A " + str(a) + "° conta o resultado da subtração de " + str(valor1[i-1]) + " - " + str(valor2[i-1]) + " = " + str(hist[i-1]))
            if op_his[i-1] == '3':
                print("A " + str(a) + "° conta o resultado da divisão de " + str(valor1[i-1]) + " / " + str(valor2[i-1]) + " = " + str(hist[i-1]))
            if op_his[i-1] == '4':
                print("A " + str(a) + "° conta o resultado da multiplicação de " + str(valor1[i-1]) + " * " + str(valor2[i-1]) + " = " + str(hist[i-1]))                      
            i-=1      
            a+=1      

    print("\n\n\n")
    system("Pause")