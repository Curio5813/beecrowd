def main():
    n = int(input())
    for i in range(0, n):
        x = int(input())
        if x == 2:
            print('Prime')
        elif x != 2 and x % 2 == 0:
            print('Not Prime')
        elif x == 3:
            print('Prime')
        elif x % 2 != 0 and x > 3:
            for k in range(3, x + 1):
                if k == x:
                    print('Prime')
                elif x % k == 0:
                    print('Not Prime')
                    break


if __name__ == '__main__':
    main()
