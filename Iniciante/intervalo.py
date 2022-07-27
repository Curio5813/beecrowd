def main():
    x = float(input())
    if 0 <= x <= 25.0000:
        print('Intervalo [0,25]')
    elif 25.0000 < x <= 50.0000:
        print('Intervalo (25,50]')
    elif 50.0000 < x <= 75.0000:
        print('Intervalo (50,75]')
    elif 75.0000 < x <= 100.0000:
        print('Intervalo (75,100]')
    elif x < 0 or x > 100.0000:
        print('Fora de intervalo')


if __name__ == '__main__':
    main()
