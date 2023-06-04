
from math import sqrt, floor


def primo_rapido():
    """
    Esta função calcula e printa "Prime" se o número fornecido pelo
    usuário é primo, ou caso contrário, "Not Prime".
    :return:
    """
    arq = open("test.csv")
    l1 = list(map(int, arq))
    print(l1)
    print(len(l1))
    cont = 0
    for k in range(1, len(l1)):
        div = floor(sqrt(l1[k]))
        if l1[k] == 2 or l1[k] == 3:
            print("Prime")
        elif l1[k] == 1 or l1[k] > 2 and l1[k] % 2 == 0:
            print("Not Prime")
        else:
            for i in range(2, div + 1):
                if l1[k] % i == 0 and i != div:
                    print('Not Prime')
                    break
                elif i == div and sqrt(l1[k]) != div:
                    print('Prime')
                    break
                elif i == div and sqrt(l1[k]) == div:
                    print("Not Prime")
                    break
    cont += 1


primo_rapido()
