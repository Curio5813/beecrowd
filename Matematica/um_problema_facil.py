from csv import reader


def um_problema_facil():
    """
    Esta função recebe um valor de entrada, calcula e imprime
    a base mínima numérica para o valor dado.
    :return:
    """
    arq = open("teste01.csv")
    lista = list(reader(arq, delimiter=" "))
    l1 = []
    for i in range(0, len(lista)):
        for k in range(0, len(lista[i])):
            l1.append(lista[i][k])
    n = input()
    base = []
    for i in n:
        for k in range(0, len(l1)):
            if i in l1[k]:
                if i == "0" or i == "1":
                    print(2)
                else:
                    base.append(l1.index(l1[k]) + 1)
    print(max(base))


um_problema_facil()
