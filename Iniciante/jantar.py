from collections import Counter


def jantar():
    """
    Esta função calcula o menor ano que um grupo de pessoas podem se reunir
    para um jantar, divididos em 2 grupos, onde os 2 grupos formam a
    totalidade das pessoas que irão jantar, um dos grupos por aqueles que
    se econtram pela primeira vez, e o segundo que já haviam se encontrado.
    Cada grupo não pode ser maior que 2/3, sendo o outro de 1/3, neste caso,
    mas nada impede que pode ser metade/metade, ou qualquer outra fração que
    não supere 2/3, uma delas. A entrada consiste num número 4 <= N <= 400,
    que é o número de participantes, C linhas são no formato A B Y, que
    representa os participantes A e B (1 ≤ A < B ≤ N) que se encontraram pela
    primeira vez no ano Y (1948 ≤ Y < 2008). Nenhum par de participantes vai
    aparecer mais de uma vez na lista, e presume-se que cada par de participantes
    que não estejam na lista se reuniu apenas agora (no ano de 2008). Para cada
    caso de teste, imprima o menor ano Y, de modo que seja possível dividir os
    participantes em duas partes, onde nenhum dos quais contém mais de 2N/3
    pessoas, de forma que todos da primeira parte se encontrou pela primeira
    vez antes do ano Y, e todas as pessoas da segunda parte se encontraram pela
    primeira vez no ano Y ou depois. Se não houver esse ano, imprima a string
    “Impossible”.
    :return:
    """
    n, c = map(int, input().split(" "))
    years, meet, menor, bol = [], [], 2009, True
    for i in range(c):
        a, b, y = list(map(int, input().split(" ")))


jantar()
