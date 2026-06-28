from collections import Counter


def insatisfacao_nas_eleicoes():
    """
    Uma eleição foi feita em uma pequena cidade de M habitantes, onde havia N
    candidatos. As pessoas escreviam o número do candidato em um pedaço de papel,
    e inseriam na urna.

    Ao final da eleição, se um candidato receber uma quantidade estritamente maior
    do que 50% dos votos, ele é considerado o vencedor. Caso contrário um segundo
    turno de eleições é feito.

    Como o processo de contagem manual é muito lento, você deve desenvolver um programa
    que decide qual o candidato vencedor ou se nenhum recebeu votos suficientes e um
    segundo turno será necessário.

    Entrada
    Na primeira linha você terá um inteiro T (T ≤ 100) indicando o número de casos de teste.

    Para cada caso de teste, na primeira linha você terá os números inteiros N (1 ≤ N ≤ 10) e
    M (1 ≤ M ≤ 103* ou 1 ≤ M ≤ 5*104**). Na próxima linha, M inteiros seguirão separados por
    espaços, indicando o candidato em que cada pessoa votou, ou seja, o número escrito em cada
    pedaço de papel dentro da urna.

    *Ocorre em aproximadamente 90% dos casos de teste;

    **Ocorre nos demais casos de teste.

    Saída
    Para cada caso, imprima o número do candidato vencedor, ou -1 caso haverá segundo turno.
    :return:
    """
    t = int(input().strip())
    for i in range(t):
        entrada = list(map(int, input().strip().split(" ")))
        n, m = int(entrada[0]), int(entrada[1])
        votacao = list(map(int, input().strip().split(" ")))
        votacao_ordenada = Counter(votacao)
        cadidato_mais_votado, votos_recebidos = max(votacao_ordenada.items(), key=lambda item: item[1])
        percentual = (votos_recebidos / len(votacao)) * 100
        if percentual > 50.0000000000000000:
            print(cadidato_mais_votado)
        else:
            print(-1)


insatisfacao_nas_eleicoes()
