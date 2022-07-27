def main():
    h, m, seg = 0, 0, 0
    segundos = int(input())
    while segundos >= 3600:
        h += 1
        segundos -= 3600
    while segundos >= 60:
        m += 1
        segundos -= 60
    seg = segundos
    print(f'{h}:{m}:{seg}')


if __name__ == '__main__':
    main()
