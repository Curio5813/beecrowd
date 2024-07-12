def o_temivel_evil_son():
    """
    Em um lugar muito distante existe um reino pacífico chamado Lá-Ara.
    Seu governante, o rei Naldo, mestre pokemon experiente, está em apuros.
    Um raro pokemon matemático chamado Evil-Son invadiu o seu território e
    ameaçou destruir todo o reino caso ninguém resolvesse o desafio descrito a
    seguir.

    Um conjunto de retas no plano está em posição geral se não existe duas retas paralelas
    e também não existe três retas que se interceptam em um mesmo ponto. A seguir, temos
    na figura (A) um conjunto de retas em posição geral, já o conjunto de retas na figura (B)
    não está em posição geral.

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_2218.png)

    O desafio consiste em computar o número de regiões no plano formadas por um conjunto de
    N retas em posição geral. O rei Naldo conta com a sua habilidade, em matemática e programação,
    para salvar o reino de Lá-Ara do temível Evil-Son.

    Entrada
    A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro
    T indicando o número de instâncias. Cada instância é composta de uma única linha que contém o
    número N representando o número de retas no conjunto.

    Saída
    Para cada instância na entrada, imprima uma única linha contendo o número de regiões formadas
    no plano pelas retas do conjunto.
    :return:
    """
    t = int(input())
    for i in range(t):
        regioes = 1
        retas = int(input())
        for j in range(1, retas + 1):
            regioes += j
        print(regioes)


o_temivel_evil_son()
