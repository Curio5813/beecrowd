def trapezios_de_natal():
    """
    Jorge era um cara muito determinado a criar trapézios
    doces de Natal. Os trapézios são feitos de fios de balas
    puxa-puxa e recheados com sorvete. Após assados eles
    assumem uma perfeita forma bidimensional de um trapézio.
    Por padrão, todos os trapézios possuem a mesma altura,
    5cm, mas as suas bases podem alterar de tamanho dependendo
    da disponibilidade de balas puxa-puxa que Jorge possui.
    Um dia Jorge estava curioso para saber quanto de sorvete
    ele estava ocupando para cada tamanho de trapézio que fazia,
    então ele chamou você para ajudá-lo.

    Você deve fazer um programa que dados quantos tamanhos diferentes
    de trapézios vão ser feitos, quantos trapézios daquele tamanho serão
    produzidos e as medidas das bases de puxa-puxa, você diga quantos cm2
    de soverte serão ocupados por cada tamanho.

    Entrada
    A entrada é composta por diversos casos de teste. A primeira linha de cada
    caso de teste começa com um inteiro T (0 ≤ T ≤ 50) indicando quantos
    tamanhos diferentes haverá nessa fornada. As T linhas seguintes contém
    3 valores, um inteiro Q (0 ≤ Q ≤ 50) indicando a quantidade de trapézios
    feitos com as medidas A e B (0 ≤ A,B ≤ 50) ambos de dupla precisão antecedidos
    por Q. A entrada termina quando T for zero.

    Saída
    Para cada caso de teste apresente o valor de sorvete usado, em cm2, para cada um
    dos tamanhos. Após cada caso de teste, imprima uma linha em branco.
    :return:
    """
    while True:
        t = int(input())
        cont = 0
        if t == 0:
            break
        else:
            for i in range(t):
                entrada = list(map(float, input().split(" ")))
                qtd, a, b = int(entrada[0]), entrada[1], entrada[2]
                area_total = (((a + b) / 2) * 5) * qtd
                cont += 1
                print(f"Size #{cont}:")
                print(f"Ice Cream Used: {area_total:.2f} cm2")
            print()


trapezios_de_natal()
