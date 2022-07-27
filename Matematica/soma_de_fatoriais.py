def soma_fatoriais():
    from math import factorial
    while True:
        try:
            m, n = input().upper().split(' ')
        except EOFError:
            break
        else:
            m, n = int(m), int(n)
            print(f'{factorial(m) + factorial(n)}')


soma_fatoriais()
