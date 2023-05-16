def rodizio_veicular():
    """
    Esta função tem como retorno um print com o dia da semana
    que um veículo automotor não pode trafegar pelas ruas com
    base nos seu último algarismo contante em sua placa.
    :return:
    """
    n = int(input())
    alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    for i in range(n):
        placa = input()
        if len(placa) == 8:
            if placa[0] in alfa and placa[1] in alfa and placa[2] in alfa and placa[3] == "-":
                if placa[4] in num and placa[5] in num and placa[6] in num and placa[7] in num:
                    ultimo = int(placa[7])
                    if ultimo == 1 or ultimo == 2:
                        print("MONDAY")
                    elif ultimo == 3 or ultimo == 4:
                        print("TUESDAY")
                    elif ultimo == 5 or ultimo == 6:
                        print("WEDNESDAY")
                    elif ultimo == 7 or ultimo == 8:
                        print("THURSDAY")
                    elif ultimo == 9 or ultimo == 0:
                        print("FRIDAY")
                else:
                    print("FAILURE")
            else:
                print("FAILURE")
        else:
            print("FAILURE")
    if n == 0:
        print("FAILURE")


rodizio_veicular()
