def laercio():
    """
    Esta função clacula e poem num lista os numeros
    impares e printa como saída, na seguinte ordem,
    o maior impar, o menor ímpar, o segundo maior
    impar, o segundo menor ímpar, o terceiro
    maior impar e o terceiro menor impar e assim
    sucessivamente. A entrada consiste de um inteiro
    N que representa o número de casos testes
    ( 1 < N < 1000 ). Cada caso teste começa com um
    inteiro M, que representa o tamanho da lista
    (0 < M < 100). Seguem M inteiros Mi (0 < Mi < 1000)
    que representam a lista de Laércio. O programa deve
    imprimir a lista ordenada como Laércio requisitou,
    com um espaço entre os valores, pulando uma linha
    a cada caso teste.
    :return:
    """
    cont, lista, lista1, lista2, lista3 = 0, [], [], [], []
    n = int(input())
    while cont < n:
        m = int(input())
        lista = list(map(int, input().split(" ")))
        for i in range(0, len(lista)):
            if lista[i] % 2 == 1:
                lista1.append(lista[i])
        lista1.sort()
        lista2 = lista1[::-1]
        for i in range(0, len(lista2)):
            if len(lista2) % 2 == 1 and len(lista2) == 1:
                lista3.append(lista2[i])
                break
            elif len(lista2) % 2 == 0:
                if i == len(lista2) // 2:
                    break
            elif len(lista2) % 2 == 1:
                if i == (len(lista2) // 2) + 1:
                    lista3.pop()
                    break
            lista3.append(lista2[i])
            lista3.append(lista1[i])
        print(*lista3)
        lista1 = []
        lista2 = []
        lista3 = []
        cont += 1


laercio()
