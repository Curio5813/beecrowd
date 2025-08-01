def distribuindo_pequis():
    """
    Um fazendeiro muito meticuloso resolveu distribuir pequis (pequi é uma
    fruta nativa do cerrado brasileiro) aos seus trabalhadores. Ele possui N
    trabalhadores e uma lista S com N valores inteiros. Ele pretende distribuir
    os pequis em etapas.

    Inicialmente nenhum trabalhador possui pequis. Na primeira etapa o fazendeiro
    distribui S1 pequis ao primeiro trabalhador, S2 pequis ao segundo e assim por
    diante até distribuir SN pequis ao N-ésimo trabalhador. Em cada uma das próximas
    etapas o fazendeiro retira o valor que está no final de S, insere este no início
    de S e então distribui novamente assim como foi feito na primeira etapa. O exemplo
    abaixo representa uma distribuição de pequis em três etapas, para N = 4 e
    S = {3, 0, 1, 0}, na qual a coluna Trabalhadores contém a quantidade de pequis que
    cada trabalhador possuirá após a execução de cada etapa.



    Como o número de funcionários e de etapas é muito grande, o fazendeiro pediu a sua ajuda
    para escrever um programa que imprime a quantidade final de pequis que cada trabalhador
    terá após a execução da última etapa.

    Entrada
    A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 10^3) seguido por um inteiro K
    (1 ≤ K ≤ 10^6), que são o número de trabalhadores a quantidade de etapas, respectivamente.
    A próxima linha contém os valores S1, S2, … , SN, onde 0 ≤ Si ≤ 103 para 1 ≤ i ≤ N.

    Saída
    A saída consiste em apenas uma linha que contém a quantidade de pequis que cada um dos N
    trabalhadores terá ao final da K-ésima etapa, ambos separados por um espaço em branco.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, s = entrada[0], entrada[1]
    trabalhadores = []
    for i in range(n):
        trabalhadores.append(0)
    pequis = list(map(int, input().strip().split(" ")))
    for i in range(s):
        for j in range(0, len(trabalhadores)):
            trabalhadores[j] += pequis[j]
        pequis = pequis[-1:] + pequis[0:-1]
    print(*trabalhadores)


distribuindo_pequis()
