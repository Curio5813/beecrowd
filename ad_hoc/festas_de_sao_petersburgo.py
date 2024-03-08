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
        festa, par, pares, amigos, amigo, sigma, sigmas = [], [], [], [], 0, [], []
        try:
            n, m, k = map(int, input().split(" "))
            for i in range(1, n + 1):
                festa.append(i)
            print(festa)
            for i in range(m):
                par = list(map(int, input().split(" ")))
                pares.append(par)
            print(pares)
            for i in range(0, len(festa)):
                for k in range(0, len(pares)):
                    if festa[i] == pares[k][0]:
                        amigo += 1
                        sigma.append(pares[k][1])
                amigos.append(amigo)
                amigo = 0
                sigmas.append(sigma)
                sigma = []
            print(amigos)
            print(sigmas)
        except EOFError:
            break


festas_de_sao_petersburgo()
