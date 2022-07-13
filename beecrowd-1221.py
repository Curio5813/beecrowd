def primo_rapido():
    """
    Esta função retorna uma verificação dizendo se um dado número é primo ou não.
    :return:
    """
    r = 2 ** 31
    cont = 0
    n = int(input())
    while cont < n:
        x = int(input())
        for i in range(2, r + 1):
            if x % i == 0 and i == x:
                print('Prime')
                break
            elif x % i == 0 and i != x:
                print('Not Prime')
                break
        cont += 1


primo_rapido()
