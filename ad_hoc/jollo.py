def jollo():
    """
    Jollo é um simples jogo de cartas que as crianças da Logônia
    adoram jogar. É um jogo entre dois jogadores usando um baralho
    normal de 52 cartas. No jogo, as cartas são ordenadas de acordo
    com seu valor e naipe, produzindo uma sequência de 52 valores
    distintos.

    O jogo é composto de três turnos, jogados em uma série melhor de
    três (um jogador deve ganhar dois turnos para ganhar o jogo). No
    início do jogo, o baralho é embaralhado e cada jogador recebe três
    cartas. Em cada turno, os jogadores mostram uma carta ao adversário
    e o jogador com a carta mais alta ganha o turno. As cartas usadas
    no turno são descartadas (ou seja, não podem ser usadas novamente).

    O filho do Rei adora jogar este jogo, mas ele não é muito esperto,
    perdendo frequentemente para sua irmã mais nova. E quando perde, ele
    chora tão alto que ninguém aguenta escutar. O criado que embaralha
    as cartas para o Príncipe e sua irmã tem medo de ser mandado para a
    prisão caso o Príncipe continue perdendo. O criado pode ver as cartas
    que ele entrega, e após distribuir cinco cartas (três à Princesa e duas
    ao Príncipe) quer saber qual a carta mais baixa que ele deve entregar
    ao Príncipe tal que não exista nenhuma possibilidade de ele perder o
    jogo, não importando a maneira como jogue.

    Entrada
    Cada caso de teste é dado em uma única linha que contém cinco inteiros
    distintos A, B, C, X e Y, descrevendo as cartas já distribuídas aos jogadores.
    As primeiras três cartas são dadas à Princesa (1 ≤ A,B,C ≤ 52) e as últimas
    duas cartas são dadas ao Príncipe (1 ≤ X,Y ≤ 52).

    O último caso de teste é seguido de uma linha contendo cinco zeros.

    Saída
    Para cada caso de teste, imprima uma única linha. Se existe uma carta que fará
    o Príncipe ganhar independente do modo como jogar, você deve imprimir a menor
    carta possível. Caso contrário, imprima -1.
    :return:
    """
    while True:
        a, b, c, x, y = map(int, input().split(" "))
        cartas, princesa, principe, vitoria, cont = [], [], [], 0, 0
        princesa.append(a)
        princesa.append(b)
        princesa.append(c)
        principe.append(x)
        principe.append(y)
        princesa.sort()
        principe.sort()
        if a == b == c == x == y == 0:
            break
        else:
            for i in range(1, 52 + 1):
                if i != a and i != b and i != c and i != x and i != y:
                    cartas.append(i)
            for i in range(0, len(principe)):
                if max(principe) < min(princesa):
                    print(-1)
                    break
                elif max(principe) < max(princesa) and min(principe) < min(princesa):
                    print(-1)
                    break
                elif max(principe) < max(princesa) and min(principe) < princesa[1]:
                    print(-1)
                    break
                elif min(principe) > max(princesa):
                    for k in range(53):
                        if k not in princesa and k not in principe and k in cartas:
                            print(k)
                            cont = 1
                            break
                elif max(principe) > max(princesa) and min(principe) < min(princesa):
                    k = max(princesa)
                    for k in range(k, 53):
                        if k not in princesa and k not in principe and k in cartas:
                            print(k)
                            cont = 1
                            break
                elif max(principe) > max(princesa) and min(princesa) < min(principe) < princesa[1]:
                    k = max(princesa)
                    for k in range(k, 53):
                        if k not in princesa and k not in principe and k in cartas:
                            print(k)
                            cont = 1
                            break
                elif max(principe) > max(princesa) and min(princesa) < min(principe) \
                        and min(principe) > princesa[1]:
                    k = princesa[1]
                    for k in range(k, 53):
                        if k not in princesa and k not in principe and k in cartas:
                            print(k)
                            cont = 1
                            break
                elif max(principe) < max(princesa) and min(principe) > min(princesa):
                    k = princesa[1]
                    for k in range(k, 53):
                        if k not in princesa and k not in principe and k in cartas:
                            print(k)
                            cont = 1
                            break
                elif max(principe) > min(princesa) and min(principe) > max(princesa):
                    k = min(princesa)
                    for k in range(k, 53):
                        if k not in princesa and k not in principe and k in cartas:
                            cont = 1
                            break
                elif max(principe) > min(princesa) and min(principe) < max(princesa):
                    k = princesa[1]
                    for k in range(k, 53):
                        if k not in princesa and k not in principe and k in cartas:
                            print(k)
                            cont = 1
                            break
                if cont == 1:
                    break
            else:
                print(-1)


jollo()
