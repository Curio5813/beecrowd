def main():
    x = int(input())
    impares = [k for k in range(1, x + 1) if k % 2 == 1]
    for k in range(0, len(impares)):
        print(impares[k])


if __name__ == '__main__':
    main()
