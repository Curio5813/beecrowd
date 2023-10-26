from collections import Counter


def senhores_da_guerra_galacticos():
    """
    Esta função calcula a equação da reta, dado pontos no
    plano cartesiano, e verifica, se é preciso ou não adionar
    mais retas para a divisão do espaço pretendido. A primeira
    linha de entrada contém dois inteiros positivos W e N,
    (1 ≤ W, N ≤ 100) denotando o número de senhores da guerra e
    o número de linhas na divisão de espaço sugerida. Ela é seguida
    por N linhas, cada uma contendo quatro inteiros x1, y1 , x2 e y2,
    cada um com um valor absoluto não superior a 10.000. Isso
    significa que uma linha está cruzando os dois pontos (x1, y1) e
    (x2, y2) no mapa galáctico. Esses dois pontos não serão iguais.
    A saida imprima o número de linhas que você terá que adicionar a
    esta sugestão para satisfazer a divisão do espaço pretendida.
    :return:
    """
    w, n = map(int, input().split(" "))
    reta, retas, equal, diff, cont, qts, linhas = [], [], 0, 0, 0, [], 0
    for i in range(n):
        p = list(map(int, input().split(" ")))
        if p[2] - p[0] != 0:
            m = (p[3] - p[1]) / (p[2] - p[0])  # Calcula o coeficiente angular da reta;
            reta.append(m)
            b = p[1] - m * p[0]  # Calcula o ponto de intersecção da reta ao eixo Y, quando x = 0
            reta.append(b)       # Caso a reta seja paralela ao eixo x, m = 0 e y = b
        elif p[2] == 0 and p[0] == 0:   # Caso X1 = 0 e  X2 = 0, a reta será conicidente com o eixo y
            reta.append(0)
            reta.append(0)
        retas.append(reta)
        reta = []
    for i in range(0, len(retas)):
        qt1 = retas.count(retas[i])
        qts.append(qt1)
    xy = dict(Counter(qts))
    for k, v in xy.items():
        if k == 1:
            cont += v
        elif k == v:
            cont += 1
        elif k != v:
            cont += v // k
    linhas = n - cont
    print(linhas)


senhores_da_guerra_galacticos()
