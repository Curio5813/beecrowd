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
        for j in range(len(tabela)):
            for k in range(len(tabela[j])):
                print(f"{tabela[j][k]:>5}", end=' ')
            print()
        flag, soma, temp2, temp3, a = False, [], 0, 0, 1
        tabela2 = deepcopy(tabela)
        for j in range(1, len(tabela[0])):
            for k in range(1, len(tabela[j])):
                temp2, temp3 = tabela[j][0], tabela[0][j]
                # print(temp2, temp3)
                if temp2 + temp3 == tabela[j][k]:
                    tabela2[j][0] = temp2
                    break
                while temp2 < 10000:
                    # print(temp2, temp3)
                    if tabela[j][k] > 0:
                        temp2 += 1
                        if temp2 + temp3 == tabela[j][k]:
                            flag = True
                            break
                    if tabela[j][k] < 0:
                        temp2 -= 1
                        if temp2 < -10000:
                            break
                        if temp2 + temp3 == tabela[j][k]:
                            flag = True
                            break
                soma.append(flag)
                tabela2[j][0] = temp2
                break
            a += 1
            for k in range(a, len(tabela[j])):
                temp2, temp3 = tabela2[j][0], tabela2[0][j]
                # print(temp2, temp3)
                if k == 1:
                    continue
                if temp2 + temp3 == tabela[j][k]:
                    tabela2[0][j] = temp3
                    break
                while temp3 < 10000 and k >= 1:
                    # print(temp2, temp3)
                    if tabela[j][k] > temp2 + temp3:
                        temp3 += 1
                        if temp2 + temp3 == tabela[j][k]:
                            flag = True
                            break
                    if tabela[j][k] < temp2 + temp3:
                        temp3 -= 1
                        if temp3 < -10000:
                            break
                        if temp2 + temp3 == tabela[j][k]:
                            flag = True
                            break
                soma.append(flag)
                tabela2[0][j + 1] = temp3
                break
        if len(soma) == len(tabela2):
            print(f"{caso}. YES")
            caso += 1
        if len(soma) != len(tabela2):
            print(f"{caso}. NO")
            caso += 1
        for j in range(len(tabela2)):
            for k in range(len(tabela2[j])):
                print(f"{tabela2[j][k]:>5}", end=' ')
            print()
        # print(soma)
        print()


joao_ainda_nao_consegue_somar()

"""
3
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
"""