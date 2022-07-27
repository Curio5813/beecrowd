def main():
    """
    Dentro de uma quanditdade de teste N < 10000, é lido um valor X pelo usário que deve retornar
    a quantidade de valores X dentro do intervalo [10,20] e quanto estão fora dele.
    """
    cont1, cont2 = 0, 0
    n = int(input())
    while n >= 10000:
        n = int(input())
    for k in range(0, n):
        x = int(input())
        while -(10 ** 7) > x or x > 10 ** 7:
            x = int(input())
        if 10 <= x <= 20:
            cont1 += 1
        elif x < 10 or x > 10:
            cont2 += 1
    return f'{cont1} in\n' \
           f'{cont2} out'


if __name__ == '__main__':
    main()
