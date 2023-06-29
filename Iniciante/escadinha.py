def escadinha():
    """
    Está função calcula o número de quantidades de números que fazem
    uma escadinha, ou seja, tenha a mesma diferença entre numeros
    consecutivos. Mesmo que não façam a escadinha terá sempre uma
    única escadinha que é ele próprio.
    :return:
    """
    cont1, cont2 = 1, 1
    n = int(input())
    nx = list(map(int, input().split(" ")))
    if len(nx) >= 3:
        for i in range(0, len(nx)):
            if i == len(nx) - 2:
                if cont1 > 1:
                    cont2 += 1
                break
            if nx[i] - abs(nx[i + 1]) == nx[i + 1] - abs(nx[i + 2]):
                cont1 += 1
            elif nx[i] - abs(nx[i + 1]) != nx[i + 1] - abs(nx[i + 2]):
                if cont1 > 1:
                    cont2 += 1
                cont1 = 1
    print(cont2)


escadinha()
