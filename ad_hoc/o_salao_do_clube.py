def o_salao_do_clube(): 
    """
    O Clube Recreativo de Tinguá está construindo a sua nova sede social.
    Os sócios desejam que o piso do salão da sede seja de tábuas de madeira,
    pois consideram que este é o melhor tipo de piso para os famosos bailes
    do clube. Uma madeireira da região doou uma grande quantidade de tábuas
    de boa qualidade, para serem utilizadas no piso. As tábuas doadas têm
    todas a mesma largura, mas têm comprimentos distintos.

    O piso do salão da sede social é retangular. As tábuas devem ser colocadas
    justapostas, sem que qualquer parte de uma tábua seja sobreposta a outra
    tábua, e devem cobrir todo o piso do salão. Elas devem ser dispostas alinhadas,
    no sentido longitudinal, e todas devem estar no mesmo sentido (ou seja, todas as
    tábuas devem estar paralelas, no sentido longitudinal). Além disso, os sócios não
    querem muitas emendas no piso, e portanto se uma tábua não é longa o bastante para
    cobrir a distãncia entre um lado e outro do salão, ela pode ser emendada a no máximo
    uma outra tábua para completar a distância.

    Há porém uma complicação adicional. O carpinteiro-chefe tem um grande respeito por
    todas as madeiras e prefere não serrar qualquer tábua. Assim, ele deseja saber se
    é possível forrar todo o piso com as tábuas doadas, obedecendo às restrições especificadas;
    caso seja possível, o carpinteiro-chefe deseja ainda saber o menor número de tábuas
    que será necessário utilizar. A figura abaixo ilustra duas possíveis maneiras de forrar
    o piso de um salão com dimensões 4 × 5 metros para um conjunto de dez tábuas doadas,
    com 100 cm de largura, e comprimentos 1, 2, 2, 2, 2, 3, 3, 4, 4 e 5 metros.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de um caso de teste contém
    dois inteiros M e N indicando as dimensões, em metros, do salão (1 ≤ N,M ≤ 104).
    A segunda linha contém um inteiro L, representando a largura das tábuas, em centímetros
    (1 ≤ L ≤ 100). A terceira linha contém um inteiro, K, indicando o número de tábuas doadas
    (1 ≤ K ≤ 105). A quarta linha contém K inteiros Xi, separados por um espaço, cada um
    representando o comprimento, em metros, de uma tábua (1 ≤ Xi ≤ 104 para 1 ≤ i ≤ K). O
    final da entrada é indicado por uma linha que contém apenas dois zeros, separados por um
    espaço em branco.

    Saída
    Para cada um dos casos de teste da entrada, seu programa deve imprimir uma única linha,
    contendo o menor número de tábuas necessário para cobrir todo o piso do salão, obedecendo
    às restrições estabelecidas. Caso não seja possível cobrir todo o piso do salão obedecendo
    às restrições estabelecidas, imprima uma linha com a palavra ‘impossivel’ (letras minúsculas,
    sem acento).
    :return:
    """
    entrada = input().strip().split(" ")
    largura, comprimento = int(entrada[0]), int(entrada[1])
    while largura != 0 and comprimento != 0:
        cont1, cont2, n_tabuas1, n_tabuas2, idx1, idx2, resp1, resp2 = 0, 0, 0, 0, [], [], [], []
        largura_tabua = int(input().strip()) / 100
        doadas = int(input().strip())
        tabuas = list(map(int, input().strip().split(" ")))
        if largura == 1 and comprimento == 1 and largura_tabua == 1:
            if tabuas.count(1) > 0:
                resp1.append(1)
        else:
            for i in range(doadas):
                for k in range(doadas):
                    if i == 0 and k != 0:
                        if tabuas[i] == largura and i not in idx1:
                            cont1 += 1
                            n_tabuas1 += 1
                            idx1.append(i)
                        if tabuas[i] + tabuas[k] == largura and i not in idx1 and k not in idx1:
                            cont1 += 1
                            n_tabuas1 += 2
                            idx1.append(i)
                            idx1.append(k)
                            if cont1 * largura * largura_tabua == largura * comprimento:
                                resp1.append(n_tabuas1)
                                cont1 = 0
                                n_tabuas1 = 0
                                idx1 = []
                    if i == k and i != 0:
                        if tabuas[k] == largura and k not in idx1:
                            cont1 += 1
                            n_tabuas1 += 1
                            idx1.append(k)
                            if cont1 * largura * largura_tabua == largura * comprimento:
                                resp1.append(n_tabuas1)
                                cont1 = 0
                                n_tabuas1 = 0
                                idx1 = []
                    if i != k:
                        if tabuas[k] == largura and k not in idx1:
                            cont1 += 1
                            n_tabuas1 += 1
                            idx1.append(k)
                            if cont1 * largura * largura_tabua == largura * comprimento:
                                resp1.append(n_tabuas1)
                                cont1 = 0
                                n_tabuas1 = 0
                                idx1 = []
                        if tabuas[i] + tabuas[k] == largura and i not in idx1 and k not in idx1:
                            cont1 += 1
                            n_tabuas1 += 2
                            idx1.append(i)
                            idx1.append(k)
                            if cont1 * largura * largura_tabua == largura * comprimento:
                                resp1.append(n_tabuas1)
                                cont1 = 0
                                n_tabuas1 = 0
                                idx1 = []
                for k in range(doadas):
                    if i == 0 and k != 0:
                        if tabuas[i] == comprimento and i not in idx2:
                            cont2 += 1
                            n_tabuas2 += 1
                            idx2.append(i)
                        if tabuas[i] + tabuas[k] == comprimento and i not in idx2 and k not in idx2:
                            cont2 += 1
                            n_tabuas2 += 2
                            idx2.append(i)
                            idx2.append(k)
                            if cont2 * comprimento * largura_tabua == largura * comprimento:
                                resp2.append(n_tabuas2)
                                cont2 = 0
                                n_tabuas2 = 0
                                idx2 = []
                    if i == k and i != 0:
                        if tabuas[k] == comprimento and k not in idx2:
                            cont2 += 1
                            n_tabuas2 += 1
                            idx2.append(k)
                            if cont2 * comprimento * largura_tabua == largura * comprimento:
                                resp2.append(n_tabuas2)
                                cont2 = 0
                                n_tabuas2 = 0
                                idx2 = []
                    if i != k:
                        if tabuas[k] == comprimento and k not in idx2:
                            cont2 += 1
                            n_tabuas2 += 1
                            idx2.append(k)
                            if cont2 * comprimento * largura_tabua == largura * comprimento:
                                resp2.append(n_tabuas2)
                                cont2 = 0
                                n_tabuas2 = 0
                                idx2 = []
                        if tabuas[i] + tabuas[k] == comprimento and i not in idx2 and k not in idx2:
                            cont2 += 1
                            n_tabuas2 += 2
                            idx2.append(i)
                            idx2.append(k)
                            if cont2 * comprimento * largura_tabua == largura * comprimento:
                                resp2.append(n_tabuas2)
                                cont2 = 0
                                n_tabuas2 = 0
                                idx2 = []
        resp1.extend(resp2)
        if len(resp1) == 0:
            print("impossivel")
        else:
            print(min(resp1))
        entrada = input().strip().split(" ")
        largura, comprimento = int(entrada[0]), int(entrada[1])


o_salao_do_clube()
