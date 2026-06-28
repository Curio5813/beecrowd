from math import gcd


def tda_racional():
    """
    Esta função calcula a fração reduzida entre duas frações
    que são ou adionada, ou subtraída, ou multiplicada, ou
    dividida entre elas.
    """
    cont = 0
    n = int(input())
    while cont < n:
        str_in = input().split()
        x1 = int(str_in[0])
        x2 = int(str_in[2])
        y1 = int(str_in[4])
        y2 = int(str_in[6])
        s = str_in[3]
        if s == "+":
            n1 = x1 * y2 + x2 * y1
            d1 = x2 * y2
            div = gcd(n1, d1)
            n2 = int(n1 / div)
            d2 = int(d1 / div)
            print(f"{n1}/{d1} = {n2}/{d2}")
        elif s == "-":
            n1 = x1 * y2 - x2 * y1
            d1 = x2 * y2
            div = gcd(n1, d1)
            n2 = int(n1 / div)
            d2 = int(d1 / div)
            print(f"{n1}/{d1} = {n2}/{d2}")
        elif s == "*":
            n1 = x1 * y1
            d1 = x2 * y2
            div = gcd(n1, d1)
            n2 = int(n1 / div)
            d2 = int(d1 / div)
            print(f"{n1}/{d1} = {n2}/{d2}")
        elif s == "/":
            n1 = x1 * y2
            d1 = x2 * y1
            div = gcd(n1, d1)
            n2 = int(n1 / div)
            d2 = int(d1 / div)
            print(f"{n1}/{d1} = {n2}/{d2}")
        cont += 1


tda_racional()
