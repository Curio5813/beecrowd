def nove():
    """
    Paulo Bruno é um menino que adora Pokemons, porém odeia matemática, ele
    detesta exponenciação e por algum motivo não calcula corretamente operações
    que envolvam o número 9. Sabendo disso, seu amigo Werlesson decidiu fazer
    um desafio, ele quer que Paulo Bruno calcule a N-ésima potência de 9 e diga
    o último dígito dessa potência. Por exemplo, sendo N=2, o resultado seria 1,
    pois 9^2=81. O problema é que, dependendo do valor de N, o resultado da exponenciação
    pode ser um número muito grande. Sem ideias, Paulo Bruno decidiu pedir sua ajuda.

    Entrada
    A entrada é composta por diversas instâncias. A primeira linha da entrada contém um
    inteiro T indicando o número de instâncias. Cada instância é composta por apenas uma
    linha, que contêm o número inteiro N(0 ≤ N ≤ 10^9).

    Saída
    Para cada instância na entrada, imprima uma linha contendo um inteiro, o último dígito de 9^N.
    :return:
    """
    t = int(input())
    for i in range(t):
        n = int(input())
        if n % 2 == 0:
            print(1)
        else:
            print(9)


nove()
