def escadinha():
    """
    Está função calcula o número de quantidades de números que fazem
    uma escadinha, ou seja, tenha a mesma diferença entre numeros
    consecutivos. Mesmo que não façam a escadinha terá sempre uma
    única escadinha que é ele próprio.
    :return:
    """
    n = int(input())
    numeros = list(map(int, input().split(" ")))
    escadinhas, diff, i = 0, [], 1
    while i <= len(numeros) - 1:
        for j in range(i, len(numeros)):
            diferenca = numeros[j] - numeros[j - 1]
            if len(diff) > 0 and diferenca == diff[-1]:
                diff.append(diferenca)
                i += 1
                continue
            else:
                diff.append(diferenca)
                escadinhas += 1
                i += 1
                break
    if len(diff) == 0:
        print(1)
    else:
        print(escadinhas)


if __name__ == '__main__':
    escadinha()
