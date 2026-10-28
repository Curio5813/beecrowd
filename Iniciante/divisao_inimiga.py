def divisao_inimiga():
    """
    O capitão Keram tem que tomar uma decisão difícil. É o ano de 2147 e há uma grande guerra no mundo.
    Seus soldados estão juntos desde o início da guerra, há dois anos, e alguns deles se tornaram
    inimigos. Felizmente, cada soldado tem no máximo 3 inimigos.

    Eles precisam atacar outro país em breve, e Keram teme que os soldados inimigos possam não cooperar
    bem durante a batalha. Ele decidiu dividi-los em grupos de forma que cada soldado tenha no máximo
    um inimigo em seu grupo. Ele também quer simplificar, então quer usar o mínimo de grupos possível.
    Você pode dividir os soldados em grupos para ele?
    Entrada

    Na primeira linha existem dois inteiros n e m, 2 ≤ n ≤ 100 000,0 ≤ m ≤ 3n / 2, onde n é o número
    de soldados e m é o número de pares de inimigos. Em seguida, seguem m linhas, cada uma contendo
    dois inteiros separados por espaço ai, bi, denotando que os soldados ai e bi são inimigos, onde
    1 ≤ ai <bi ≤ n. Você pode assumir que todos os soldados têm no máximo 3 inimigos.
    Saída

    A primeira linha de saída contém o número mínimo de grupos de soldados k. Cada uma das próximas k
    linhas contém uma lista separada por espaços de soldados em um grupo único.

    :return:
    """
    entrada = list(map(int, input().split(" ")))
    n, m = entrada[0], entrada[1]
    inimigos, grupos, podem, nao_podem  = [], [], [], []
    for i in range(m):
        entrada2 = list(map(int, input().split(" ")))
        inimigos.append(entrada2)
    for k in range(1, n + 1):
       for i in range(0, len(inimigos)):
           for j in range(0, len(inimigos[i])):
               if k in inimigos[i]:
                   if inimigos[i][0] != k:
                       nao_podem.append(inimigos[i][0])
                   else:
                       nao_podem.append(inimigos[i][1])
       for i in range(1, n + 1):
           if i not in nao_podem and i != k:
               podem.append(k)
               podem.append(i)
               break
       podem.sort()
       if podem not in grupos:
            grupos.append(podem)
       podem = []
       nao_podem = []
    print(grupos)
    print(len(grupos))
    for i in range(0, len(grupos)):
        print(*grupos[i])



divisao_inimiga()
