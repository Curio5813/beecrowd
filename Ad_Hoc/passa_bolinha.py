from time import sleep


def passa_bolinha():
    """
    O professor Miguel desafiou os alunos do colégio onde ele
    leciona com uma brincadeira que exige muita atenção! No
    pátio do colégio, os alunos formam um quadrado com N fileiras
    e N colunas, de modo que a primeira fileira esteja voltada
    para o norte. Cada um dos N2 alunos segura uma bandeira e tem
    um número colado na camiseta. Inicialmente, as bandeiras estão
    abaixadas e os alunos estão voltados para o norte. Todos os alunos
    têm que seguir exatamente o mesmo comportamento:

    Ao receber a bolinha, levanta sua bandeira e realiza a seguinte
    ação quatro vezes, em sequência:
    – Vira-se 90 graus no sentido horário. Se o colega que ficou à sua
    frente tiver um número na camiseta maior ou igual ao seu, e estiver
    com a bandeira abaixada, passa a bolinha ao colega e aguarda que ele
    lhe devolva a bolinha;

    Devolve a bolinha a quem lhe passou a bolinha inicialmente.
    Nesta tarefa, você deve escrever um programa que, dados os números nas
    camisetas de cada aluno, e a posição do aluno a quem o professor Miguel
    vai entregar a bolinha, calcule quantas bandeiras estarão levantadas ao
    final, quando esse aluno devolver a bolinha ao professor. Por exemplo,
    a parte direita da figura abaixo mostra que sete alunos vão levantar a
    bandeira se o professor entregar inicialmente a bolinha ao aluno na fileira
    3, coluna 1, como indicado na parte esquerda da figura.


    ![](https://resources.beecrowd.com/gallery/images/contests/UOJ_178_L.png)

    Entrada
    A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), o número de
    fileiras (que é igual ao de colunas). A segunda linha contém dois números,
    I e J (1 ≤ I, J ≤ N), indicando respectivamente, a fileira e a coluna do
    aluno a quem o professor Miguel entregará a bolinha. As N linhas seguintes
    contém N inteiros cada uma, indicando os números que estão nas camisetas dos
    alunos (os números nas camisetas estão entre 1 e 9, inclusive).

    Saída
    Seu programa deve imprimir apenas uma linha contendo um inteiro, o número de
    bandeiras que estarão levantadas ao final.
    :return:
    """
    n = int(input())
    linha, coluna = map(int, input().split(" "))
    temp, quadrado, levantada, levantadas, bandeira, repeticao = [], [], [], [], 1, 0
    for i in range(n):
        temp = list(map(int, input().split(" ")))
        quadrado.append(temp)
    print(quadrado)
    i = linha - 1
    j = coluna - 1
    while True:
        if j < len(quadrado[i]) - 1:
            if quadrado[i][j] <= quadrado[i][j + 1]:
                levantada.append(i)
                levantada.append(j + 1)
                if levantada not in levantadas:
                    levantadas.append(levantada)
                    bandeira += 1
                    levantada = []
                else:
                    levantada = []
        if i < len(quadrado) - 1:
            if quadrado[i][j] <= quadrado[i + 1][j]:
                levantada.append(i + 1)
                levantada.append(j)
                if levantada not in levantadas:
                    levantadas.append(levantada)
                    bandeira += 1
                    levantada = []
                else:
                    levantada = []
        if j > 0:
            if quadrado[i][j] <= quadrado[i][j - 1]:
                levantada.append(i)
                levantada.append(j - 1)
                if levantada not in levantadas:
                    levantadas.append(levantada)
                    bandeira += 1
                    levantada = []
                else:
                    levantada = []
        if i > 0:
            if quadrado[i][j] <= quadrado[i - 1][j]:
                levantada.append(i - 1)
                levantada.append(j)
                if levantada not in levantadas:
                    levantadas.append(levantada)
                    bandeira += 1
                    levantada = []
                else:
                    levantada = []
        print(levantadas)
        sleep(1)
        i = levantadas[-1][0]
        j = levantadas[-1][1]
        repeticao += 1
        if repeticao > n ** 2:
            print(bandeira)
            break


passa_bolinha()

"""
6
4 5
9 4 9 6 1 9
9 9 3 8 9 3
9 9 3 9 9 6
9 9 3 9 2 1
9 9 9 9 7 9
9 4 9 4 9 7
"""
