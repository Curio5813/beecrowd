def main():

    a, b, c = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)

    maior_ab = (a + b + abs(a - b)) / 2
    maior_ac = (a + c + abs(a - c)) / 2
    maior_bc = (b + c + abs(b - c)) / 2
    if maior_ab == a and maior_ac == a:
        return f'{a} eh o maior'
    elif maior_ab == b and maior_bc == b:
        return f'{b} eh o maior'
    elif maior_ac == c and maior_bc == c:
        return f'{c} eh o maior'


if __name__ == '__main__':
    print(main())
