from math import ceil, floor


def dividindo_os_trabalhos():
    """
    A função printa o valor ótimo de trabalhos que deve ser
    feitos pelos dois estudantes, cabendo um número igual ou
    bem próximo a que os estudantes devem fazer
    :return:
    """
    while True:
        try:
            trabalhos, rangel, gugu, k = [], 0, 0, -1
            n = int(input())
            trabalhos = list(map(int, input().split(" ")))
            # print(len(trabalhos))
            soma = sum(trabalhos)
            # print(soma)
            media = floor(soma / 2)
            # print(media, end=" ")
            for i in range(0, len(trabalhos)):
                rangel += trabalhos[i]
                if rangel >= media:
                    gugu = sum(trabalhos[i + 1::])
                    # print(rangel, end=" ")
                    # print(gugu, end=" ")
                    print(ceil(abs(rangel - gugu)))
                    break
        except EOFError:
            break


dividindo_os_trabalhos()
