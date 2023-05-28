def dividindo_os_trabalhos():
    """
    A função printa o valor ótimo de trabalhos que deve ser
    feitos pelos dois estudantes, cabendo um número igual ou
    bem próximo a que os estudantes devem fazer
    :return:
    """
    while True:
        try:
            i, soma = 0, 0
            n = int(input())
            x = list(map(int, input().split()))
            x = x[0:n]
            e = x[::-1]
            while soma < x[-1] and i < len(x) - 1:
                soma += x[i]
                i += 1
            print(abs(x[-1] - soma))
        except EOFError:
            break


dividindo_os_trabalhos()
