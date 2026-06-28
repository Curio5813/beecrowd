def acoes():
    """
    Ada é uma investidora de um negócio bastante instável e de alto risco:
    ações da NlogNintendo.No entanto, por ter enorme simpatia pela empresa
    belo-horizontina, Ada continua investindo mesmo assim.

    Porém, a instabilidade às vezes dificulta que ela faça seu planejamento de
    portfólio a longo prazo.Para ajudá-la, ela contratou você para fazer um
    programa que prevê o valor das ações da NlogNintendo.Ada registrou que,
    no dia D, uma ação da NlogNintendo valia I reais. Além disso, logo no início
    dos dias pares, o preço da ação sobe X reais em relação ao preço do final do
    dia anterior.Nos dias ímpares, o preço da ação já se inicia com um valor X
    reais abaixo do valor no fim do dia anterior.E agora? Será que você consegue
    ajudá-la a saber qual será o preço da ação daqui a F dias?

    Entrada
    A entrada é composta de uma linha contendo 4 inteiros separados por espaço: D
    (1 ≤ D ≤ 365) (o dia em que Ada registrou o preço da ação da NlogNintendo),
    I(X ≤ I ≤ 1000) (o preço inicial registrado da ação), X (1 ≤ X ≤ I) (a variação
    diária do preço da ação) e F (1 ≤ F ≤ 365) (o número de dias no futuro em que
    seu programa deve prever o preço da ação).

    Saída
    A saída deve conter uma linha com um único inteiro: o preço previsto da ação F
    dias após o dia em que o preço inicial foi registrado.
    :return:
    """
    d, i, x, f = map(int, input().split(" "))
    if d % 2 == 1:
        for j in range(f):
            if j % 2 == 0:
                i += x
            if j % 2 == 1:
                i -= x
    elif d % 2 == 0:
        for j in range(f):
            if j % 2 == 0:
                i -= x
            if j % 2 == 1:
                i += x
    print(i)


acoes()
