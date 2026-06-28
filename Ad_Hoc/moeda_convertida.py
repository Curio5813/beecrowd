def moeda_convertida():
    """
    Charlinho vivia na Nlogônia e tinha o sonho de poder ir ao maior
    parque de diversões de lá: o Nopi Nari. Um dia, depois de economizar
    muito, ele conseguiu ir ao parque. Chegando lá, descobriu que dentro
    do parque não se utilizava a moeda do país, mas uma moeda específica
    do local. Ele também descobriu que, caso sobrasse alguma quantia no
    fim do dia, ele não poderia trocar de volta os valores. Dessa forma,
    ele deseja comprar somente o necessário para que ele possa se divertir,
    e não sobrar nenhum valor. Por isso, ele pediu a tua ajuda. Dado o valor
    corrente da moeda do parque, e a quantidade que ele pretende comprar,
    informe o total do valor que Charlinho irá pagar.

    Entrada
    A entrada consiste em vários casos de teste. Cada caso contém um valor real M,
    representando a cotação da moeda do parque naquele dia; e um número inteiro N,
    representando a quantidade dessa moeda que Charlinho pretende adquirir.

    Saída
    Imprima o valor total que Charlinho irá pagar.
    :return:
    """
    m = float(input())
    n = int(input())
    print(f"{(n * m):.2f}")


moeda_convertida()
