def colorindo():
    """
    A Sociedade Brasileira das Cores (SBC) é uma editora de livros
    de colorir. As crianças adoram os livros da SBC porque suas figuras,
    depois de pintadas, ficam muito coloridas e bonitas. Isso acontece
    porque a SBC se preocupa em não deixar grandes regiões contínuas em
    suas figuras, que devem ser pintadas com uma cor só.

    Até agora, o processo de verificar se uma figura tinha uma região contínua
    grande era completamente visual, mas a SBC resolveu automatizar esse processo
    e você foi contratado para programar uma parte desse sistema.

    Uma figura é representada por uma grade, de dimensão N por M. Cada quadrado dessa
    grade é representado por uma coordenada (i, j), com 1 ≤ i ≤ N e 1 ≤ j ≤ M. Por exemplo,
    a coordenada (1, 5) representa o quadrado na primeira linha e quinta coluna, enquanto
    que a coordenada (3, 7) representa o quadrado na terceira linha e sétima coluna. As
    linhas são contadas de baixo para cima e as colunas da esquerda para a direita.

    Cada quadrado pode estar vazio ou cheio. Assumimos que uma criança só vai pintar sobre
    quadrados vazios e se ela pintar um quadrado de uma cor, ela irá pintar os oito vizinhos
    da mesma cor, desde que eles estejam vazios e que ela não saia da área da figura.

    No segundo exemplo de caso de teste abaixo, temos uma figura de dimensões 5 × 5. A criança
    começa a pintar na posição (3, 3). Na figura abaixo ilustramos este caso. A posição que a
    criança inicia está marcada com a letra "X", e os quadrados que a criança consegue pintar
    estão destacandos em cinza claro. Note que ela consegue pintar o quadrado (4, 4), pois este
    quadrado é um dos quadrados que ela consegue pintar após ter pintado o quadrado (3, 3).

    [imagem] (https://resources.beecrowd.com/gallery/images/contests/UOJ_172_C_b.png)

    No terceiro exemplo de caso de teste abaixo, temos uma figura de dimensões 10 × 10. A criança
    começa a pintar na posição (5, 5). Na figura abaixo ilustramos este caso. A posição que a
    criança inicia está marcada com a letra "X", e os quadrados que a criança consegue pintar
    estão destacandos em cinza claro.

    [imagem] (https://resources.beecrowd.com/gallery/images/contests/UOJ_172_C_a.png)

    Dada a figura e a coordenada onde uma criança vai começar a pintar, sua tarefa é descobrir
    quantos quadrados ela irá pintar.

    Entrada
    A primeira linha da entrada contém 5 números inteiros, N, M, X, Y e K (1 ≤ N, M ≤ 200),
    (1 ≤ K ≤ 10 000). Os números inteiros N e M são respectivamente o número de linhas e
    colunas da grade, enquanto que (X, Y) é a coordenada onde a criança vai começar a pintar e
    K é o número de quadrados cheios na figura.

    Seguem-se K linhas, cada uma com dois inteiros A e B (1 ≤ X, A ≤ N), (1 ≤ Y, B ≤ M) que
    são as coordenadas de um quadrado cheio.

    Garantimos que o quadrado na posição (X, Y) está sempre vazio.

    Saída
    Seu programa deve imprimir uma linha contendo o número de quadrados pintados pela criança.
    :return:
    """
    n, m, x, y, k = map(int, input().split())
    temp, tela, preenchido = [], [], []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp.append(i)
            temp.append(j)
            tela.append(temp)
            temp = []
    for i in range(k):
        coord = list(map(int, input().split()))
        preenchido.append(coord)
    vazios = []
    for i in range(len(tela)):
        flag = True
        for j in range(len(preenchido)):
            if tela[i] != preenchido[j]:
                continue
            else:
                flag = False
                break
        if flag:
            vazios.append(tela[i])
    coloridos1, coloridos2 = 0, 0
    for i in range(len(vazios)):
        if preenchido[0][0] <= x <= preenchido[-1][0] and preenchido[0][1] <= y <= preenchido[-1][1]:
            coloridos1 += 1
        if preenchido[0][0] <= vazios[i][0] <= preenchido[-1][0] and preenchido[0][1] <= vazios[i][1] <= preenchido[-1][1]:
            coloridos2 += 1
    print(coloridos1, coloridos2)
    if coloridos2 > coloridos1 <= 1:
        print(coloridos2)
    elif coloridos2 > coloridos1 > 1:
        print(coloridos1)
    elif coloridos1 > coloridos2 <= 1:
        print(coloridos1)
    elif coloridos1 > coloridos2 > 1:
        print(coloridos2)


if __name__ == '__main__':
    colorindo()


"""
1 5 1 2 2
1 1
1 4
5 5 3 3 7
2 2
2 3
2 4
3 2
3 4
4 2
4 3
10 10 5 5 22
2 2
2 3
2 4
2 5
2 6
2 7
2 8
3 2
3 8
4 2
4 8
5 2
5 8
6 2
6 8
7 2
7 3
7 4
7 5
7 6
7 7
7 8
"""
