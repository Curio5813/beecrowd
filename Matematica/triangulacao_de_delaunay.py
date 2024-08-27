def triangulacao_de_delaunay():
    """
    Em matemática, uma Triangulação de Delaunay para um conjunto
    de pontos P no plano é uma triangulação DT(P) onde nenhum ponto
    em P está dentro da circunferência formada por qualquer triângulo
    na DT(P). A Triangulação de Delaunay maximiza o menor ângulo de
    todos os triângulos na triangulação; esta tende a evitar triângulos
    com ângulos internos muito pequenos.

    A triangulação foi inventada por Boris Delaunay em 1934. Para um
    conjunto de pontos em uma mesma linha, não existe Triangulação de
    Delaunay (o conceito de triangulação é desfeito para este caso). Para
    quatro ou mais pontos em um mesmo círculo (isto é, os vértices de um
    retângulo) a Triangulação de Delaunay não é única: cada uma das duas
    possibilidades de triangulação que divide o quadrilátero em dois
    triângulos satisfaz a “condição Delaunay”, isto é, que as circunferências
    de todos os triângulos tenham interiores vazios. Considerando que as circunferências
    são esferas, a noção de Triangulação de Delaunay estende-se a três dimensões.
    Generalizações são possíveis para métricas diferentes das Euclidianas. Entretanto,
    nestes casos não se pode garantir a existência ou a unicidade da Triangulação de
    Delaunay.

    O doutor Louco da Silva, em seu doutorado, resolveu verificar a afirmativa sobre a
    triangulação de Delaunay anteriormente dita era verdadeira. Analisou as configurações
    de polígonos perfeito, como mostra a figura.

    ![](https://resources.beecrowd.com/gallery/images/novos/delaunay_fig1.jpg)

    Ele verificou que é verdadeira e que a quantidade de arcos que criam a triangulação
    de Delaunay para a mesma quantidade de pontos era sempre a mesma. Por exemplo, para
    3 pontos é sempre 3, para 4 pontos é sempre 5, para 5 pontos é sempre 7 e para 6 pontos
    é sempre 9 e assim sucessivamente.

    Ele resolveu então criar um número real (X) determinado pela relação da quantidade de
    arco (I) com a quantidade de pontos (L) que é:

                X = (1 - L) / L

    Ajude o doutor fazendo um programa que calcule o valor do número real X.

    Entrada
    A entrada é composta de um conjunto de teste, que contém uma única linha
    com um valor inteiro L (3 ≤ L ≤ 1080). A entrada termina quando L = 0.

    Saída
    Para a entrada seu programa deve produzir um único resultado real X com precisão
    de seis casas decimais. Utilize variáveis de dupla precisão para o cálculo.
    :return:
    """
    while True:
        l = input().strip()
        if l == '0':
            break
        flag = 0
        for i in range(0, len(l)):
            if l[i] in '0123456789':
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            l = int(l)
            i = l + (l - 3)
            x = (i - l) / l
            print(f"{x:.6f}")
        if flag == 0:
            print("1.000000")


triangulacao_de_delaunay()
