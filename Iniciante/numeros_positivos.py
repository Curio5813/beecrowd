def main():
    cont = 0
    for k in range(1, 7):
        num = float(input())
        if num > 0:
            cont += 1
    print(f'{cont} valores positivos')


if __name__ == '__main__':
    main()
