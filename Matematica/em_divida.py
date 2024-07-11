def em_divida():
    """
    Ignácio e Inês realmente gostam de ciência. Eles vivem em Noglônia,
    onde todos sabem que há N museus de ciência. Ignácio e Inês têm N
    sábados livres, então eles concordaram em uma programação para visitar
    um museu de ciência diferente em cada um desses dias.

    Ignácio é muito mesquinho, então todo sábado ele irá dizer a Inês que
    se esqueceu de trazer o dinheiro para pagar a entrada do museu, e pedi-la
    para pagar por ele. Inês sempre faz isso, e por conhecê-lo bem, sabe que
    também que ele nunca irá pagá-la se ela não pedir seu dinheiro de volta.
    Na verdade, Inês sabe que mesmo que ela peça Ignácio seu dinheiro de volta,
    ele só aceitará pagar se a dívida acumulada é um múltiplo de 100, porque senão
    ele vai argumentar que não tem nenhuma dívida a pagar exatamente, e então não
    pagará nada.

    Sendo essa situação, todos os domingos, se a dívida acumulada é um múltiplo de
    100 Inês vai até a casa de Ignácio para reivindicar o seu dinheiro, e porque
    ele não vai ter nenhuma desculpa irá pagar, sem qualquer tipo de desculpa. É
    claro que Ignácio não gosta disso, mas é consolado pela ideia de que, se a dívida
    acumulada depois de visitar os N museus não é um múltiplo de 100, Inês não deve
    cobrar a última parte de seu dinheiro.

    Inês gostaria de saber quantas vezes ela vai ter que ir para a casa de Ignácio
    para pedir seu dinheiro. Para o cálculo, ela pode fornecer uma lista de preços
    dos ingressos para os N museus de ciência em Noglônia, na ordem em que ela e
    Ignácio vão visitá-los.

    Entrada
    Cada caso de teste é descrito usando duas linhas. A primeira linha contém um
    número inteiro N, indicando o número de museus de ciência em Noglônia (1 ≤ N ≤ 100).
    A segunda linha contém N inteiros Pi representando os preços dos ingressos para os
    diferentes museus, na ordem em que eles vão ser visitados (1 ≤ Pi ≤ 100 para i = 1, ..., N).
    O final da entrada é indicado por -1.

    Saída
    Para cada caso de teste, você deve imprimir uma única linha contendo um número inteiro,
    o que representa o número de vezes que Inês vai ter de ir à casa de Ignácio para pedir
    seu dinheiro.
    :return:
    """
    while True:
        n = int(input())
        multiplo, visita = 0, 0
        if n == -1:
            break
        else:
            dividas = list(map(int, input().split(" ")))
            for i in range(0, len(dividas)):
                multiplo += dividas[i]
                if multiplo % 100 == 0:
                    visita += 1
        print(visita)


em_divida()
