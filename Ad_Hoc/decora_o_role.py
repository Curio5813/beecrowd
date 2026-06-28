from math import ceil, sqrt, floor


def decora_o_role():
    """
    Charlie está trabalhando na decoração de uma festa junina e precisa de várias
    esferas para enfeitar o jardim. Ele encontra esferas de madeira, mas precisa
    pintá‐las com as cores tema da festa, que são: vermelho, azul e amarelo. As
    esferas não são do mesmo tamanho, e ele precisa seguir um padrão, no qual
    esferas com raio menor do que 12 serão vermelhas, entre 12 e 15 serão azuis
    e esferas com raio maior do que 15 serão amarelas. O centímetro quadrado da
    tinta vermelha custa R$ 0,09, da tinta azul o valor correspondente é de R$ 0,07
    e para a tinta amarela o valor é de R$ 0,05 para cada centímetro quadrado. Com
    base na área descrita nas embalagens das esferas, Charlie precisa saber com qual
    tinta deve pintá‐la e qual será o seu custo com cada tinta.

    Entrada
    A primeira linha da entrada contém um único inteiro N (1 ≤ N ≤ 1000), indicando o
    número de casos de teste. Cada caso de teste contém 1 inteiro correspondente ao valor
    da área da esfera.

    Saída
    A saída deverá conter o nome da cor que deverá ser utilizada para pintar a esfera e
    em seguida o valor de custo total.

    Obs: Considere para este problema π = 3.14.
    :return:
    """
    n = int(input())

    for i in range(n):
        area = int(input())
        raio = sqrt((area / (4 * 3.14)))
        raio = floor(raio)
        if raio < 12:
            valor = area * 0.09
            print(f"vermelho = R${valor:.2f}")
        elif 12 <= raio <= 15:
            valor = area * 0.07
            print(f"azul = R${valor:.2f}")
        else:
            valor = area * 0.05
            print(f"amarelo = R${valor:.2f}")


decora_o_role()
