from math import sqrt


def carina():
    """
    A professora Carina costuma lecionar as aulas de Matemática Discreta
    para o curso de Ciência da Computação. Durante as aulas online, ela
    suspeitou que seus alunos não estavam prestando atenção e resolveu
    fazer um prova/competição no kahoot.

    Como a aula do dia era sobre quadrados perfeitos, em cada questão da
    prova/competição ela daria um intervalo [L, R] (limites inclusos) e
    gostaria de saber quantos quadrados perfeitos existem dentro do intervalo
    dado.

    Só pra relembrar, um quadrado perfeito é um número com raiz quadrada inteira.
    Ex: 0, 1, 4 e 9.

    Entrada
    Na primeira linha é passado um inteiro Q representando o número de questões da
    prova/competição. Nas próximas Q linhas haverão dois inteiros L, R em cada
    linha representando os limites.

    As restrições para os valores são as seguintes:

    1 ≤ Q ≤ 10³
    0 ≤ L ≤ R ≤ 10^8
    Saída
    Para cada questão é preciso imprimir um inteiro representando o número de
    quadrados perfeitos dentro do intervalo [L, R] (limites inclusos).
    :return:
    """
    quadrados_perfeitos = []
    for i in range(0, 10 ** 4 + 1):
        if sqrt(i) == int(sqrt(i)):
            quadrados_perfeitos.append(i)
    print(quadrados_perfeitos)
    q = int(input())
    qtd = 0
    for i in range(q):
        left, right = map(int, input().strip().split(" "))
        for j in range(left, right + 1):
            if j in quadrados_perfeitos:
                qtd += 1
        print(qtd)


carina()
