def main():
    from decimal import Decimal
    lista = []
    a, b, c = input().split(' ')
    a, b, c = float(Decimal(a)), float(Decimal(b)), float(Decimal(c))
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.sort()
    lista.reverse()
    a = lista[0]
    b = lista[1]
    c = lista[2]
    if a >= b + c:
        print('NAO FORMA TRIANGULO')
    elif a ** 2 == b ** 2 + c ** 2:
        print('TRIANGULO RETANGULO')
        if b == c:
            print('TRIANGULO ISOSCELES')
    elif a ** 2 > b ** 2 + c ** 2:
        print('TRIANGULO OBTUSANGULO')
        if b == c:
            print('TRIANGULO ISOSCELES')
    elif a ** 2 < b ** 2 + c ** 2:
        print('TRIANGULO ACUTANGULO')
        if a != b != c:
            pass
        elif a == b == c:
            print('TRIANGULO EQUILATERO')
        else:
            print('TRIANGULO ISOSCELES')


if __name__ == '__main__':
    main()
