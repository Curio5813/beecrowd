def wertyu():
    """
    Um erro comum de digitação é colocar as mãos no teclado uma
    posição à direita da correta posição. Desta forma, "Q" é
    digitado como "W" e "J" é digitado como "K" e assim por
    diante. Você deve decodificar a mensagem desta maneira.

    Entrada
    A entrada consiste em várias linhas de texto. Cada linha
    pode conter dígitos, espaços e letras maiúsculas. (exceto Q, A, Z),
    ou pontuação, exceto crase (`) conforme mostrado acima.
    Teclas rotuladas como palavras [Tab, BackSp, Control, etc.]
    não são representados na entrada. Você deverá repassar cada
    letra ou símbolo de pontuação pelo símbolo imediatamente à esquerda.
    Os espaços de entrada simplesmente deverão ser ecoados (impressos)
    na saída.

    Saída
    Para cada linha de entrada, imprima uma linha de saída correspondente
    com a mensagem decodificada.
    :return:
    """
    teclado = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
    while True:
        try:
            frase = input()
            for i in range(0, len(frase)):
                if i == len(frase) - 1:
                    if frase[i] == " ":
                        print(" ")
                        break
                    else:
                        print(teclado[teclado.index(frase[i]) - 1])
                        break
                if frase[i] == " ":
                    print(" ", end="")
                else:
                    print(teclado[teclado.index(frase[i]) - 1], end="")
        except EOFError:
            break


wertyu()
