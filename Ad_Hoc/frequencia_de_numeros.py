import collections


def frequencia_de_numeros():
    """
    Esta função retorna o numero de vezes que um determinado
    numero aparece, em ordem crescente, na sequencia de números
    dados como entrada.
    :return:
    """
    n = int(input())
    l1 = []
    for i in range(n):
        num = int(input())
        l1.append(num)
    colecao = dict(collections.Counter(l1))
    dict_ordered = collections.OrderedDict(sorted(colecao.items()))
    d = dict(dict_ordered)
    for k, v in d.items():
        print(f"{k} aparece {v} vez(es)")


frequencia_de_numeros()
