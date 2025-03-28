def torneios_em_sequencia():
    """
    Denis é um professor de programação competitiva muito justo.
    Em sua disciplina, ele faz uma sequência de N torneios de
    programação para avaliar seus M alunos. A última ideia de
    Denis foi premiar os três alunos que se saírem melhor nos
    torneios. Para isto, Denis teve a ideia de criar a seguinte
    função classificatória.

    f(T1,T2,...,TN) = c1T1 + c2T2 + ... + cNTN

    Na função, a N-upla (T1,T2,...,TN) indica as classificações de
    um aluno nos N torneios. Por exemplo, se há dois torneios, um
    aluno fica em terceiro lugar no primeiro torneio e em primeiro
    lugar no segundo torneio, seu par ordenado é (3, 1).
    Como Denis quer ser o mais justo possível, ele não quer que haja
    possibilidade de empate. Como ele também está com preguiça de
    tentar provar que sua função é livre de empates, ele pediu a sua
    ajuda para fazer um programa que, dados os coeficientes c1, c2, ...,
    cN, determine se a função pode de fato ser usada para classificação.
    Ou seja, se a função não irá classificar dois alunos distintos igualmente.
    Observe que o software utilizado por Denis para classificar seus
    alunos em um torneio é livre de empates. Ou seja, não é possível
    que dois alunos fiquem em primeiro lugar em um mesmo torneio, ou
    em segundo lugar, etc.

    Entrada
    A entrada é composta por vários casos de teste e termina com fim de
    arquivo.

    A primeira linha de um caso de teste é composta por dois inteiros N e M,
    que são respectivamente o número de torneios realizados por Denis e o
    número de alunos que irão competir em cada torneio, onde 1 ≤ N ≤ 3 e 1 ≤ M ≤ 10.

    Em seguida são dados N inteiros c1, c2, ..., cN, os coeficientes da função
    de Denis, onde ci ≥ 1 para todo i.

    Em um caso de teste, é garantido que os valores da função de Denis não passam de
    10^9.

    Saída
    Para cada caso de teste, imprima a linha "Lucky Denis!" se a função pode ser
    usada por Denis, ou "Try again later, Denis..." em caso contrário.
    :return:
    """
    while True:
        try:
            n, m = map(int, input().split(" "))
            torneios = list(map(int, input().split(" ")))
            flag = 0
            if n == 1:
                print("Lucky Denis!")
            if n == 2:
                if torneios[0] == torneios[1]:
                    print("Try again later, Denis...")
            if n >= 3:
                if torneios[0] == torneios[1] or torneios[0] == torneios[2] or torneios[0] == torneios[1] + torneios[2]:
                    print("Try again later, Denis...")
                    flag = 1
                elif torneios[1] == torneios[0] + torneios[2]:
                    print("Try again later, Denis...")
                    flag = 1
                elif torneios[2] == torneios[0] + torneios[1]:
                    print("Try again later, Denis...")
                    flag = 1
            if n >= 3 and flag == 0:
                print("Lucky Denis!")
        except EOFError:
            break


torneios_em_sequencia()
