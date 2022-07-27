def main():
    i, j, n = 1, 7, 0
    while i <= 9:
        while n % 3 != 0 or n == 0:
            print(f'I={i} J={j}')
            n += 1
            j -= 1
        i += 2
        j += 5
        n = 0


if __name__ == '__main__':
    main()
