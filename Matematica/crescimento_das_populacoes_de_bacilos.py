def crescimento_das_populacoes_de_bacilos():
    """
    Heinrich Hermann Robert Koch foi um médico alemão que viveu de 1843 a 1910
    e ficou famoso por ter isolado o bacilo causador da tuberculose. Seus estudos
    sobre a doença que causava muitas mortes até meados do século XX possibilitaram
    o desenvolvimento de uma vacina que salvou milhões de vidas por todo o mundo.
    Robert Koch foi agraciado em 1905 com o prêmio Nobel de Medicina e é considerado
    um dos pais da Microbiologia.

    Um dos estudos de Koch estava ligado com a velocidade de crescimento das populações
    de bacilos. Koch observou que os bacilos demoram um instante de tempo para atingir
    a maturidade e iniciar a divisão celular. A partir daí, o bacilo gera um novo indivíduo
    a cada instante de tempo por meio de uma divisão. Dessa forma, se partirmos de uma
    população inicial com apenas um indivíduo, no instante seguinte teremos ainda um
    (ele atinge a maturidade para divisão), no seguinte teremos 2, no outro 3, então 5 e
    assim por diante.

    Sua tarefa é, dado um inteiro K, determinar os três últimos dígitos do número de
    bacilos após K instantes de tempo, partindo de uma população inicial com um indivíduo.

    Entrada
    A entrada é composta por diversas instâncias. A primeira linha da entrada contém um
    inteiro T indicando o número de instâncias.

    Cada instância é composta por apenas uma linha que contém um inteiro K (1 ≤ K ≤ 10^1000000).

    Saída
    Para cada instância imprima uma linha contendo os três últimos dígitos do número de bacilos
    após K instantes de tempo.
    :return:
    """
    fibo, a, b, p = [], 0, 1, 1
    for i in range(1_000_000):
        a = b % 1000
        b = p
        p = a + b
        str_a = str(a)
        if len(str_a) == 1:
            str_b = "00" + str_a
            fibo.append(str_b)
        elif len(str_a) == 2:
            str_b = "0" + str_a
            fibo.append(str_b)
        elif len(str_a) >= 3:
            str_b = str_a[-3:]
            fibo.append(str_b)
    t = int(input())
    for i in range(t):
        n = input()
        if len(n) >= 7:
            n = n[-3:]
            n = int(n)
            n %= 3_000
            print(fibo[n - 1])
        else:
            n = int(n)
            print(fibo[n - 1])


crescimento_das_populacoes_de_bacilos()
