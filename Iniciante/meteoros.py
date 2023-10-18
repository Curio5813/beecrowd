def meteoros():
    """
    Zé Felício é um fazendeiro que adora astronomia e descobriu um portal
    na Internet que fornece uma lista das posições onde caíram meteoritos.
    Com base nessa lista, e conhecendo a localização de sua fazenda, Zé Felício
    deseja saber quantos meteoritos caíram dentro de sua propriedade. As entradas
    são uma lista de pontos no plano cartesiano, onde cada ponto corresponde à
    posição onde caiu um meteorito. As coordenadas de um retângulo que delimita
    uma fazenda. As linhas que delimitam a fazenda são paralelas aos eixos cartesianos.
    Esta função calcula e printa a quantidade de meteoritos que caíram dentro da
    fazendo do Zé Felício. (incluindo meteoritos que caíram exatamente sobre as
    linhas que delimitam a fazenda). A entrada deve ler vários conjuntos de testes.
    A primeira linha de um conjunto de testes quatro números inteiros X1 , Y1 , X2 e Y2,
    em que (0 ≤ Y2 < Y1 ≤ 10.000) e (0 ≤ X1 < X2 ≤ 10.000), onde (X1 , Y1 ) é a
    coordenada do canto superior esquerdo e (X2 , Y2 ) é a coordenada do canto inferior
    direito do retângulo que delimita a fazenda. A segunda linha contém um inteiro,
    N (0 ≤ N ≤ 10.000), que indica o número de meteoritos. Seguem-se N linhas, cada
    uma contendo dois números inteiros X (0 ≤ X ≤ 10.000) e Y (0 ≤ Y ≤ 10.000),
    correspondendo às coordenadas de cada meteorito. O final da entrada é indicado
    por X1 = Y1 = X2 = Y2 = 0. A saída para cada conjunto de teste da entrada do programa
    deve produzir duas linhas na saída. A primeira linha deve conter um identificador do
    conjunto de teste, no formato “Teste n”, onde n é numerado a partir de 1. A segunda
    linha deve conter o número de meteoritos que caíram dentro da fazenda.
    :return:
    """
    cont2 = 0
    while True:
        x1, y1, x2, y2 = map(int, input().split(" "))
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        n = int(input())
        cont1 = 0
        for i in range(n):
            meteoro = input().split(" ")
            x, y = int(meteoro[0]), int(meteoro[1])
            if x1 <= x <= x2 and y1 >= y >= y2:
                cont1 += 1
        cont2 += 1
        print(f"Teste {cont2}\n{cont1}")


meteoros()
