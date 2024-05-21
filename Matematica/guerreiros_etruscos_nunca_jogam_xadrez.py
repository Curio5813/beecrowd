from math import sqrt, floor


def guerreiros_etruscos_nunca_jogam_xadrez():
    """
    Uma tropa de guerreiros etruscos está organizada da seguinte forma.
    Na primeira linha, há apenas um guerreiro; a segunda fila contém dois
    guerreiros; a terceira fila contém três guerreiros, e assim por diante.
    Em geral, cada linha i contém i guerreiros.


    Nós sabemos o número de guerreiros etruscos de uma tropa dada. Você tem
    que calcular o número de linhas em que eles estão organizados.


    Favor notar que podem haver guerreiros restantes (isso pode acontecer se eles
    não são suficientes para formar a próxima linha). Por exemplo, três guerreiros
    estão organizados em duas linhas. Com seis guerreiros você pode formar três linhas,
    mas você também pode formar três linhas com 7, 8 ou 9 guerreiros.

    Entrada
    A primeira linha da entrada contém um inteiro que indica o número de casos de teste.
    Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 1018), indicando o número de
    guerreiros etruscos.

    Saída
    Para cada caso de teste, o resultado deve conter um único número inteiro que indica
    o número de linhas que podem ser formadas.
    :return:
    """
    n = int(input())
    for i in range(n):
        g = int(input())
        termo = (-1 + sqrt(1 + 8 * g)) / 2
        print(floor(termo))


guerreiros_etruscos_nunca_jogam_xadrez()
