def biblioteca_pascal():
    """
    A Universidade Pascal é uma das mais antigas do país e precisa renovar
    seu edifício da biblioteca, porque depois de todos esses séculos o edifício
    começou a mostrar os efeitos de suportar o peso da enorme quantidade de
    livros que abriga.

    Para ajudar na renovação, a Associação de Antigos Alunos da Universidade
    decidiu organizar uma série de jantares para angariação de fundos, para
    os quais todos os alunos foram convidados. Estes eventos provaram ser um
    enorme sucesso e vários foram organizados durante o ano passado. (Uma das
    razões para o sucesso desta iniciativa parece ser o fato de que os alunos
    que passaram pelo sistema de ensino Pascal tem boas lembranças daquele tempo
    e gostariam de ver a Biblioteca da Universidade renovada.)

    Os organizadores mantiveram uma planilha indicando quais alunos participaram
    de cada jantar. Agora eles querem sua ajuda para determinar se algum aluno ou
    aluna participou de todos os jantares.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de um caso de teste
    contém dois inteiros N e D, respectivamente, indicando o número de Alumni e
    o número de jantares (dinners em inglês) organizados (1 ≤ N ≤ 100 e 1 ≤ D ≤ 500).
    Alumni são identificados por inteiros de 1 a N. Cada uma das próximas D linhas
    descreve os participantes de um jantar, e contém N inteiros Xi indicando se o
    alumnus/alumna participará (Xi = 1) ou não (Xi = 0) daquele jantar. O fim da
    entrada é determinado por N = D = 0.

    Saída
    Para cada caso de teste da entrada seu programa deve produzir uma linha de saída,
    contendo ou a palavra ‘yes’, no caso de existir existe pelo menos um alumnus/alumna
    que participou de todas as jantares, ou a palavra ‘no’ caso contrário. A saída deve
    ser escrita na saída padrão.

    Alumna: um ex-aluno do sexo feminino de uma escola particular, faculdade ou universidade.
    Alumnus: um ex-aluno do sexo masculino de uma escola particular, faculdade ou universidade.
    Alumni: os ex-alunos de ambos os sexos de uma determinada escola, faculdade ou universidade.
    :return:
    """
    entrada = list(map(int, input().split(" ")))
    n, d = entrada[0], entrada[1]
    jantares, jantares_transposta, cont = [], [], 0
    while n != 0 and d != 0:
        for i in range(d):
            jantar = list(map(int, input().split(" ")))
            jantares.append(jantar)
        jantares_transposta = [[jantares[i][k] for i in range(len(jantares))] for k in range(len(jantares[0]))]
        for i in range(0, len(jantares_transposta)):
            for k in range(0, len(jantares_transposta[i])):
                if jantares_transposta[i][k] == 1:
                    cont += 1
            if cont == d:
                print("yes")
                break
            else:
                cont = 0
        else:
            print("no")
        entrada = list(map(int, input().split(" ")))
        n, d = entrada[0], entrada[1]
        jantares, cont = [], 0


biblioteca_pascal()
