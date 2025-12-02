def mega_inversoes():
    """
    O limite superior de n2 para qualquer algoritmo de classificação
    é fácil de obter: basta pegar dois elementos que estão deslocados
    um em relação ao outro e trocá-los. Conrad concebeu um algoritmo que
    prossegue pegando não dois, mas três elementos mal colocados. Ou seja,
    pegue três elementos ai > aj > ak com i < j < k e coloque-os na ordem
    ak, aj, ai. Agora, se para o algoritmo original as etapas são limitadas
    pelo número máximo de inversões (n * (n - 1)) / 2, Conrad está perdendo
    o juízo quanto ao limite superior para tais triplos em uma dada sequência.
    Ele pede que você escreva um programa que conte o número desses triplos.

    Entrada
    A primeira linha da entrada é o comprimento da sequência, 1 ≤ n ≤ 105. A próxima
    linha contém a sequência inteira a1, a2,. . . , an. Você pode assumir que todos
    ai ∈ [1, n].

    Saída
    Imprima o número de triplas invertidos.
    :return:
    """
    n = int(input())
    lista = list(map(int, input().split()))
    cont = 0
    for j in range(1, n - 1):
        maiores = 0
        menores = 0
        for i in range(j):
            if lista[i] > lista[j]:
                maiores += 1
        for k in range(j + 1, n):
            if lista[j] > lista[k]:
                menores += 1
        cont += maiores * menores
    print(cont)


if __name__ == '__main__':
    mega_inversoes()

"""
3
1 2 3
4
3 3 2 1
"""