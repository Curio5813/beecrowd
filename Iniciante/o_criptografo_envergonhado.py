from math import floor, sqrt


def o_criptografo_envegonhado():
    """
    Está função calcula o menor fator primo entre o produto
    de dois números primos e printa o resultado. A entrada
    consiste em não mais do que 20 casos de teste. Cada caso
    de teste é uma linha com os inteiros 4 ≤ K ≤ 10 100 e
    2 ≤ L ≤ 10 6 . K é a própria chave, um produto de dois
    primos. L é o tamanho mínimo desejado dos fatores na chave.
    O conjunto de entrada é encerrado por um caso em que K = 0 e
    L = 0. Para cada número K , se um de seus fatores for
    estritamente menor do que o L exigido, seu programa deve
    produzir "BAD p " , onde p é o menor fator em K . Caso contrário,
    a saída deve ser "GOOD". Os casos devem ser separados por uma
    quebra de linha.
    :return:
    """
    while True:
        k, lp = map(int, input().split(" "))
        if k == 0 and lp == 0:
            break
        for i in range(2, 1000000 + 1):
            if k % i == 0 and i >= lp:
                print("GOOD")
                break
            elif k % i == 0 and i < lp:
                print(f"BAD {i}")
                break


o_criptografo_envegonhado()
