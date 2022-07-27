def main():
    a = round(float(input()), 1)
    while a < 0 or a > 10:
        a = round(float(input()), 1)
    b = round(float(input()), 1)
    while b < 0 or b > 10:
        b = round(float(input()), 1)
    media = (a * 3.5 + b * 7.5) / 11
    print(f'MEDIA = {media:.5f}')


if __name__ == '__main__':
    main()
