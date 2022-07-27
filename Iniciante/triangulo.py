def main():
    a, b, c = input().split(' ')
    a, b, c = float(a), float(b), float(c)
    if a + b > c and a + c > b and b + c > a:
        perimetro = a + b + c
        print(f'Perimetro = {perimetro:.1f}')
    else:
        area = ((a + b) * c) / 2
        print(f'Area = {area:.1f}')


if __name__ == '__main__':
    main()
