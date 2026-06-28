def branco_e_preto():
    """
    O famoso jogo Preto e Branco é um jogo individual que é jogado
    com um conjunto de fichas idênticas. Cada ficha tem duas faces
    com cores diferentes. Surpreendentemente, essas cores são preto
    e branco.

    O jogo começa colocando N fichas formando uma única linha. Existe
    um objetivo que é uma dada sequência de N cores preto ou branco.
    Em um único movimento, o jogador pode escolher um grupo de fichas
    consecutivas e inverter a sua cor, em outras palavras, para cada
    ficha no grupo, a cor que estava voltada para cima, esta voltada
    para baixo, e a que estava voltada para baixo está virada para cima.
    O jogo termina quando as cores voltadas para cima são iguais ao
    objetivo.

    Barby acaba de descobrir este jogo e logo ela percebeu que você pode
    sempre ganhar invertendo cada ficha individualmente, se necessário.
    Para tornar o jogo mais desafiador para ela, ela queria ganhar no menor
    número possível de movimentos. Note que Barby apenas se preocupa com
    quantos movimentos ela faz, e não importa quantas fichas são invertidas
    em cada jogada. Para saber o quão bem Barby está jogando, ela lhe pediu
    para fazer um programa que, dada a posição inicial da ficha e o objetivo,
    mostra o menor número possível de movimentos para ganhar o jogo. Você
    vai dizer que não?

    Entrada
    A entrada contém vários casos de teste. Cada caso de teste é descrito em
    uma única linha que contém duas palavras não vazias S e T de igual tamanho
    e, no máximo, 500 caracteres cada. S indica a posição inicial da ficha, enquanto
    T representa o objetivo. Ambas as palavras contêm apenas letras maiúsculas
    "B" e "N", que representam, respectivamente, branco e preto. A última linha da
    entrada contém dois asteriscos ("*") separados por um espaço único e não deve ser
    processado como um caso de teste.

    Saída
    Para cada caso de teste de saída, imprima uma única linha com um inteiro representando
    a quantidade mínima de jogadas necessárias para passar as fichas da posição inicial S
    para o objetivo T.
    :return:
    """
    while True:
        entrada = input().split(" ")
        s, t = entrada[0], entrada[1]
        move, flag, saida, termino = 0, 0, [], []
        if s == "*" and t == "*":
            break
        for i in s:
            saida.append(i)
        for i in t:
            termino.append(i)
        if saida == termino:
            print(0)
        else:
            i = 0
            while i <= len(saida) - 1:
                # print(i)
                if saida[i] != termino[i]:
                    # print(saida[i])
                    move += 1
                    while saida[i] != termino[i]:
                        i += 1
                        if i >= len(saida) - 1:
                            break
                    if i >= len(saida) - 1:
                        break
                else:
                    i += 1
            if move == 0:
                print(1)
            else:
                print(move)

branco_e_preto()
