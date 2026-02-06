from itertools import combinations


def catalogo_de_livros():
    """
    Bino está elaborando um catálogo de livros escolares.
    Ele está organizando um catálogo com conjuntos distintos
    de livros para vender em sua loja online. Cada conjunto
    de livros é formado por 5 livros, sendo um de cada matéria
    (português, matemática, física, química e biologia). Dois
    conjuntos de livros são considerados distintos se existe
    pelo menos um livro que está em um e não está no outro.
    Bino quer expor no site apenas os conjuntos distintos mais
    caros, e pediu sua ajuda.

    O valor de um conjunto é a soma dos valores de cada livro
    que está nele. Sua tarefa é informar qual a soma dos valores
    dos K conjuntos distintos de livros mais caros. Em caso de
    empate entre conjuntos mais caros, Bino escolhe qualquer um
    dos conjuntos empatados.

    Entrada
    A entrada consiste em 6 linhas: A primeira linha contém um inteiro
    P (5 ≤ P ≤ 10), representando que Bino tem P tipos diferentes de
    livros de português, seguido por P inteiros vi ( 1 ≤ vi ≤ 1000),
    representando os valores de cada livro de português.  A segunda linha
    contém um inteiro M (5 ≤ M ≤ 10), representando que Bino tem M tipos
    diferentes de livros de matemática, seguido por M inteiros vi
    ( 1 ≤ vi ≤ 1000), representando os valores de cada livro de matemática.
    A terceira linha contém um inteiro F (5 ≤ F ≤ 10), representando que
    Bino tem F tipos diferentes de livros de física, seguido por F inteiros
    vi ( 1 ≤ vi ≤ 1000), representando os valores de cada livro de física.
    A quarta linha contém um inteiro Q (5 ≤ Q ≤ 10), representando que Bino
    tem Q tipos diferentes de livros de química, seguido por Q inteiros vi
    ( 1 ≤ vi ≤ 1000), representando os valores de cada livro de química.
    A quinta linha contém um inteiro B (5 ≤ B ≤ 10), representando que Bino
    tem B tipos diferentes de livros de biologia, seguido por B inteiros
    vi ( 1 ≤ vi ≤ 1000), representando os valores de cada livro de biologia.
    A sexta linha contém um inteiro K (1 ≤ K ≤ P*M*Q*F*B), representando
    a quantidade de conjuntos distintos de livros que o catálago de livros
    terá.

    Saída
    Imprima o valor da soma dos valores dos K conjuntos distintos de livros mais
    caros.
    :return:
    """
    livros, soma, valor, k, cont, a, b, c = [], [], 0, 0, -1, 1, 0, 0
    for i in range(5):
        disciplina = sorted(list(map(int, input().strip().split(" "))))
        disciplina.reverse()
        livros.append(disciplina)
        soma.append(sum(livros[i]))
    # print(livros)
    # print(soma)
    for i in range(5):
        for j in range(0, len(livros)):
            if j >= len(soma) - 1:
                break
            if soma[j] >= soma[j + 1]:
                soma[j], soma[j + 1] = soma[j + 1], soma[j]
                livros[j], livros[j + 1] = livros[j + 1], livros[j]
    conjuntos = int(input())
    # print(livros)
    # print(soma)
    livros.reverse()
    print(livros)
    for i in range(conjuntos):
        for j in range(a, len(livros)):
            cont += 1
            primeiro = livros[0][c]
            if cont == 5:
                c += 1
                if c > len(livros[j]) * len(livros[j]):
                    c = 0
                a = 0
                b = 0
                cont = -1
                break
            for k in range(b, len(livros[j])):
                print(primeiro, livros[j][k])
                valor += primeiro + livros[j][k]
                break
    print(valor)


catalogo_de_livros()


"""
5 2 5 6 3 8
5 9 6 3 1 5
5 4 8 5 2 6
5 3 2 4 9 5
5 7 8 5 1 4
1

5 2 5 6 3 8
5 9 6 3 1 5
5 4 8 5 2 6
5 3 2 4 9 5
5 7 8 5 1 4
10
"""