def main():
    x = int(input())
    if x % 2 == 0:
        for k in range(x + 1, x + 1 + (6 * 2), 2):
            print(k)
    elif x % 2 == 1:
        for k in range(x, x + (6 * 2), 2):
            print(k)


if __name__ == '__main__':
    main()
