def main():
    from math import sqrt
    x1, y1 = input().split(' ')
    x2, y2 = input().split(' ')
    x1 = round(float(x1), 1)
    y1 = round(float(y1), 1)
    x2 = round(float(x2), 1)
    y2 = round(float(y2), 1)

    distacia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f'{distacia:.4f}')


if __name__ == '__main__':
    main()
