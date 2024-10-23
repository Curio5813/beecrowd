def pares_de_numeros():
    """
    Temos um vetor de N inteiros distintos e dois inteiros I e F. Precisamos
    computar quantos pares desses inteiros do vetor somam pelo menos I e no
    máximo F. Por exemplo, se o vetor for [45, 12, 11, 7, 83, 29, 5] e I = 19
    e F = 52, temos exatamente 8 pares cuja soma está entre 19 e 52: {5, 29},
    {5, 45}, {7, 12}, {7, 29}, {7, 45}, {11, 12}, {11, 29} e {12, 29}.

    Entrada
    A primeira linha da entrada contém três inteiros N, I e F, indicando respectivamente
    o tamanho do vetor e o valor mínimo da soma e o valor máximo da soma.

    Saída
    Seu programa deve imprimir uma única linha contendo um inteiro indicando quantos pares
    de inteiros no vetor somam pelo menos I e no máximo F.

    Restrições

    • 2 ≤ N ≤ 1000

    • −2000 ≤ I, F ≤ 2000

    • O valor de cada inteiro no vetor está entre −1000 e 1000

    • Os inteiros no vetor são distintos
    :return:
    """
    n, i, f = map(int, input().split(" "))
    vetor = list(map(int, input().split(" ")))
    cont = 0
    for j in range(0, len(vetor)):
        for k in range(0, len(vetor)):
            if j != k and i <= vetor[j] + vetor[k] <= f:
                cont += 1
    print(cont//2)


pares_de_numeros()
