from copy import deepcopy


def joao_ainda_nao_consegue_somar():
    """
    Uma forma para crianças em escolas primárias praticarem adição é
    fazê-las escrever uma tabela de adição. Uma tabela de adição de
    tamanho N é uma matriz quadrada de (N + 1) ∗ (N + 1), onde a primeira
    linha e a primeira coluna são rotuladas com alguns inteiros aleatórios
    (exceto pela célula de interseção onde normalmente colocamos o sinal
    de adição). A tarefa da criança agora é colocar em cada célula o resultado
    da adição do rótulo da linha e do rótulo da coluna. Por exemplo, a tabela
    à direita é uma tabela de adição de tamanho 3.

    (imagem) https://judge.beecrowd.com/pt/problems/view/3392

    Quando os alunos crescem e entram em escolas de nível intermediário, podemos
    dar-lhes o oposto. Dê a eles uma tabela N ∗ N e deixe que eles decidam como
    adicionar rótulos para que seja uma tabela de adição válida (se é de fato uma
    tabela de adição). Dada uma tabela N∗ N, que não inclui nenhum rótulo, seu
    trabalho é decidir se é possível rotulá-la corretamente ou não. Não estamos
    interessados nos próprios rótulos, apenas decidir se é uma tabela de adição
    ou não. Por exemplo, a tabela 2 ∗ 2 à esquerda não é uma tabela de adição,
    enquanto a da direita é.

    (Imagem) https://judge.beecrowd.com/pt/problems/view/3392

    Input
    Seu programa será testado em um ou mais casos de teste. A primeira linha da
    entrada é um inteiro D que representa o número de casos. A primeira linha de
    cada caso de teste é um inteiro N, onde N ≤ 10, representando o tamanho da
    tabela. Em seguida, haverá N linhas, cada uma com N inteiros representando a
    tabela N ∗ N no formato de linha principal. Cada número na tabela está entre
    -10.000 e 10.000 (inclusive).

    Saída
    Para cada caso de teste, exiba o resultado em uma única linha usando o seguinte
    formato:
    KW
    Onde k é o número do caso de teste (começando em 1) e o resultado é "YES" se o
    caso de teste for uma tabela de adição, ou "NO" se não for.
    :return:
    """
    n = int(input())
    caso = 1
    for i in range(n):
        linha = int(input())
        linhas, tabela, temp1 = [], [], []
        # Construindo a matriz para calcular as somas.
        for j in range(linha + 1):
            if j == linha + 1:
                while len(temp1) < linha:
                    temp1.append(0)
                linhas.extend(temp1)
                tabela.append(linhas)
                break
            if j == 0:
                temp1.append('+')
                while len(temp1) < linha + 1:
                    temp1.append(0)
                linhas.extend(temp1)
                tabela.append(linhas)
                linhas = []
                temp1 = []
            else:
                linhas.append(1)
                linhas.extend(list(map(int, input().split())))
                tabela.append(linhas)
                linhas = []
        # Mostrando a matriz básica consturída para montar a matriz soma
        for j in range(len(tabela)):
            for k in range(len(tabela[j])):
                print(f"{tabela[j][k]:>5}", end=' ')
            print()
        tabela2 = deepcopy(tabela) # Fazendo deepcopy para verificação das somas.
        # Acando os primeiros fatores que iram ser somados.
        for j in range(1, len(tabela[0])):
            for k in range(1, len(tabela[j])):
                temp2, temp3 = tabela[j][0], tabela[0][j]
                if temp2 + temp3 == tabela[j][k]:
                    tabela2[j][0] = temp2
                    # print(temp2, temp3, 'OK')
                    break
                while temp2 < 10000:
                    # print(temp2, temp3)
                    if tabela[j][k] > 0:
                        temp2 += 1
                        if temp2 + temp3 == tabela[j][k]:
                            # print(temp2, temp3, 'OK')
                            break
                    if tabela[j][k] < 0:
                        temp2 -= 1
                        if temp2 < -10000:
                            break
                        if temp2 + temp3 == tabela[j][k]:
                            # print(temp2, temp3, 'OK')
                            break
                tabela2[j][0] = temp2
                break
        achados, soma, idx, idx2 = [], [], 0, 0
        # Achando os segundos fatores e verificando validade da matriz soma.
        # Como a ordem dos fatores a serem somados, um vez válido para um resultado, deve valer
        # Para o resto da matriz.
        for j in range(1, len(tabela)):
            a = 1
            for k in range(a, len(tabela[j])):
                temp2, temp3 = tabela2[j][0], tabela2[0][j]
                if tabela[j][k] == temp2 + temp3:
                    if len(achados) < linha:
                        achados.append(temp3)
                    if idx2 > linha - 1:
                        idx2 = 0
                    if temp3 == achados[idx2]:
                        soma.append(True)
                        # print(temp2, temp3, 'OK', achados[idx2], idx2)
                        idx2 += 1
                    else:
                        soma.append(False)
                        break
                if tabela[j][k] != temp2 + temp3:
                    while temp3 < 10000 and k >= 1:
                        if tabela[j][k] < temp2 + temp3:
                            temp3 -= 1
                            if temp2 + temp3 == tabela[j][k]:
                                if len(achados) < linha:
                                    achados.append(temp3)
                                if idx2 > linha - 1:
                                    idx2 = 0
                                if temp3 == achados[idx2]:
                                    soma.append(True)
                                    # print(temp2, temp3, 'OK', achados[idx2], idx2)
                                    idx2 += 1
                                    a += 1
                                    break
                                else:
                                    soma.append(False)
                            if temp3 + temp2 < tabela[j][k] and temp3 != achados[idx2]:
                                soma.append(False)
                                break
                        if tabela[j][k] > temp2 + temp3:
                            temp3 += 1
                            if temp2 + temp3 == tabela[j][k]:
                                if len(achados) < linha:
                                    achados.append(temp3)
                                if idx2 > linha - 1:
                                    idx2 = 0
                                if temp3 == achados[idx2]:
                                    soma.append(True)
                                    # print(temp2, temp3, 'OK', achados[idx2], idx2)
                                    idx2 += 1
                                    a += 1
                                    break
                                else:
                                    soma.append(False)
                                    break
                            if temp3 + temp2 > tabela[j][k] and temp3 != achados[idx2]:
                                soma.append(False)
                                break
                        # print(temp2, temp3, idx2)
                        # print(achados)
                        # print(soma)
                        if False in soma:
                            break
            if False in soma:
                break
        # Caso não seja uma matriz soma.
        if not False in soma:
            print(f"{caso} YES")
            caso += 1
        # Caso seja uma matriz soma.
        if False in soma:
            print(f"{caso} NO")
            caso += 1
        idx, idx2 = 0, 1
        # print(achados)
        # Arranjando os fatores para ser exibida na matriz completa.
        for j in range(0, len(tabela)):
            tabela2[0][idx2] = achados[idx]
            idx += 1
            idx2 += 1
            if idx2 > linha:
                break
        # Exibindo a matriz.
        for j in range(len(tabela2)):
            for k in range(len(tabela2[j])):
                print(f"{tabela2[j][k]:>5}", end=' ')
            print()
        # print(achados)
        # print(soma)
        print()


joao_ainda_nao_consegue_somar()

"""
5
3
4 -1 6
7 2 9
1 -4 3
2
1 4
3 5
2
3 6
2 5
5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 1 19 20
21 22 23 24 25
"""