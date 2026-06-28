def sequencias_de_granizo():
    """
    Considere a sequência formada iniciando-se por um inteiro positivo
    h0 e iterando com n = 1, 2, . . . com a seguinte definição, até que hn = 1:

    hn = { ½ × hn-1 se hn-1 é par;

    hn = { 3 × hn-1 + 1 se hn-1 é ímpar.

    Por exemplo, se iniciarmos com h0 = 5 a seguinte sequência é gerada: 5, 16, 8, 4,
    2, 1. Se começarmos com h0 = 11, a sequência gerada é 11, 34, 17, 52, 26, 13, 40,
    20, 10, 5, 16, 8, 4, 2, 1.

    Como você pode ver nos exemplos, os números aumentam e diminuem, mas eventualmente
    terminam em 1 (isto é verdade para pelo menos para todos os números que já foram testados).
    Estas sequências são chamadas de Sequências de Granizo porque são similares à formação
    do granizo, pois são carregados para cima pelos ventos várias vezes, até que finalmente
    caem no chão.

    Neste problema, dado um inteiro positivo, sua tarefa é computar o maior número na Sequência
    de Granizo que inicie com este o número dado.

    Entrada
    Cada caso de teste é descrito por uma única linha. A linha contém um inteiro H que
    representa o valor inicial para construir a sequência (1 ≤ H ≤ 500).

    O último caso de teste é composto por uma linha contendo um único zero.

    Saída
    Para cada caso de teste, imprima uma linha com um inteiro representando o maior número
    na Sequência de Granizo que inicia com o número da entrada.
    :return:
    """
    h = int(input())
    while h != 0:
        numeros = [h]
        while h != 1:
            if h % 2 == 1:
                h = 3 * h + 1
                numeros.append(h)
            elif h % 2 == 0:
                h = h // 2
                numeros.append(h)
        print(max(numeros))
        h = int(input())


sequencias_de_granizo()
