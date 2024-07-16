from math import factorial


def nem_tudo_e_greve_versao_hard():
    """
    :return:
    """
    n = int(input())
    m = n
    soma, cont = 0, 0
    k = n
    for i in range(n, 0, -1):
        if i == n:
            permutacao = int(factorial(i) / factorial(k))
            soma += permutacao
            print(i, k, permutacao, soma)
        else:
            k = i - 1
            a = k
            if i == 2 and k == 1:
                permutacao = int(factorial(i) / factorial(k))
                soma += permutacao
                print(i, k, permutacao, soma)
                break
            else:
                while a <= m:
                    permutacao = int(factorial(i) / factorial(k))
                    soma += permutacao
                    print(i, k, permutacao, soma)
                    a += a

    print(soma)
    p = 10 ** 9 + 7
    print(p)
    resultado = soma % p
    print(resultado)


nem_tudo_e_greve_versao_hard()
