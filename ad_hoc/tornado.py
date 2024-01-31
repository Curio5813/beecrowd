def tornado():
    """
    É este tempo louco o resultado da interferência contínua da
    humanidade no meio ambiente? Ou é simplesmente o ciclo normal
    das mudanças climáticas através dos tempos? Ninguém parece
    saber ao certo, mas o fato é que os fenômenos naturais, como
    tornados e furacões atingem nosso país com mais força e freqüência
    do que nas décadas passadas.

    Um tornado acaba de atingir a fazenda Silverado, produtora de
    gado e de leite, e fez estragos. O telhado do celeiro foi rasgado,
    várias árvores foram arrancadas, o caminhão da fazenda foi derrubado...
    Mas o pior é que o tornado destruiu várias seções da cerca que rodeava
    a propriedade. A cerca foi muito bem construída, com postes de
    concreto a cada dois metros, e arame farpado encerrando o perímetro
    de toda a fazenda (o perímetro, em metros, é um número par, o que torna
    a cerca perfeitamente regular).

    Agora vários postes estão quebrados ou faltando, e há falhas na cerca.
    Para evitar que o gado fique de fora da propriedade, a cerca deve ser
    restaurada o mais rápido possível. Reconstruindo o muro à sua forma
    original, com postes de concreto, vai levar um longo tempo. Enquanto
    isso, os proprietários da fazenda decidiram fechar as lacunas com uma
    cerca temporária, feita com postes de madeira. Postes de madeira serão
    colocados exatamente nos mesmos pontos onde os postes estão faltando ou
    foram quebrados. No entanto, a fim de tornar a reconstrução temporária
    mais rápida e menos dispendiosa, os donos decidiram utilizar menos postes:
    um poste de madeira será utilizado para substituir um poste de concreto
    ausente / quebrado somente se o comprimento do arame farpado necessário
    para fechar a distância até o próximo poste (de madeira ou concreto) for
    superior a quatro metros.

    Dada a descrição de quantos postes estão quebrados ou faltando, você deve
    escrever um programa que determine a menor quantidade de postes de madeira
    que são necessários para fechar as lacunas da cerca, de acordo com a decisão
    dos proprietários.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de um caso de teste
    contém um N indicando o número original de postes de concreto da cerca(5 ≤ N ≤ 5000).
    A segunda linha de um caso de teste irá conter N inteiros Xi indicando o estado
    de cada poste de concreto após a passagem do tornado (0 ≤ Xi ≤ 1 para 1 ≤ i ≤ N).
    Se Xi = 1 o poste i esté em boas condições, se Xi = 0 o poste i está quebrado ou
    faltando. Note que o poste N é ao lado do poste 1. O final da entrada é indicado
    por N = 0 .

    Saída
    Para cada caso de teste da entrada seu programa deve produzir uma linha de saída,
    contendo um inteiro indicando o menor número de postes de madeira que são necessários
    para restaurar o muro, de acordo com a decisão dos proprietários.
    :return:
    """
    n = int(input())
    while n != 0:
        i, cont1, cont2 = 0, 0, 0
        cerca = list(map(int, input().split(" ")))
        for k in range(len(cerca) - 1, 0, -1):
            if cerca[k] == 1:
                break
            if cerca[k] == 0:
                cont1 += 1
        if cont1 % 2 == 0:
            while i < len(cerca):
                if i == len(cerca) - 1:
                    break
                if cerca[0] == 0 and cerca[-1] == 0:
                    cerca[-1] = 1
                    cont2 += 1
                else:
                    if cerca[i] == 0 and cerca[i + 1] == 0:
                        cerca[i + 1] = 1
                        i += 1
                        cont2 += 1
                    else:
                        i += 1
        if cont1 % 2 != 0:
            while i < len(cerca):
                if i == len(cerca) - 1:
                    break
                if cerca[0] == 0 and cerca[-1] == 0:
                    cerca[0] = 1
                    cont2 += 1
                else:
                    if cerca[i] == 0 and cerca[i + 1] == 0:
                        cerca[i + 1] = 1
                        i += 1
                        cont2 += 1
                    else:
                        i += 1
        print(cont2)
        n = int(input())


tornado()
