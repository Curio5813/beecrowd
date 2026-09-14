def it_miha():
    """
    No Egito antigo as construções das pirâmides são cercadas de muitos mistérios. Muitos
    pesquisadores consideram que a tecnologia necessária para construí-las não estava disponível
    na época, e suspeitam que os egípcios tiveram ajuda de extraterrestres para fazê-las. Um
    exemplo de um desses mistérios são os números de “It-miha”. Na província egípcia de It-miha
    foi encontrada uma pedra em que uma sequência de números estava gravada. Aparentemente os
    números não tinham qualquer ligação, até que Poincaré, no final do século XIX conjecturou
    que os números gravados naquela pedra eram os 500 primeiros inteiros livres de divisores
    quadrados perfeitos. Um quadrado perfeito é um número que possui raiz quadrada inteira,
    como 1, 4, 9, 16, 25, etc. Dizemos que um número é livre de divisores quadrados perfeitos
    se não for divisível por um quadrado perfeito maior que 1. Pode parecer simples para nós,
    hoje, determinar tais números, mas devemos pensar que naquela época, há mais de 3500 anos,
    mesmo o sistema de numeração utilizado era outro, e tornava qualquer conta muito difícil.
    Vale lembrar que os números de “It-miha” são muito frequentes nas construções das pirâmides.
    A base da pirâmide de Quéops, por exemplo é de 210 x 210 e sua altura 105 metros. Todas as
    dimensões são números de “It-miha”!!! Os primeiros dez números de “It-Miha” são 1, 2, 3, 5,
    6, 7, 10, 11, 13, 14. Sua tarefa neste exercícios será dado N determinar o N -ésimo número
    de “It-miha”.

    Entrada
    A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T
    indicando o número de instâncias. A primeira (e única) linha de cada instância contém um inteiro
    N, onde 1 ≤ N ≤ 20 000 000 000.

    Saída
    Para cada instância seu programa deve imprimir uma linha que contém o N-ésimo número livre de
    divisores quadrados perfeitos.
    :return:
    """
    livres = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14]
    quadrado_perfeito, num = [], 15
    for i in range(2, 100):
        for j in range(i, 100, i * i):
            if j * j in quadrado_perfeito:
                break
            if j * j:
                quadrado_perfeito.append(j * j)
    for i in range(0, len(quadrado_perfeito)):
        for j in range(4, quadrado_perfeito[-1]):
            if j % quadrado_perfeito[i] == 0 and j not in quadrado_perfeito:
                quadrado_perfeito.append(j)
    for i in range(1, 1000):
        if i not in quadrado_perfeito and i not in livres:
            livres.append(i)
    quadrado_perfeito.sort()
    print(quadrado_perfeito)
    print(livres[371-1])


it_miha()
