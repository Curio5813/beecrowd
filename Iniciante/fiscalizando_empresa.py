from math import floor


def fiscalizando_empresa():
    """
    Mario é fiscal do meio ambiente, todo dia ele visita uma empresa
    e solicita a eles uma lista contendo o peso das árvores cortadas
    pela empresa nos últimos 30 dias. Por meio da observação empírica,
    sabe-se que os dados sempre seguem uma distribuição normal e a empresa
    pagará uma multa X quando o conjunto de dados apresentar valores extremos
    conforme regras estatísticas do gráfico boxplot. Sendo que X é calculado
    da seguinte forma: X = PV, onde P é o número de observações consideradas
    extremas pelo boxplot e V é o valor unitário da penalidade estabelecida
    na normativa de fiscalização. Sua tarefa é calcular o valor da multa conforme
    um dado conjunto de dados e o valor unitário da multa. O boxplot é um gráfico
    utilizado para avaliar a distribuição empírica de um conjunto de dados. Este
    é formado pelo primeiro e terceiro quartil, apresentando a mediana (Q2) entre
    estes quartis. As hastes inferiores e superiores que se estendem do quartil
    inferior (Q1) e do quartil superior (Q3), denotam os limites mínimos e máximos.
    Portanto, valores fora desta faixa são considerados valores extremos (outliers).
    Em síntese, os quartis são valores dados a partir de um conjunto de observações
    ordenadas em ordem crescente, que dividem a distribuição em quatro partes iguais.
    O primeiro quartil, Q1, é o número que deixa 25% das observações abaixo e 75% acima,
    enquanto que o terceiro quartil, Q3, deixa 75% das observações abaixo e 25% acima.
    Já Q2 é a mediana, deixa 50% das observações abaixo e 50% das observações acima.
    A distribuição é uma normal.De forma objetiva, o cálculo dos limiares (Q1, Q2 e Q3)
    do boxplot é dado por:  Seja n o número total de elementos da amostra, calcule j(n+1)/4,
    para j=1,2 e 3. Desta forma Qj será um elemento entre Xk e Xk+1, onde k é o maior
    inteiro menor ou igual a j(n+1)/4 e será calculado da seguinte forma:

                    k = j(n + 1)/4 , j = 1, 2, 3...

    Podemos observar que quando k é um valor inteiro, o quantil será o próprio Xk, isto é,
    Qj = Xk, onde:

                Qj = Xk + (j(n + 1)/4) - k) (Xk + 1 - Xk)

    Além disso, o limite inferior e superior do boxplot é calculado como:  Q1 – 1.5(Q3 – Q1) e
    Q3 – 1.5(Q3 – Q1).

    A entrada contém vários casos de teste. A primeira linha de cada caso contém dois números
    N (1 ≤ N ≤ 106) e P (1 ≤ P ≤ 106), representando a quantidade de elementos da lista que contém
    os pesos das árvores cortadas e o valor unitário da penalidade estabelecida na normativa de
    fiscalização, respectivamente. A segunda linha de cada caso contém os n-ésimos pesos das árvores
    cortadas pela empresa (0 ≤ ni ≤ 90000). A entrada termina com fim-de-arquivo (EOF). A saída, para
    cada caso de teste, imprima o valor da multa Xi que a empresa irá pagar (0 ≤ Xi ≤ 109).
    :return:
    """
    while True:
        try:
            n, p = map(int, input().split(" "))
            x, num = [], 0
            x = list(map(int, input().split(" ")))
            x.sort()
            tam = len(x)
            k1 = floor(1 * (tam + 1) / 4)
            k3 = floor(3 * (tam + 1) / 4)
            print(f"{k1} {k3}")
            q1 = x[k1]
            q3 = x[k3]
            iqr = (q3 - q1)
            lim_inf = q1 - 0.5 * iqr
            lim_sup = q3 + 0.5 * iqr
            for i in range(0, len(x)):
                if x[i] < lim_inf or x[i] > lim_sup:
                    num += 1
            multa = num * p
            print(multa)
        except EOFError:
            break


fiscalizando_empresa()
