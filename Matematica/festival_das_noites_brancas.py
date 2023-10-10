from sys import setrecursionlimit


setrecursionlimit(1000000000)

def festival_das_noites_brancas():
    """
    Esta função, dado uma sequência de numeros binários, calcula
    o n-ésimo numero de fibonacci, que deve estar inscrito no
    cartão para que a pessoa possa entrar no teatro para assistir
    o festival das noites brancas. A entrada é composta por diversas
    instâncias. A primeira linha da entrada contém um inteiro T indicando
    o número de instâncias. Cada instância consiste em uma linha contendo
    uma descrição de fileira com até 10000 dígitos. A descrição de uma
    fileira é uma sequência de ’1’s e ’0’s, nunca começando com ’0’
    (a primeira cadeira de todas as fileiras estão reservadas). A saída
    para cada instância imprima os 3 dígitos que devem estar escrito no
    cartão para a pessoa entrar no teatro.
    :return:
    """
    t = int(input())
    a, b, p, fibo, ordemm = 0, 1, 1, [], 0
    for i in range(500_000):
        a = b
        b = p
        p = a + b
        fibo.append(a)
    for i in range(t):
        binario = input()
        ordem = int(binario, 2)
        num = fibo[ordem - 1]
        num = str(num)
        if len(num) == 1:
            print(f"00{num}")
        elif len(num) == 2:
            print(f"0{num}")
        elif len(num) == 3:
            print(num)
        elif len(num) > 3:
            num = num[::-1]
            num = num[0:3]
            num = num[::-1]
            print(num)


festival_das_noites_brancas()
