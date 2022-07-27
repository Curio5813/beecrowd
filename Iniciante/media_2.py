def main():
    a = round(float(input()), 1)
    while a < 0 or a > 10:
        a = round(float(input()), 1)
    b = round(float(input()), 1)
    while b < 0 or b > 10:
        b = round(float(input()), 1)
    c = round(float(input()), 1)
    while c < 0 or b > 10:
        b = round(float(input()), 1)
    media = (a * 2 + b * 3 + c * 5) / 10
    print(f'MEDIA = {media:.1f}')


if __name__ == '__main__':
    main()
