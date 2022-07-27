def main():
    a, b = input().split(' ')
    a, b = int(a), int(b)
    if a >= b and a % b == 0 or b >= a and b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


if __name__ == '__main__':
    main()
