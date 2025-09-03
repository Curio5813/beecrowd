from copy import deepcopy

def cubos_coloridos():
    """
    Crianças adoram brincar com pequenos cubos. Elas passam horas
    criando ‘casas’, ‘prédios’, etc. O irmãozinho de Tomaz acabou
    de ganhar um conjunto de blocos coloridos no seu aniversário.
    Cada face de cada cubo é de uma cor.

    Como Tomaz é uma criança muito analítica, ele decidiu descobrir
    quantos “tipos” diferentes de cubos o seu irmãozinho ganhou. Você
    pode ajuda-lo? Dois cubos são considerados do mesmo tipo se for
    possível rotacionar um deles de forma que as cores nas faces
    respectivas dos dois blocos sejam iguais.

    Entrada
    A entrada contém vários casos de teste. A primeira linha do caso de
    teste contém um inteiro N especificando o número de cubos no conjunto
    (1 ≤ N ≤ 1000). As próximas 3 x N linhas descrevem os cubos do conjunto.
    Na descrição as cores serão identificadas pelos números de 0 a 9. A
    descrição de cada cubo será dada em três linhas mostrando as cores das
    seis faces do cubo “aberto”, no formato dado no exemplo abaixo. No exemplo
    abaixo, as faces do cubo tem cores de 1 a 6, a face com cor 1 está no
    lado oposto da face com a cor 3, e a face com cor 2 é vizinha das faces
    1, 3, 4 e 6, e está no lado oposto da face com cor 5.

    1
    2 4 5 6
    3

    O final da entrada é indicado por N = 0.

    Saída
    Para cada caso de teste seu programa deve imprimir uma linha contendo um único
    inteiro, correspondente ao numero de tipos de cubos no conjunto dado.
    :return:
    """
    n = int(input())
    while n != 0:
        cubos = []
        for i in range(n):
            primeiro_ultimo, opostos1, opostos2, temp = [], [], [], []
            pirmeiro = int(input())
            linha = list(map(int, input().strip().split(" ")))
            ultimo = int(input())
            primeiro_ultimo.append(pirmeiro)
            primeiro_ultimo.append(ultimo)
            opostos1.append(primeiro_ultimo)
            reverso = deepcopy(primeiro_ultimo)
            reverso.reverse()
            opostos2.append(reverso)
            temp = [linha[0], linha[2]]
            opostos1.append(temp)
            opostos2.append(temp)
            temp = [linha[1], linha[3]]
            opostos1.append(temp)
            opostos2.append(temp)
            temp = [opostos1, opostos2]
            cubos.append(temp)
        diferentes, flag = 0, 0
        for i in range(len(cubos)):
            prox = (i + 1) % len(cubos)
            flag = 1
            for k in range(i + 1, len(cubos)):
                igual = True
                for j in range(len(cubos[i][0])):  # percorre pares de faces
                    if cubos[i][0][j] not in cubos[k][0] and cubos[i][0][j] not in cubos[k][1]:
                        print(cubos[i][0][j], cubos[k][0], cubos[k][1])
                        igual = False
                if igual:
                    flag = 0
            if flag == 1:
                diferentes += 1
        print(diferentes)
        n = int(input())


cubos_coloridos()
