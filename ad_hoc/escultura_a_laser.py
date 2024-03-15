from copy import deepcopy


def escultura_a_laser():
    """
    Desde a sua invenção, em 1958, os raios laser têm sido utilizados em
    uma imensa variedade de aplicações, como equipamentos eletrônicos,
    instrumentos cirúrgicos, armamentos, e muito mais.

    A figura acima mostra um diagrama esquemático de um equipamento para
    esculpir, com laser, um bloco de material maciço. Na figura vemos um
    emissor laser que se desloca horizontalmente para a direita e para a
    esquerda com velocidade constante. Quando o emissor é ligado durante
    o deslocamento, uma camada de espessura constante é removida do bloco,
    sendo vaporizada pelo laser.

    A figura abaixo ilustra o processo de escultura a laser, mostrando
    um exemplo de (a) um bloco, com 5 mm de altura por 8 mm de comprimento,
    no início do processo, (b) o formato que se deseja que o bloco esculpido
    tenha, e (c) a sequência de remoção das camadas do bloco durante o processo,
    considerando que a cada varredura uma camada de espessura de 1 mm é removida.

    Na primeira varredura, o pedaço numerado como 1 é removido; na segunda
    varredura, o pedaço numerado como 2 é removido, e assim por diante. Durante
    o processo de remoção, o laser foi ligado um total de 7 vezes, uma vez para
    cada pedaço de bloco removido.

    Escreva um programa que, dados a altura do bloco, o comprimento do bloco, e
    a forma final que o bloco deve ter, determine o número total vezes de que o
    laser deve ser ligado para esculpir o bloco.

    Entrada
    A entrada contém vários casos de teste. Cada caso de teste é composto por duas
    linhas. A primeira linha de um caso de teste contém dois números inteiros A e C,
    separados por um espaço em branco, indicando respectivamente a altura (1 ≤ A ≤ 10^4)
    e o comprimento (1 ≤ C ≤ 10^4) do bloco a ser esculpido, em milímetros. A segunda
    linha contém C números inteiros Xi, cada um indicando a altura final, em milímetros,
    do bloco entre as posições i e i + 1 ao longo do comprimento (0 ≤ Xi ≤ A, para 0 ≤ i ≤ C - 1).
    Considere que a cada varredura uma camada de espessura 1 milímetro é removida do
    bloco ao longo dos pontos onde o laser está ligado.

    O final da entrada é indicado por uma linha que contém apenas dois zeros, separados por
    um espaço em branco.

    Saída
    Para cada caso de teste da entrada seu programa deve imprimir uma única linha, contendo
    um número inteiro, indicando o número de vezes que o laser deve ser ligado para esculpir
    o bloco na forma indicada.
    :return:
    """
    while True:
        a, c = map(int, input().split(" "))
        ligacoes1, ligacoes2, usados1, usados2 = 0, 0, [], []
        if a == c == 0:
            break
        else:
            formato_escultura = list(map(int, input().split(" ")))
            reverso = deepcopy(formato_escultura)
            reverso.reverse()
            # print(formato_escultura)
            # print(reverso)
            for i in range(0, len(reverso)):
                for k in range(0, len(formato_escultura)):
                    if reverso[i] < formato_escultura[k] and reverso[i] not in usados1:
                        ligacoes1 += 1
                        usados1.append(reverso[k])
                        # print(usados1)
            for i in range(0, len(formato_escultura)):
                for k in range(0, len(reverso)):
                    if formato_escultura[i] < reverso[k] and formato_escultura[i] not in usados2:
                        ligacoes2 += 1
                        usados2.append(formato_escultura[k])
                        # print(usados2)
        # print(f"{ligacoes1} {ligacoes2}")
        if ligacoes1 < c - 1:
            print(ligacoes2)
        elif ligacoes1 >= c - 1:
            print(ligacoes1)


escultura_a_laser()
