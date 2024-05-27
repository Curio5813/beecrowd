def numeros_virados():
    """
    Você acaba de ganhar um baralho com N cartas. Cada uma
    dessas cartas tem dois números escritos: um no lado da
    frente, e outro no lado de trás.

    Seu amigo te desafiou para um jogo. Ele embaralhou as
    cartas do baralho e as colocou numa mesa. As cartas estão
    dispostas em uma linha, uma ao lado da outra, todas com a
    face da frente virada para cima.

    Da esquerda para a direita, você sabe que o número escrito
    na face da frente da i-ésima carta é Ai, e que o número
    escrito na face de trás da i-ésima carta é Bi.

    O jogo é dividido em duas partes.

    Na primeira parte, você deve escolher K cartas do baralho.
    Para escolher uma carta você deve selecionar ou a carta mais à
    esquerda ou a carta mais à direita da mesa e pegá-la para si.

    Em seguida você deve escolher L das cartas que você pegou e virá-las.

    A sua pontuação será igual à soma do número na face da frente de
    todas as K cartas escolhidas, mais a soma do número na face de trás
    de todas as L cartas viradas.

    O desafio? Conseguir a maior pontuação possível, é claro!

    Entrada
    A primeira linha contém um inteiro N (1≤N≤105). A segunda linha contém
    N inteiros A1, A2, ... AN, (1≤Ai≤109). A terceira linha contém N inteiros
    B1, B2, ... BN, (1≤Bi≤109). A quarta linha contém dois inteiros K e L (1≤L≤K≤N).

    Saída
    Imprima uma linha contendo um inteiro, representando a maior pontuação
    possível.
    :return:
    """
    n = int(input())
    cartas_a = list(map(int, input().split(" ")))
    cartas_b = list(map(int, input().split(" ")))
    cont, escolhida, escolhidas, num, maior, soma, maiores = 0, [], [], [], 0, 0, []
    k, lr = map(int, input().split(" "))
    while cont < k:
        cont += 1
        if cartas_a[0] >= cartas_a[-1] and cartas_b[0] >= cartas_b[-1]:
            escolhida.append(cartas_a[0])
            escolhida.append(cartas_b[0])
            escolhidas.append(escolhida)
            escolhida = []
            cartas_a.pop(0)
            cartas_b.pop(0)
        elif cartas_a[0] < cartas_a[-1] and cartas_b[0] < cartas_b[-1]:
            escolhida.append(cartas_a[-1])
            escolhida.append(cartas_b[-1])
            escolhidas.append(escolhida)
            escolhida = []
            cartas_a.pop(-1)
            cartas_b.pop(-1)
        elif (cartas_a[0] >= cartas_a[-1] and cartas_b[0] <= cartas_b[-1]
              and cartas_a[0] + cartas_b[0] >= cartas_a[-1] + cartas_b[-1]):
            escolhida.append(cartas_a[0])
            escolhida.append(cartas_b[0])
            escolhidas.append(escolhida)
            escolhida = []
            cartas_a.pop(0)
            cartas_b.pop(0)
        elif (cartas_a[0] >= cartas_a[-1] and cartas_b[0] <= cartas_b[-1]
              and cartas_a[0] + cartas_b[0] < cartas_a[-1] + cartas_b[-1]):
            escolhida.append(cartas_a[-1])
            escolhida.append(cartas_b[-1])
            escolhidas.append(escolhida)
            escolhida = []
            cartas_a.pop(-1)
            cartas_b.pop(-1)
        elif (cartas_a[0] <= cartas_a[-1] and cartas_b[0] >= cartas_b[-1]
              and cartas_a[0] + cartas_b[0] >= cartas_a[-1] + cartas_b[-1]):
            escolhida.append(cartas_a[0])
            escolhida.append(cartas_b[0])
            escolhidas.append(escolhida)
            escolhida = []
            cartas_a.pop(0)
            cartas_b.pop(0)
        elif (cartas_a[0] <= cartas_a[-1] and cartas_b[0] >= cartas_b[-1]
              and cartas_a[0] + cartas_b[0] < cartas_a[-1] + cartas_b[-1]):
            escolhida.append(cartas_a[-1])
            escolhida.append(cartas_b[-1])
            escolhidas.append(escolhida)
            escolhida = []
            cartas_a.pop(-1)
            cartas_b.pop(-1)
    cont = 0
    # print(escolhidas)
    # print(cartas_a)
    # print(cartas_b)
    for i in range(0, len(escolhidas)):
        if sum(escolhidas[i]) > maior:
            num.append(escolhidas[i][1])
            maior = sum(escolhidas[i])
    num.reverse()
    while cont < lr and len(num) > 0:
        maximo = max(num)
        maiores.append(maximo)
        num.pop(num.index(max(num)))
        cont += 1
    # print(maiores)
    for i in range(0, len(escolhidas)):
        soma += escolhidas[i][0]
    soma += sum(maiores)
    print(soma)


numeros_virados()
