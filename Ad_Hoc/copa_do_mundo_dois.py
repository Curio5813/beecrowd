def copa_do_mundo_dois():
    """
    A Nlogônia é atualmente um dos países com maior crescimento econômico
    no mundo, e seus governantes têm se esforçado para que o país seja mais
    conhecido e respeitado internacionalmente. Recentemente a Nlogônia foi
    escolhida para ser a sede da Copa do Mundo de Futebol Amador, e está se
    preparando para receber os milhares de torcedores que o evento atrai.

    Como parte da preparação para a Copa, o governo planeja realizar uma reforma
    em todo o sistema de transporte intermunicipal, que é hoje composto de uma
    malha de rodovias e ferrovias, cada rodovia ou ferrovia interligando um par
    de cidades. Com as rodovias e ferrovias existentes já é possível viajar entre
    qualquer par de cidades (possivelmente passando por outras cidades no caminho),
    mas o governo quer oferecer melhores condições de transporte para os visitantes
    e a população.

    Como não há recursos para reformar todas as rodovias e ferrovias, o governo quer
    escolher um conjunto de rodovias e ferrovias para ser reformado, e já realizou um
    estudo para estabelecer o custo de reforma de cada rodovia e ferrovia. A escolha
    deve obedecer aos seguintes critérios:

    ao final da reforma, deve ser possível viajar entre qualquer par de cidades (possivelmente
    passando por outras cidades) utilizando apenas rodovias ou ferrovias reformadas;
    para priorizar o transporte público, dentre as escolhas que satisfazem a restrição 1,
    deve-se escolher uma que minimize o número de rodovias reformadas;
    dentre as escolhas que satisfazem as restrições 1 e 2, deve-se escolher uma que minimize
    o custo total.
    Você foi contratado para escrever um programa que, conhecidos os custos de reforma de cada
    rodovia e ferrovia, determine o menor custo possível para a reforma, obedecidos os
    critérios estabelecidos.

    Entrada
    A primeira linha da entrada contém três inteiros N (2 ≤ N ≤ 100), F (1 ≤ F ≤ N(N − 1)/2)
    e R (1 ≤ R ≤ N(N − 1)/2), indicando respectivamente o número de cidades, de ferrovias e de
    rodovias. As cidades são identificadas por inteiros de 1 a N. Cada uma das F linhas seguintes descreve uma ferrovia e contém três inteiros A, B (1 ≤ A < B ≤ N) e C (1 ≤ C ≤ 1000), onde A e B representam cidades e C representa o custo da reforma da ferrovia que interliga A e B. Cada uma das R linhas seguintes descreve uma rodovia e contém três inteiros I, J e K, onde I e J (1 ≤ I < J ≤ N) representam cidades e K (1 ≤ K ≤ 1000) representa o custo da reforma da rodovia que interliga I e J.

    Saída
    Seu programa deve produzir uma única linha, contendo o menor custo possível para o conjunto
    de reformas de ferrovias e rodovias, obedecendo aos critérios estabelecidos.
    :return:
    """
    entrada = input().strip().split(" ")
    n, f, r = int(entrada[0]), int(entrada[1]), int(entrada[2])
    trechos, estradas, cidade, cidades, orcamento, x, orcamentos, ordem_trechos = (
        [], [], [], [], [], 1, 0, [])
    for i in range(1, n):
        trechos.append(i)
    for i in range(f + r):
        estrada = list(map(int, input().strip().split(" ")))
        estradas.append(estrada)
    for i in range(0, len(estradas)):
        for j in range(0, len(estradas[i])):
            cidade.append(estradas[i][0])
            cidade.append(estradas[i][1])
            cidades.append(cidade)
            orcamento.append(estradas[i][2])
            cidade = []
            break
    k = 0
    while ordem_trechos != trechos:
        menor = 0
        if cidades[k][0] == x and cidades[k][1] == x + 1:
            for i in range(0, len(estradas)):
                if estradas[i][0:2] == cidades[k][0:2]:
                    menor = orcamento[i]
                    if orcamento[i] < menor:
                        menor = orcamento[i]
            ordem_trechos.append(cidades[k][0])
            # print(cidades[k][0], cidades[k][1], orcamento[k])
            # print(ordem_trechos)
            orcamentos += menor
            x += 1
        else:
            k += 1
            if k > len(cidades) - 1:
                k = 0

    # print(cidades)
    # print(ordem_trechos)
    # print(orcamento)
    print(orcamentos)


copa_do_mundo_dois()

"""
3 3 2
1 2 1000
1 3 1000
2 3 900
1 3 800
2 3 700

5 4 5
3 4 300
1 2 100
2 4 300
1 3 250
4 5 600
3 4 200
2 3 100
2 5 400
1 5 450

5 2 3
4 5 60
2 3 60
1 2 50
1 4 50
3 4 50

5 4 5
3 4 300
1 2 100
2 4 300
1 3 250
4 5 600
3 4 200
2 3 100
2 5 440
1 5 450
"""