def companheiros_de_exercito():
    """
    Nlogonia está lutando uma guerra implacável contra seu país
    vizinho Cubicônia. O General Chefe do Exército da Nlogônia
    decidiu atacar o inimigo com uma formação linear de soldados,
    que avançariam juntos até conquistar o país vizinho. Antes de
    lutar, o General Chefe ordenou que cada soldado na linha de
    ataque, além de proteger a si mesmo e atacar, deveria também
    proteger seus dois vizinhos (mais próximos) na linha, se tais
    vizinhos existissem (porque o soldado mais a esquerda não possui
    um vizinho mais a esquerda e o soldado mais a direita não possui
    um vizinho mais a direita). O General Chefe também disse aos
    soldados que proteger seus companheiros era muito importante para
    previnir que a linha de ataque fosse quebrada. Tão importante que,
    se o companheiro a esquerda ou a direita de um soldado é morto,
    então o próximo soldado vivo a esquerda ou a direita daquele soldado,
    respectivamente, deveria se tornar seu companheiro.

    A batalha é violenta, e muitos soldados na linha de ataque estão sendo
    mortos por tiros, granadas e bombas. Mas seguindo as ordens do General
    Chefe, imediatamente após tomar conhecimento das baixas na linha de ataque,
    a divisão de sistemas de informação do Exército tem que informar aos soldados
    quem são seus novos companheiros.

    Serão dados o número de soldados na linha de ataque, e uma sequencia de
    relatórios de baixa. Cada relatório de baixa descreve um grupo de soldados
    contíguos na linha de ataque que acabaram de ser mortos na batalha. Escreva
    um programa que, para cada relatório de baixa, imprime os novos companheiros
    formados.

    Entrada
    Cada caso de teste é descrito usando várias linhas. A primeira linha da entrada
    contém dois inteiros S e B representando respectivamente o número de soldados na
    linhas de ataque, e o número de relatórios de baixa (1 ≤ B ≤ S ≤ 10^5). Os soldados
    são identificados por números diferentes de 1 até S, de acordo com usas posições na
    linha de ataque, sendo que 1 o soldado mais a esquerda e S o soldado mais a direita.
    Cada uma da B linhas seguintes descrevem um relatório de perda usando dois inteiros
    L (esquerda) e R (direita), significando que os soldados de L até R foram mortos
    (1 ≤ L ≤ R ≤ S). Você pode assumir que até o momento aqueles soldados estavam vivos
    e acabaram de ser mortos.

    O último caso de teste é seguido por uma linha contendo dois zeros.

    Saída
    Para cada caso de teste imprima B+1 linhas. Na i-ésima linha da saída escreva os novos
    companheiros formados por remover da linha de ataque os soldados que acabaram de ser
    mortos de acordo com o i-ésimo relatório de baixa. Ou seja, para cada relatório de
    baixa 'L R', imprima o primeiro soldado sobrevivente a esquerda de L, e o primeiro soldado
    sobrevivente a direita de R. Para cada direção, imprima o caractere '*' (asterisco) se não
    existe soldado sobrevivente naquela direção. Imprima uma linha contendo um único caractere '-'
    (hifen) após cada caso de teste.
    :return:
    """
    while True:
        s, b = map(int, input().split(" "))
        soldados = []
        if s == b == 0:
            break
        else:
            for i in range(1, s + 1):
                soldados.append(i)
            for i in range(b):
                e, d = map(int, input().split(" "))
                print(soldados)
                for j in range(e - 1, -1, -1):
                    soldados[j] = 0
                for j in range(d, s):
                    soldados[j] = 0
                for j in range():
                    if soldados[j] != 0:
                        print(soldados[j], end=" ")


            print("-")


companheiros_de_exercito()
