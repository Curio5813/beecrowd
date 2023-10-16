def as_frutas_esquecidas():
    """
    Dados os nomes de frutas e um conjunto de palavras cifradas
    saber se o persogem do problema, Sheldon Cooper, comeu ou
    detesta tal fruta, caso elas apareçam no conjunto das palafras cifradas.
    A entrada, primeira linha contém dois inteiros: 1) N que representa
    a quantidade de nomes de frutas que será verificado/procurado, limitado
    por [1,100]; 2) M que representa a quantidade de linhas da lista de nomes
    das frutas, limitado por [15,500]; Além disso, cada linha M da lista d
    e nomes e cada linha N com o nome de fruta seguem o limite: [4,100].
    A saída deve printar, para cada nome de fruta procurado: “Sheldon come
    a fruta X” ou “Sheldon detesta a fruta X” (onde X é nome da fruta que
    foi verificada na lista em lowercase).
    :return:
    """
    n, m = map(int, input().split(" "))
    frutas, cifragens, comeu, detesta, cont, qt1, qt2, bol = [], [], [], [], 0, 0, 0, 1
    for i in range(n):
        fruta = input().lower()
        frutas.append(fruta)
    for i in range(m):
        cifragem = input().lower()
        cifragens.append(cifragem)
    for i in range(0, len(frutas)):
        while cont < m:
            qt1 = cifragens[cont].count(frutas[i])
            qt2 = cifragens[cont].count((frutas[i][::-1]))
            if qt1 > 0 or qt2 > 0:
                print(f"Sheldon come a fruta {frutas[i]}")
                break
            cont += 1
        else:
            if cont >= m:
                print(f"Sheldon detesta a fruta {frutas[i]}")
        cont = 0


as_frutas_esquecidas()
