def main():
    calculo = 0
    for k in range(1, 3):
        a, b, c = input().split(' ')
        a = int(a)
        b = int(b)
        c = round(float(c), 2)
        calculo += b * c
    return f'VALOR A PAGAR: R$ {calculo:.2f}'


if __name__ == '__main__':
    print(main())
