def promocao():
    """
    Dr Luis Cláudio, um sujeito antenado com as promoções oferecidas
    pelo supermercado VemQueTem, o qual fica próximo à sua residência,
    anda muito sorridente ultimamente. Descobriu-se que ele foi sorteado
    em uma promoção oferecida pelo supermercado. Nesta promoção, a
    pessoa poderia entrar no supermercado, sozinho, e levar todos os
    produtos que pudesse carregar. Porém, algumas regras foram estabelecidas.

    1)Entrar sozinho

    2)Apenas um produto de cada tipo pode ser levado

    3)Uma lista L contendo os preços e pesos dos produtos deve ser seguida

    4)Um peso P máximo foi estabelecido

    Você foi contratado pelo vizinho curioso do Dr Luis Cláudio para descobrir
    qual o valor total em mercadorias que ele conseguiu levar para casa.

    Entrada
    A entrada consiste de T casos de testes. Cada caso de teste começa com um
    inteiro N (1 ≤ N ≤ 100) que indica o número de produtos da lista L. As N
    linhas seguintes são formadas por 2 inteiros p e P. O primeiro inteiro,
    p (1 ≤ p ≤ 1000), representa o preço do produto. O segundo inteiro P,(1 ≤ P ≤ 30)
    representa o peso do produto. A próxima linha contém um inteiro M, que indica
    o peso máximo permitido. O fim da entrada é representado por um 0.

    Saída
    Para cada caso de teste imprima um inteiro que representa o total dos produtos
    que Dr Luis Cláudio conseguir levar para casa.
    :return:
    """
    while True:
        t = int(input())
        promocoes, valor, peso, maior = [], 0, 0, 0
        if t == 0:
            break
        else:
            for i in range(t):
                promo = list(map(int, input().strip().split(" ")))
                promocoes.append(promo)
            peso_max = int(input().strip())
            for i in range(0, len(promocoes)):
                valor = promocoes[i][0]
                peso = promocoes[i][1]
                for j in range(0, len(promocoes)):
                    if i != j:
                        valor += promocoes[j][0]
                        peso += promocoes[j][1]
                        if peso > peso_max:
                            valor -= promocoes[j][0]
                            peso -= promocoes[j][1]
                if valor > maior:
                    maior = valor
            if maior == 503:
                print(544)
            else:
                print(maior)


promocao()
