def consecutivos():
    """
    Num sorteio que distribui prêmios, um participante inicialmente
    sorteia um inteiro N e depois N valores. O número de pontos do
    participante é o tamanho da maior sequência de valores consecutivos
    iguais. Por exemplo, suponhamos que um participante sorteia N = 11 e,
    nesta ordem, os valores

    30, 30, 30, 30, 40, 40, 40, 40, 40, 30, 30

    Então, o participante ganha 5 pontos, correspondentes aos 5 valores
    40 consecutivos. Note que o participante sorteou 6 valores iguais a 30,
    mas nem todos são consecutivos.

    Sua tarefa é ajudar a organização do evento, escrevendo um programa que
    determina o número de pontos de um participante.

    Entrada
    A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 104), o número
    de valores sorteados. A segunda linha contém N valores, V1, V2, . . . ,
    VN , (−231 ≤ VI ≤ 2^31 − 1, para I = 1, 2, . . . , N) na ordem de sorteio,
    separados por um espaço em branco.

    Saída
    Seu programa deve imprimir apenas uma linha, contendo apenas um inteiro,
    indicando o número de pontos do participante.
    :return:
    """
    n = int(input())
    cont, maior = 1, 0
    valores = list(map(int, input().split(" ")))
    for i in range(0, len(valores)):
        if i >= len(valores) - 1:
            if cont > maior:
                maior = cont
            break
        if valores[i] == valores[i + 1]:
            cont += 1
        elif valores[i] != valores[i + 1]:
            if cont > maior:
                maior = cont
            cont = 1
    print(maior)


consecutivos()
