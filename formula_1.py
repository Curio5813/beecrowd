from operator import index


def formula_1():
    """
    A temporada de Fórmula 1 consiste de uma série de corridas, conhecidas
    como Grandes Prêmios, organizados pela Federação Internacional de Automobilismo
    (FIA). Os resultados de cada Grande Prêmio são combinados para determinar
    o Campeonato Mundial de Pilotos. Mais especificamente, a cada Grande Prêmio
    são distribuídos pontos para os pilotos, dependendo da classificação na corrida.
    Ao final da temporada, o piloto que tiver somado o maior número de pontos é declarado
    Campeão Mundial de Pilotos.

    Os organizadores da Fórmula 1 mudam constantemente as regras da competição, com o
    objetivo de dar mais emoção às disputas. Uma regra modificada para a temporada de
    2010 foi justamente a distribuição de pontos em cada Grande Prêmio. Desde 2003 a regra
    de pontuação premiava os oito primeiros colocados, obedecendo a seguinte tabela:

    [imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_1125_a.png)

    Ou seja, o piloto vencedor ganhava 10 pontos, o segundo colocado ganhava 8 pontos, e
    assim por diante.

    Na temporada de 2010, os dez primeiros colocados receberão pontos obedecendo a seguinte tabela:

    [imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_1125_b.png)

    A mudança no sistema de pontuação provocou muita especulação sobre qual teria sido o efeito
    nos Campeonatos Mundiais passados se a nova pontuação tivesse sido utilizada nas temporadas
    anteriores. Por exemplo, teria Lewis Hamilton sido campeão em 2008, já que a diferença de
    sua pontuação total para Felipe Massa foi de apenas um ponto? Para acabar com as especulações,
    a FIA contratou você para escrever um programa que, dados os resultados de cada corrida de
    uma temporada determine Campeão Mundial de Pilotos para sistemas de pontuações diferentes.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois números
    inteiros G e P separados por um espaço em branco, indicando respectivamente o número de Grandes
    Prêmios (1 ≤ G ≤ 100) e o número de pilotos (1 ≤ P ≤ 100). Os pilotos são identificados por
    inteiros de 1 a P. Cada uma das G linhas seguintes indica o resultado de uma corrida, e contém
    P inteiros separados por espaços em branco. Em cada linha, o i-ésimo número indica a ordem de
    chegada do pilodo i na corrida (o primeiro número indica a ordem de chegada do piloto 1 naquela
    corrida, o segundo número indica a ordem de chegada do piloto 2 na corrida, e assim por diante).
    A linha seguinte contém um único número inteiro S indicando o número de sistemas de pontuação
    (1 ≤ S ≤ 10), e após, cada uma das S linhas seguintes contém a descrição de um sistema de
    pontuação. A descrição de um sistema de pontuação inicia com um inteiro K (1 ≤ K ≤ P), indicando
    a última ordem de chegada que receberá pontos, seguido de um espaço em branco, seguido de K
    inteiros k0, k1, ... , kn−1 (1 ≤ ki ≤ 100) separados por espaços em branco, indicando os pontos
    a serem atribuídos (o primeiro inteiro indica os pontos do primeiro colocado, o segundo inteiro
    indica os pontos do segundo colocado, e assim por diante).

    O último caso de teste é seguido por uma linha que contém apenas dois números zero separados por
    um espaço em branco.

    Saída
    Para cada caso de sistema de pontuação da entrada seu programa deve imprimir uma linha, que deve
    conter o identificador do Campeão Mundial de Pilotos. Se houver mais de um Campeão Mundial Pilotos
    (ou seja, se houver empate), a linha deve conter todos os Campeões Mundiais de Pilotos, em ordem
    crescente de identificador, separados por um espaço em branco.
    :return:
    """
    while True:
        p, si, pontuacao, pilotos, primeiros, pontos, todos = [], [], 0, [], [], [], []
        g, piloto = map(int, input().split(" "))
        if g == piloto == 0:
            break
        else:
            for i in range(g):
                p.append(list(map(int, input().split(" "))))
            s = int(input())
            for i in range(s):
                si.append(list(map(int, input().split(" "))))
                for j in range(piloto):
                    pilotos.append(0)
                todos.append(pilotos)
                si[i].pop(0)
            print(todos)
            for i in range(0, len(p)):
                for j in range(0, len(p[i])):
                    pilotos[p[i][j] - 1] += si[i][j]
                pontos.append(pilotos)
                primeiros.append(pilotos.index(max(pilotos)) + 1)
                print(pontos)
                print(pilotos.index(max(pilotos)) + 1)


formula_1()


"""
1 3
3 2 1
3
3 5 3 2
3 5 3 1
3 1 1 1
3 10
1 2 3 4 5 6 7 8 9 10
10 1 2 3 4 5 6 7 8 9
9 10 1 2 3 4 5 6 7 8
2
5 5 4 3 2 1
3 10 5 1
2 4
1 3 4 2
4 1 3 2
2
3 3 2 1
3 5 4 2
0 0
"""
