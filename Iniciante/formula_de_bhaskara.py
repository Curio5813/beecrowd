def main():
    from decimal import Decimal
    a, b, c = input().split(' ')
    a, b, c = float(Decimal(a)), float(Decimal(b)), float(Decimal(c))
    delta = b ** 2 - (4 * a * c)
    if delta > 0 and a != 0:
        r1 = (-b + delta ** (1/2)) / (2 * a)
        r2 = (-b - delta ** (1/2)) / (2 * a)
        print(f'R1 = {r1:.5f}\n'
              f'R2 = {r2:.5f}')
    elif delta == 0 and a != 0:
        r1 = -b / (2 * a)
        r2 = r1
        print(f'R1 = {r1:.5f}\n'
              f'R2 = {r2:.5f}')
    elif delta < 0 or a == 0:
        print('Impossivel calcular')


if __name__ == '__main__':
    main()
