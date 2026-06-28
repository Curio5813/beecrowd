def xenlonguinho():
    """
    Kogu está buscando as esferas do dragão para invocar Xenlonguinho
    e pedir para ele reviver seu amigo Kuriri, que infelizmente morreu
    na última batalha dos guerreiros Zê.

    Porém Kogu está tendo muita dificuldade para encontrar as esferas,
    por isso Xenlonguinho que é seu conhecido há muito tempo, decidiu
    abrir uma exceção e aceitou ser invocado caso Kogu encontre todas
    as esferas cujo o número de divisores da quantidade de estrelas da
    esfera sejam par.

    Por exemplo se existem sete esferas, Kogu não precisaria encontrar as
    esferas de uma e quatro estrelas, pois elas tem uma quantidade ímpar
    de divisores, então ele só precisa pegar 5 esferas para invocar Xenlonguinho.

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_2596.png)

    Como Kogu não é muito bom em contas, ele pediu para você escrever um
    programa que dado o total de esferas existentes, mostre a quantidade
    mínima de esferas que ele precisa procurar.

    Entrada
    A primeira linha consiste de um inteiro C que representa a quantidade de
    casos de teste. As linhas subsequentes contém um inteiro N (2 ≤ N ≤ 1000)
    que representa a quantidade de esferas necessárias para invocar Xenlonguinho.

    Saída
    Seu programa deve exibir a quantidade mínima de esferas que Kogu tem que
    procurar.
    :return:
    """
    c = int(input())
    for i in range(c):
        n = int(input())
        esferas = 0
        for j in range(1, n + 1):
            divisores = 0
            for k in range(1, n + 1):
                if j % k == 0:
                    divisores += 1
            if divisores % 2 == 0:
                esferas += 1
        print(esferas)


xenlonguinho()
