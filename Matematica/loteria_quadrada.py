from math import factorial


def loteria_quadrada():
    """
    O Governo da República Unida de Little Tower está desenvolvendo um
    novo tipo de loteria. O principal objetivo da loteria é arrecadar
    dinheiro para a construção do Estádio Olímpico Little Tower, para
    atender a 400.000 pessoas. A proposta do estádio é uma estratégia
    de Little Tower para sediar a Copa do Mundo em 2078. O sorteio será
    executado semanalmente. Cada semana, os bilhetes, sob a forma de cartões
    quadrados serão vendidos. Cada bilhete terá quadrados com números
    impressos no interior, de uma sequência de N linhas e N colunas, conforme
    mostrado na Figura 1.

    [imagem](https://resources.beecrowd.com/gallery/images/novos/Square%20Lottery.png)
                    Fig 1: Um exemplo de bilhete para N = 3.

    Em cada bilhete nenhum número aparece duas vezes e, portanto, todos os números de
    1 a N2 estarão presentes (em ordem aleatória de posições). Não haverá duas passagens
    iguais vendidas na mesma semana. No entanto, todos os possíveis diferentes bilhetes
    serão vendidos, uma vez que os cidadãos de Little Tower amam loterias. Os ingressos
    serão vendidos por T$ 1,00 (um Torreal, Unidade monetária de Little Tower). Para
    escolher o(s) vencedor(es), quatro números (entre 1 e N2) serão escolhidos
    aleatoriamente e o(s) bilhete(s) cujos números escolhidos sejam vértices de um quadrado,
    será concedido o prêmio em dinheiro. Por exemplo, o bilhete mostrado na Figura 1 é um
    bilhete premiado, se os números colhidos são (6, 3, 2, 9), (1, 4, 2, 5) ou (7, 8, 9, 6),
    mas não é um bilhete premiado, se os números colhidos forem (1, 7, 2, 9). Se mais de
    um bilhete for vencedor, os clientes que compraram os bilhetes vão compartilhar o prêmio
    da semana. O governo de Little Tower pede sua ajuda para determinar o valor do prêmio
    a ser pago para cada bilhete vencedor para um dado N, e uma determinada percentagem,
    sobre o montante total recebido pelos ingressos, que o governo quer pagar como prêmios.

    Entrada
    A entrada conterá vários casos de teste. Cada teste é descrito em uma linha que contém
    dois números, um inteiro N e um valor de ponto flutuante (real) P, representando,
    respectivamente, o número de linhas (e colunas) dos bilhetes, bem como a percentagem
    do dinheiro recebido que será pago como prêmio (2 ≤ N ≤ 100 e 0 ≤ P ≤ 100.0). O final
    da entrada é indicado por N = P = 0.

    Saída
    Para cada caso de teste seu programa deve produzir uma linha de saída, contendo um valor
    real representando o prêmio a ser pago para cada bilhete premiado. O valor do prêmio
    deverá ser impresso com 2 dígitos de precisão, e o último dígito decimal deve ser
    arredondado. A entrada não irá conter os casos de teste onde diferenças de arredondamento
    são significativas.
    :return:
    """
    while True:
        entrada = list(input().split())
        n, p = int(entrada[0]), float(entrada[1])
        if n == p == 0:
            break
        talao = n ** 2
        combinacao = factorial(talao)/(factorial(talao - 4) * factorial(4))
        if talao == 4:
            print(f'{(p/100):.2f}')
        if talao > 4:
            ganhos = round(combinacao/(4 * n), 2)
            print(f'{ganhos:.2f}')


loteria_quadrada()
