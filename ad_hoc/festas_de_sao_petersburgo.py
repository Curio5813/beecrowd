def festas_de_sao_petersburgo():
    """
    São Petersburgo tornou-se após o fim da cortina de ferro, no
    início dos anos 90, uma das principais cidades da cena alternativa
    em todo o mundo. Grupos de punks, diversas bandas de hardcore
    e outros representantes da cena alternativa mudaram-se para a
    cidade, atraídas pela grande quantidade de jovens. Com o surgimento
    das comunidades virtuais, alguns anos mais tarde, notou-se o enorme
    potencial do uso destas comunidades para combinar encontros,
    festas, raves, etc.

    Nestas festas de São Petersburgo é sempre muito importante que cada
    um dos participantes tenha pelo menos um certo número de amigos na
    rede social. E, ao mesmo tempo, desejamos convidar o maior número
    possível de pessoas de São Petersburgo desde que a restrição com
    relação ao número de amigos seja satisfeita. Tal restrição diz que,
    para ser convidada a festa, a pessoa precisa ter pelo menos um número
    K de amigos na lista de convidados.

    Sua tarefa neste problema é, dado o conjunto de pessoas da comunidade
    e a lista de suas relações, determinar quais devem ser chamadas para
    que a festa tenha a maior quantidade possível de participantes satisfazendo
    a restrição.

    Entrada
    A entrada é composta por diversas instâncias e termina com final de arquivo
    (EOF). A primeira linha de cada instância contém três inteiros N (1 ≤ N ≤ 1000),
    M e K (O ≤ K ≤ N) representando respectivamente o número de pessoas na comunidade,
    o número de relações de amizade nessa comunidade e o número mínimo de amigos
    convidados uma pessoa precisa ter para ser convidada. Cada pessoa da comunidade
    é identificada por números de 1 a N. Cada uma das próximas M linhas contém um par
    de pessoas indicando que elas são amigas na rede social.

    Saída
    Para cada instância imprima uma única linha contendo a lista das pessoas a serem
    convidadas separadas por um espaço em branco. A lista deve estar ordenada em ordem
    crescente. Caso ninguém possa ser convidado, imprima o número 0.
    :return:
    """
    while True:
        festa, convidados, par, pares = {}, [], [], []
        try:
            n, m, k = map(int, input().split(" "))
            for i in range(1, n + 1):
                festa[i] = 0
            for i in range(m):
                conv, amigo = map(int, input().split(" "))
                festa[conv] += 1
                festa[conv] += festa[amigo]
                par.append(conv)
                par.append(amigo)
                pares.append(par)
                par = []
            for i in range(0, len(pares)):
                keys1 = pares[i][0]
                keys2 = pares[i][1]
                if festa[keys2] > 1:
                    festa[keys1] += 1
            for keys in festa.keys():
                if festa[keys] >= k:
                    convidados.append(keys)
            convidados.sort()
            if len(convidados) > 0:
                print(*convidados)
            else:
                print(0)
        except EOFError:
            break


festas_de_sao_petersburgo()
