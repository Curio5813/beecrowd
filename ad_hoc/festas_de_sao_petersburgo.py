from collections import defaultdict


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
        try:
            comunidade, festa, amigos, temp, cont, amizades = (
                [], [], [], [], 0, defaultdict(list))
            pessoas, relacoes, minimo = map(int, input().split(" "))
            for i in range(1, pessoas + 1):
                comunidade.append(i)

            for i in range(relacoes):
                par = list(map(int, input().split(" ")))
                amigos.append(par)
            n, j = 0, 0
            while n < len(comunidade):
                for j in range(0, len(amigos)):
                    if comunidade[n] == amigos[j][0] and amigos[j][1] not in amizades[comunidade[n]]:
                        amizades[comunidade[n]].append(amigos[j][1])
                        cont += 1
                    elif comunidade[n] == amigos[j][1] and amigos[j][0] not in amizades[comunidade[n]]:
                        amizades[comunidade[n]].append(amigos[j][0])
                        cont += 1
                amizades[comunidade[n]].append(str(cont))
                n += 1
                cont = 0
            amizades = dict(amizades)
            print(amizades)
            convidados, atende = [], True
            chaves = sorted(amizades.keys())
            for k, v in amizades.items():
                if int(amizades[k][-1]) < minimo:
                    atende = False
                else:
                    atende = True
                    break
            if not atende:
                print(0)
            else:
                for i in range(len(chaves) - 1):
                    k = chaves[i]
                    prox = chaves[i + 1]
                    if set(amizades[k]) & set(amizades[prox]):
                        convidados.append(k)
            print(*convidados)
        except EOFError:
            break


festas_de_sao_petersburgo()


"""
6 6 2
1 3
3 5
2 3
2 4
4 6
6 2
"""
