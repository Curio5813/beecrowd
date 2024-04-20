def desafio_g():
    quinhao, ancestralidade, cont = [], [], 0
    n, k = map(int, input().split(" "))
    quinhao = list(map(int, input().split(" ")))
    ancestralidade = list(map(int, input().split(" ")))
    print(ancestralidade)
    print(quinhao)
    for i in range(0, len(ancestralidade)):
        if i >= len(ancestralidade) - 1:
            break
        if ancestralidade[i + 1] - ancestralidade[i] <= 0 or \
                abs(ancestralidade[i + 1] - ancestralidade[i]) >= 2:
            cont += quinhao[i]
            print(ancestralidade[i])
            # print(quinhao[i + 1])
    print(cont)


desafio_g()
