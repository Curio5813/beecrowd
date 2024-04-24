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
            for i in range(n):
                trabalhos.append(int(input()))
            print(len(trabalhos))
            soma = sum(trabalhos)
            print(soma)
            media = soma / 2
            print(media, end=" ")
            for i in range(0, len(trabalhos)):
                rangel += trabalhos[i]
                if rangel > media:
                    rangel -= trabalhos[i]
                    print(rangel, end=" ")
                    print(ceil(abs(rangel - media)))
                    break
        except EOFError:
            break


dividindo_os_trabalhos()
