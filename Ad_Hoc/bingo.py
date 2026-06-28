def bingo():
    """
    Albert, Charles e Mary inventaram uma nova versão do clássico
    jogo de Bingo. Na versão tradicional, o jogo é presidido por
    um não-jogador conhecido como caller. No começo de cada partida,
    cada jogador recebe uma carta contendo uma única combinação de
    números de 0 até N dispostos em colunas e linhas. O caller opera
    um globo contendo N+1 bolas numeradas de 0 até N. Em cada turno,
    o caller sorteia uma bola do globo, anuncia o número sorteado aos
    jogadores e não a coloca novamente no globo. Cada jogador procura
    pelo número em sua carta e o marca caso o encontre. O primeiro jogador
    que marcar um padrão pré-definido completo em sua carta (uma linha
    horizontal, por exemplo) ganha um prêmio.

    Na versão Albert-Charles-Mary, em cada turno, o caller sorteia uma
    primeira bola, coloca-a de volta no globo, sorteia uma segunda bola,
    coloca-a de volta no globo, e então anuncia a diferença absoluta entre
    os números das duas bolas. Para aumentar o entusiasmo, antes do início
    da partida, um subconjunto possivelmente vazio de bolas é retirado do
    globo, de forma que ao menos duas bolas permaneçam no globo. Eles
    gostariam de saber se cada número de 0 até N podem ainda ser anunciados
    utilizando a nova regra de sorteio e considerando apenas as bolas que
    permaneceram dentro do globo.
    Entrada
    Cada caso de teste é dado em exatamente duas linhas. A primeira linha contém
    dois inteiros N e B. O significado de N foi descrito acima (1 ≤ N ≤ 90),
    enquanto B representa o número de bolas que permaneceram no globo (2 ≤ B ≤ N+1).
    A segunda linha contém B inteiros distintos bi, indicando as bolas que permaneceram
    no globo (0 ≤ bi ≤ N). O último caso de teste é seguido por uma linha contendo dois
    zeros.

    Saída
    Para cada caso de teste, imprima uma única linha contendo um único caractere 'Y' se
    for possível anunciar todos os números de 0 até N, inclusive, ou um único caractere
    'N' caso contrário.
    :return:
    """
    n, b = map(int, input().split(" "))
    dif_bolas = []
    numeros = []
    while n != 0 and b != 0:
        bolas = list(map(int, input().split(" ")))
        bolas.sort()
        for i in range(0, n + 1):
            numeros.append(i)
        for i in range(0, len(bolas)):
            for k in range(0, len(bolas)):
                diff = abs(bolas[i] - bolas[k])
                if diff not in dif_bolas:
                    dif_bolas.append(diff)
        for i in range(0, len(numeros)):
            if numeros[i] not in dif_bolas:
                print("N")
                break
        else:
            print("Y")
        n, b = map(int, input().split(" "))
        dif_bolas = []
        numeros = []


bingo()
