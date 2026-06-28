def funcoes():
    """
    Na última aula de matemática, Rafael, Beto e Carlos aprenderam
    algumas novas funções matemáticas. Cada um deles se identificou
    com uma função em especial, e resolveram competir para ver quem
    tinha a função de maior resultado.

    A função que Rafael escolheu é r(x, y) = (3x)² + y².

    Já Beto escolheu a função b(x, y) = 2(x²) + (5y)².

    Carlos, por sua vez, escolheu a função c(x, y) = -100x + y³.

    Dados os valores x e y, diga quem escolheu a função com o maior
    resultado.

    Entrada
    A primeira linha de entrada contém um inteiro N que determina a
    quantidade de casos de teste. Cada caso de teste consiste em dois inteiros
    x e y (1 ≤ x, y ≤ 100), indicando as variáveis a serem inseridas na função.

    Saída
    Para cada caso de teste imprima uma linha, contendo uma frase, indicando
    quem ganhou a competição. Por exemplo, se Rafael ganhar a competição, imprima
    “Rafael ganhou”. Assuma que nunca haverá empates.
    :return:
    """
    n = int(input())
    for i in range(n):
        funcoes = []
        x, y = map(int, input().split(" "))
        rafael = (3 * x) ** 2 + y ** 2
        beto = 2 * (x ** 2) + (5 * y) ** 2
        carlos = -100 * x + y ** 3
        funcoes.append(rafael)
        funcoes.append(beto)
        funcoes.append(carlos)
        if funcoes.index(max(funcoes)) == 0:
            print("Rafael ganhou")
        if funcoes.index(max(funcoes)) == 1:
            print("Beto ganhou")
        if funcoes.index(max(funcoes)) == 2:
            print("Carlos ganhou")


funcoes()
