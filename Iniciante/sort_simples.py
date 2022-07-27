def main():
    lista01, lista02 = [], []
    a, b, c = input().split(' ')
    a, b, c = int(a), int(b), int(c)
    lista01.append(a)
    lista01.append(b)
    lista01.append(c)
    lista02 = lista01.copy()
    lista02.sort()
    for k in range(0, len(lista02)):
        print(lista02[k])
    print('')
    for k in range(0, len(lista01)):
        print(lista01[k])


if __name__ == '__main__':
    main()
