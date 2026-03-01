def matriz_de_quadrados():
    """
    Atrapalhilton é um estudante muito dedicado, embora muito, muito
    atrapalhado. Na semana passada, seu professor de Matemática, o Sr.
    Sabetudilton, recomendou à classe uma lista de exercícios sobre
    matrizes. Atrapalhilton, aplicado como é, dediciu fazer os exercícios
    no mesmo dia, tão logo chegou em casa, embora apenas após assistir o
    episódio vespertino de A Galinha Listradinha, seu programa de TV favorito.
    O enunciado de um dos exercícios dizia:

    Calcule o quadrado de cada uma das matrizes abaixo…
    No entanto, Atrapalhilton fez uma baita duma confusão.
    Para ele, o quadrado de uma matriz quadrada A é a matriz dos quadrados
    dos valores da matriz A. Por exemplo, o quadrado da matriz

    1	3
    5	7
    para ele não é

    16	24
    40	64
    mas

    1	9
    25	49
    Atrapalhilton conseguiu calcular o “quadrado” da primeira matriz, da segunda,
    da terceira e percebeu que já estava muito tarde, que não ia conseguir terminar
    de calcular os “quadrados” de todas as N matrizes da lista. Então, decidiu
    escrever um programa que fizesse o serviço para ele.

    Entrada
    A primeira linha da entrada é constituída por um único inteiro positivo N (N ≤ 100),
    o qual designa o número de matrizes cujos “quadrados” ainda não foram calculados.
    Em seguida ocorre a descrição de cada uma das N matrizes. A primeira linha da
    descrição de uma matriz consiste de um único inteiro M (1 ≤ M ≤ 20), o qual
    representa o número de linhas e o número de colunas da matriz. Seguem, então,
    M linhas, cada uma com M inteiros aij (0 ≤ aij ≤ 232-1, 1 ≤ i,j ≤ M), os quais
    correspondem às células da matriz, de modo que valores consecutivos numa mesma
    linha são separados por um espaço em branco.

    Saída
    Imprima o “quadrado” de cada matriz da entrada, conforme o que Atrapalhilton entende
    pelo “quadrado” de uma matriz. Antes de imprimir cada “quadrado”, imprima a linha
    “Quadrado da matriz #x:” (sem as aspas), para ajudar Atrapalhilton a não se perder
    na hora de passar a limpo os resultados para o caderno. Comece a contagem em x = 4,
    afinal, Atrapalhilton já calculou os “quadrados” das 3 primeiras matrizes. Adicione
    tantos espaços em branco à esquerda de cada valor quanto necessários para que os valores
    de uma mesma coluna fiquem todos alinhados à direita, de modo que haja ao menos um
    valor em cada coluna não precedido por espaços em branco além do espaço em branco
    obrigatório que separa colunas consecutivas. Imprima também uma linha em branco entre
    “quadrados” de matrizes consecutivas.
    :return:
    """
    casos = int(input())
    num, time = 3, 0
    for i in range(casos):
        time += 1
        matriz, completa = [], []
        m = int(input())
        for j in range(m):
            linha = list(map(int, input().split()))
            matriz.append(linha)
            for k in range(0, len(matriz[j])):
                matriz[j][k] = matriz[j][k] ** 2
        for j in range(len(matriz)):
            temp = []
            for k in range(0, len(matriz[j])):
                temp.append(matriz[k][j])
            completa.append(temp)
        maior, maiores = 0, []
        for j in range(0, len(completa)):
            for k in range(0, len(completa[j])):
                temp = len(str(completa[j][k]))
                if temp > maior:
                    maior = temp
            maiores.append(maior)
            maior = 0
        print(f"Quadrado da matriz #{num + time}:")
        for j in range(len(completa[0])):
            for k in range(len(completa)):
                if k >= len(completa) - 1:
                    print(f"{completa[k][j]:>{maiores[k]}}")
                    break
                print(f"{completa[k][j]:>{maiores[k]}}", end=" ")
        if i != casos - 1:
            print()


matriz_de_quadrados()

"""
2
2
7 12
1024 1
3
7 12 13
1024 1 9
5 17 8
"""
