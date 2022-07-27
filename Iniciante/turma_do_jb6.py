def main():
    """
    Dodô, Leo e Pepper passam várias madrugadas conversando, em algum lugar do Condomínio
    Jardim Botânico IV. Diversos assuntos astrais ganham pauta nestas conversas homéricas.
    Nas últimas sessões, Dodô tem falado do jogo de RPG que ele e Leo estão inventando,
    Leo (para “variar”, mas com razão) tem falado do gênero musical heavy metal e Pepper
    ficou fascinado com a história da mitologia grega contada por Leo.

    Os garotos resolveram adotar uma estratégia para dividir as sessões igualmente entre os
    assuntos, de modo que eles possam especular cada um ao máximo e chegarem a conclusões
    astronômicas. Eles irão jogar “pedra, papel e tesoura” para decidir o assunto da sessão
    de hoje, e então irão alternar os assuntos nas próximas sessões. Dadas as jogadas de
    Dodô, Leo e Pepper, nesta ordem, você deve determinar o assunto da sessão de hoje.

    Entrada
    A entrada é composta por vários casos de teste e termina com fim de arquivo. Cada caso
    de teste é composto por uma única linha, que contém as jogadas de cada um dos garotos,
    como mostrado nos exemplos.

    Saída
    Para cada caso de teste, imprima uma única linha com a mensagem "Os atributos dos monstros
    vao ser inteligencia, sabedoria..." para indicar que Dodô é o vencedor, a mensagem
    "Iron Maiden's gonna get you, no matter how far!" para indicar que Leo é o vencedor,
    a mensagem "Urano perdeu algo muito precioso..." para indicar que Pepper é o vencedor,
    ou a mensagem "Putz vei, o Leo ta demorando muito pra jogar..." se houver empate.
    """
    while True:
        assunto = ['Os atributos dos monstros vao ser inteligencia, sabedoria...',
                   "Iron Maiden's gonna get you" + ", " + "no matter how far!",
                   'Urano perdeu algo muito precioso...',
                   'Putz vei, o Leo ta demorando muito pra jogar...'
                   ]
        jogo = ['papel', 'pedra', 'tesoura']
        try:
            jogada = input().split()
        except EOFError:
            break
        else:
            if jogada[0] == jogo[0] and jogada[1] == jogo[0] and jogada[2] == jogo[0]:
                print(assunto[3])
            elif jogada[0] == jogo[0] and jogada[1] == jogo[1] and jogada[2] == jogo[0]:
                print(assunto[3])
            elif jogada[0] == jogo[0] and jogada[1] == jogo[2] and jogada[2] == jogo[0]:
                print(assunto[1])
            elif jogada[0] == jogo[0] and jogada[1] == jogo[0] and jogada[2] == jogo[1]:
                print(assunto[3])
            elif jogada[0] == jogo[0] and jogada[1] == jogo[1] and jogada[2] == jogo[1]:
                print(assunto[0])
            elif jogada[0] == jogo[0] and jogada[1] == jogo[2] and jogada[2] == jogo[1]:
                print(assunto[3])
            elif jogada[0] == jogo[0] and jogada[1] == jogo[0] and jogada[2] == jogo[2]:
                print(assunto[2])
            elif jogada[0] == jogo[0] and jogada[1] == jogo[1] and jogada[2] == jogo[2]:
                print(assunto[3])
            elif jogada[0] == jogo[0] and jogada[1] == jogo[2] and jogada[2] == jogo[2]:
                print(assunto[3])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[0] and jogada[2] == jogo[0]:
                print(assunto[3])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[1] and jogada[2] == jogo[0]:
                print(assunto[2])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[2] and jogada[2] == jogo[0]:
                print(assunto[3])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[0] and jogada[2] == jogo[1]:
                print(assunto[1])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[1] and jogada[2] == jogo[1]:
                print(assunto[3])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[2] and jogada[2] == jogo[1]:
                print(assunto[3])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[0] and jogada[2] == jogo[2]:
                print(assunto[3])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[1] and jogada[2] == jogo[2]:
                print(assunto[3])
            elif jogada[0] == jogo[1] and jogada[1] == jogo[2] and jogada[2] == jogo[2]:
                print(assunto[0])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[0] and jogada[2] == jogo[0]:
                print(assunto[0])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[1] and jogada[2] == jogo[0]:
                print(assunto[3])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[2] and jogada[2] == jogo[0]:
                print(assunto[3])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[0] and jogada[2] == jogo[1]:
                print(assunto[3])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[1] and jogada[2] == jogo[1]:
                print(assunto[3])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[2] and jogada[2] == jogo[1]:
                print(assunto[2])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[0] and jogada[2] == jogo[2]:
                print(assunto[3])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[1] and jogada[2] == jogo[2]:
                print(assunto[1])
            elif jogada[0] == jogo[2] and jogada[1] == jogo[2] and jogada[2] == jogo[2]:
                print(assunto[3])


if __name__ == '__main__':
    main()
