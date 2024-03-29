from math import sqrt, ceil


def primo_rapido():
    """
    Esta função calcula e printa "Prime" se o número fornecido pelo
    usuário é primo, ou caso contrário, "Not Prime".
    :return:
    """
    n = int(input())
    cont = 0
    while cont < n:
        x = int(input())
        div = ceil(sqrt(x))
        for i in range(2, div + 1):
            if x == 2:
                print("Prime")
                break
            elif x % 2 == 0:
                print("Not Prime")
                break
            elif x == 3:
                print("Prime")
                break
            elif x % i == 0 and i != div:
                print("Not Prime")
                break
            elif i == div and sqrt(x) != div:
                print("Prime")
                break
            elif i == div and sqrt(x) == div:
                print("Not Prime")
                break
        cont += 1


primo_rapido()
