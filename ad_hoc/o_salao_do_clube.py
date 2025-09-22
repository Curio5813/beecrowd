from copy import deepcopy


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
    comprimento1, comprimento2 = 1, 1
    while comprimento1 != 0 and comprimento2 != 0:
        entrada = input().strip().split(" ")
        comprimento1, comprimento2 = int(entrada[0]), int(entrada[1])
        area_salao = comprimento1 * comprimento2
        largura = int(input().strip())
        qt_tabuas = int(input())
        if (comprimento1 * comprimento2 * 100) % largura != 0:
            print("impossivel")
        else:
            numero_tabuas, soma, idx, caso1, respostas = 0, 0, 0, False, []
            tabuas = list(map(int, input().split(" ")))
            if sum(tabuas) < area_salao:
                print("impossivel")
            else:
                tabuas.sort()
                invertidas = deepcopy(tabuas)
                invertidas.reverse()
                for i in range(0, len(invertidas)):
                    for j in range(idx, len(tabuas)):
                        if i == 0 and invertidas[i] == comprimento2:
                            numero_tabuas += 1
                            soma += invertidas[i]
                            if soma == area_salao:
                                respostas.append(numero_tabuas)
                                caso1 = True
                                break
                            break
                        elif invertidas[i] == comprimento1:
                            numero_tabuas += 1
                            soma += invertidas[i]
                            if soma == area_salao:
                                respostas.append(numero_tabuas)
                                caso1 = True
                                break
                            idx = j + 1
                            break
                        elif invertidas[i] + tabuas[j] == comprimento1:
                            numero_tabuas += 2
                            soma += invertidas[i] + tabuas[j]
                            if soma == area_salao:
                                respostas.append(numero_tabuas)
                                caso1 = True
                                break
                            idx = j + 1
                        else:
                            break
                    if caso1:
                        break
                numero_tabuas, soma, idx, caso1 = 0, 0, 0, False
                for i in range(0, len(invertidas)):
                    for j in range(idx, len(tabuas)):
                        if i == 0 and invertidas[i] == comprimento2:
                            numero_tabuas += 1
                            soma += invertidas[i]
                            if soma == area_salao:
                                respostas.append(numero_tabuas)
                                caso1 = True
                                break
                            break
                        elif invertidas[i] == comprimento2:
                            numero_tabuas += 1
                            soma += invertidas[i]
                            if soma == area_salao:
                                respostas.append(numero_tabuas)
                                caso1 = True
                                break
                            idx = j + 1
                            break
                        elif invertidas[i] + tabuas[j] == comprimento2:
                            numero_tabuas += 2
                            soma += invertidas[i] + tabuas[j]
                            if soma == area_salao:
                                respostas.append(numero_tabuas)
                                caso1 = True
                                break
                            idx = j + 1
                            break
                        else:
                            break
                    if caso1:
                        break
                if caso1:
                    print(min(respostas))
                if not caso1:
                    print("impossivel")


o_salao_do_clube()
