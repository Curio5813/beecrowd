def main():
    i, j, n = 0, 1, 0
    while i <= 2:
        while n % 3 != 0 or n == 0:
            if int(i) == i and int(j) == j:
                print(f'I={int(i)} J={int(j)}')
            elif int(i) == i and int(j) != j:
                print(f'I={int(i)} J={j:.1f}')
            elif int(i) != i and int(j) == j:
                print(f'I={i:.1f} J={int(j)}')
            elif int(i) != i and int(j) != j:
                print(f'I={i:.1f} J={j:.1f}')
            n += 1
            j += 1
        i += 0.2
        i = round(i, 1)
        j = 1 + i
        n = 0


if __name__ == '__main__':
    main()
