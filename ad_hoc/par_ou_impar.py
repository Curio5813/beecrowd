def par_ou_impar():
    """
    Muitas crianças gostam de decidir todas as disputas através do
    famoso jogo de Par ou Ímpar. Nesse jogo, um dos participantes
    escolhe Par e o outro Ímpar. Após a escolha, os dois jogadores
    mostram, simultaneamente, uma certa quantidade de dedos de uma
    das mãos. Se a soma dos dedos das mãos dos dois jogadores for par,
    vence o jogador que escolheu Par inicialmente, caso contrário
    vence o que escolheu Ímpar.

    Dada uma seqüência de informações sobre partidas de Par ou Ímpar
    (nomes dos jogadores e números que os jogadores escolheram), você
    deve escrever um programa para indicar o vencedor de cada uma das
    partidas.

    Entrada
    A entrada é composta de vários conjuntos de testes. A primeira linha
    de um conjunto de testes contém um inteiro N (0 ≤ N ≤ 1000), que indica
    o número de partidas de Par ou Ímpar que aconteceram. As duas linhas
    seguintes contêm cada uma um nome de jogador. Um nome de jogador é uma
    cadeia de no mínimo um e no máximo dez letras (maiúsculas e minúsculas),
    sem espaços em branco. As N linhas seguintes contêm cada uma dois inteiros
    A e B que representam o número de dedos que cada jogador mostrou em cada
    partida (0 ≤ A ≤ 5 e 0 ≤ B ≤ 5). Em todas as partidas, o primeiro jogador
    sempre escolhe Par. O final da entrada é indicado por N = 0.

    Saída
    Para cada conjunto de teste da entrada, seu programa deve produzir a saída
    da seguinte forma. A primeira linha deve conter um identificador do conjunto
    de teste, no formato “Teste n”, onde n é numerado seqüencialmente a partir de 1.
    As próximas N linhas devem indicar o nome do vencedor de cada partida. A próxima
    linha deve ser deixada em branco. A grafia mostrada no Exemplo de Saída, abaixo,
    deve ser seguida rigorosamente.
    :return:
    """
    n = int(input())
    cont = 1
    while n != 0:
        print(f"Teste {cont}")
        p1 = input()
        p2 = input()
        for i in range(n):
            jogada = list(map(int, input().strip().split(" ")))
            if sum(jogada) % 2 == 0:
                print(p1)
            else:
                print(p2)
        print()
        cont += 1
        n = int(input())


par_ou_impar()


"""
3
Pedro
Paulo
2 4
3 5
1 0
2
Claudio
Carlos
1 5
2 3
0
"""