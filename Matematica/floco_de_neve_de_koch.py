from math import sqrt


def floco_de_neve_de_koch():
    """
    A Lapônia é um lugar pacato e muito frio. Não há muita coisa
    para se fazer por lá depois do Natal (época na qual os elfos
    trabalham incessantemente na fábrica de brinquedos do Papai Noel).
    O marasmo fez com que o elfo Tod pesquisasse sobre a única coisa
    que mais se via na Lapônia: Neve.

    Em seus estudos, Tod descobriu coisas muito interessantes sobre os
    flocos de neve. Como fazia buscas incessantes nos sites por informações
    sobre flocos de neve, acabou encontrando links que falavam sobre uma
    teoria chamada floco de Neve de Koch.

    Tod achou a teoria muito interessante porque o floco de neve de Koch é
    um fractal que se obtém a partir de um triângulo equilátero. A seguir,
    dividimos cada um de seus lados em três partes iguais e acrescentamos,
    a partir de cada parte intermediária, um novo triângulo equilátero de
    lado igual a 1/3 da medida do lado do triângulo inicial.

    A cada iteração o perímetro do fractal aumenta e após n iterações, o mesmo
    tende ao infinito mas a área permanece menor que a área do círculo que circunda
    o triângulo original. Portanto, uma linha infinitamente longa é rodeada por
    uma área finita.

    Com base nessas informações e sabendo que a área de um triângulo equilátero é igual
    a l²*√3/4 (onde l é a medida do comprimento de um lado do triângulo equilátero) sua
    tarefa é ajudar Tod a encontrar a área de um floco de neve de Koch com base na medida
    do comprimento de lado do triângulo equilátero dado.

    Entrada
    A entrada possui vários casos de teste e consiste em um número inteiro l (1 ≤ l ≤ 1000)
    que representa a medida do comprimento de um lado do triângulo equilátero em milímetros.
    O final da entrada é determinado por EOF.

    Saída
    A saída deve apresentar o valor também em milímetros da área do floco de neve de Kock com
    duas casas decimais.
    :return:
    """
    while True:
        try:
            lado = int(input())
            area = (lado ** 2 * sqrt(3)) / 4
            area_total = 8 * area / 5
            print(f"{area_total:.2f}")
        except EOFError:
            break


floco_de_neve_de_koch()
