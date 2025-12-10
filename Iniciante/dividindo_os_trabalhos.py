def dividindo_os_trabalhos():
    """
    A função printa o valor ótimo de trabalhos que deve ser
    feitos pelos dois estudantes, cabendo um número igual ou
    bem próximo a que os estudantes devem fazer
    :return:
    """
    while True:
        try:
            diferenca = []
            n = int(input())
            trabalhos = list(map(int, input().split()))
            for i in range(0, len(trabalhos)):
                rangel = sum(trabalhos[0:i + 1])
                gugu = sum(trabalhos[i + 1:])
                # print(rangel, gugu)
                diff = abs(rangel - gugu)
                if diff == 0:
                    diferenca.append(diff)
                    break
            print(min(diferenca))
        except EOFError:
            break


dividindo_os_trabalhos()


"""
3
2 3 5
4
1 2 2 6
"""