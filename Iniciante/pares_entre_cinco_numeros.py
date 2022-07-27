def main():
    pares = []
    for k in range(0, 5):
        num = int(input())
        if num % 2 == 0:
            pares.append(num)
    print(f'{len(pares)} valores pares')


if __name__ == '__main__':
    main()
