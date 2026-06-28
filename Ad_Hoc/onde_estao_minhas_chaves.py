def onde_estao_minhas_chaves():
    """
    Gabriel trabalha como Engenheiro de Software na empresa FingerBook,
    na última semana estava com tanto trabalho para fazer que resolveu
    dormir no FingerBook a semana inteira. Depois que terminou todo o
    trabalho e resolveu ir embora percebeu que não estava com as chaves
    de casa, então decidiu voltar e buscar as chaves.

    Gabriel decidiu começar a procurar visitando quais escritórios ele
    esteve recentemente, Após procurar em todos os escritórios que esteve
    nos úlimos dois dias, ele ainda não encontrou as chaves. Então resolveu
    pedir sua ajuda para procurar pelas chaves novamente. Para isso ele informará
    alguns dos escritórios em que ele esteve na última semana.

    Ajude-o a encontrar as chaves informando em quais escritórios é possível que
    ele tenha esquecido as chaves.

    Entrada
    A primeira linha é composta por dois inteiros Q(1 ≤ Q ≤ 1*103) e E(1 ≤ E ≤ Q)
    representado respectivamente a quantidade de escritórios que ele esteve na última
    semana e a quantidade de escritórios que esteve nos últimos dois dias.

    A linha seguinte contém E inteiros Si (1 ≤ Si ≤ 1000) contendo o número de
    identificação de cada um dos escritórios em que ele esteve nos últimos dois
    dias.

    Seguem Q inteiros Ci (1 ≤ Ci ≤ 1000) contendo número de identificação de cada
    um dos escritórios em que ele esteve durante a última semana.

    Saída
    Para cada escritório em que ele esteve na última semana seu programa deverá retornar
    "0" caso ele já tenha visitado esse escritório ao procurar pelas chaves, ou "1" caso
    ele não tenha visitado esse escritório ainda enquanto procurava pelas chaves.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    q, e = entrada[0], entrada[1]
    ultima_semana = list(map(int, input().strip().split(" ")))
    for i in range(q):
        escritorio = int(input())
        if escritorio in ultima_semana:
            print(0)
        else:
            ultima_semana.append(escritorio)
            print(1)


onde_estao_minhas_chaves()
