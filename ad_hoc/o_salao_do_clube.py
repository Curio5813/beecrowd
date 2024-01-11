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
    entr = input().split(" ")
    larg, comp = int(entr[0]), int(entr[1])
    while larg != 0 and comp != 0:
        cont1, cont2, tabuas1, tabuas2 = 0, 0, 0, 0
        larg_tab = int(input())
        doadas = int(input())
        tabs_string = input().split(" ")
        tabs_int = [int(tabua) for tabua in tabs_string]
        tabs_int.sort()
        tabs_int.reverse()
        temp_tabs = tabs_int.copy()
        k = len(tabs_int) - 1
        # Laço no sentido do comprimento.
        for i in range(0, len(temp_tabs)):
            if cont1 * larg_tab == larg * comp * larg_tab:
                break
            while k >= 0:
                if temp_tabs[i] > comp:
                    break
                elif temp_tabs[i] == comp:
                    cont1 += temp_tabs[i]
                    tabuas1 += 1
                    temp_tabs[i] = 0
                    break
                elif temp_tabs[i] < comp:
                    temp = temp_tabs[i] + temp_tabs[k]
                    if temp > comp or i == k:
                        break
                    elif temp == comp:
                        cont1 += temp
                        tabuas1 += 2
                        temp_tabs[i] = 0
                        temp_tabs[k] = 0
                        k -= 1
                        break
                    elif temp < comp:
                        k -= 1
                        break
        # Laço no sentido da largura.
        k = len(tabs_int) - 1
        temp_tabs = tabs_int.copy()
        for i in range(0, len(temp_tabs)):
            if cont2 * larg_tab == larg * comp * larg_tab:
                break
            while k >= 0:
                if temp_tabs[i] > larg:
                    break
                elif temp_tabs[i] == larg:
                    cont2 += temp_tabs[i]
                    tabuas2 += 1
                    temp_tabs[i] = 0
                    break
                elif temp_tabs[i] < larg:
                    temp = temp_tabs[i] + temp_tabs[k]
                    if temp > larg or i == k:
                        break
                    elif temp == larg:
                        cont2 += temp
                        tabuas2 += 2
                        temp_tabs[i] = 0
                        temp_tabs[k] = 0
                        k -= 1
                        break
                    elif temp < larg:
                        k -= 1
                        break
        if cont1 * larg_tab == larg * comp * larg_tab and cont2 * larg_tab == larg * comp * larg_tab:
            if tabuas1 <= tabuas2:
                print(tabuas1)
        elif cont1 * larg_tab == larg * comp * larg_tab and cont2 * larg_tab == larg * comp * larg_tab:
            if tabuas1 > tabuas2:
                print(tabuas2)
        elif cont1 * larg_tab == larg * comp * larg_tab and cont2 * larg_tab != larg * comp * larg_tab:
            print(tabuas1)
        elif cont1 * larg_tab != larg * comp * larg_tab and cont2 * larg_tab == larg * comp * larg_tab:
            print(tabuas2)
        elif cont1 * larg_tab != larg * comp * larg_tab and cont2 * larg_tab != larg * comp * larg_tab:
            print("impossivel")
        entr = input().split(" ")
        larg, comp = int(entr[0]), int(entr[1])


o_salao_do_clube()
