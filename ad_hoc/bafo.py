def bafo():
    """
    Álbuns de figurinhas – sejam de times de futebol, princesas ou
    super-heróis – têm marcado gerações de crianças e adolescentes.
    Conseguir completar um álbum é uma tarefa muitas vezes árdua,
    envolvendo negociações com colegas para a troca de figurinhas.
    Mas a existência das figurinhas propicia uma outra brincadeira,
    que foi muito popular entre crianças no século passado: o jogo de
    bater figurinhas (o famoso “Bafo”). O jogo é muito simples, mas
    divertido (e muito competitivo). No início de uma partida, cada
    criança coloca em uma pilha um certo número de figurinhas. Uma
    partida é composta de rodadas; a cada rodada as crianças batem
    com a mão sobre a pilha de figurinhas, tentando virá-las com o
    vácuo formado pelo movimento da mão. As crianças jogam em turnos,
    até que a pilha de figurinhas esteja vazia. Ganha a partida a criança
    que conseguir virar mais figurinhas.

    Aldo e Beto estão jogando bafo com todas as suas figurinhas e pediram
    sua ajuda para calcular quem é o vencedor.

    Você deve escrever um programa que, dada a quantidade de figurinhas que
    Aldo e Beto viraram em cada rodada, determine qual dos dois é o vencedor.

    Entrada
    A entrada é composta de vários casos de teste, cada um correspondendo a uma
    partida entre Aldo e Beto. A primeira linha de um caso de teste contém um
    número inteiro R (1 ≤ R ≤ 1000) que indica quantas rodadas ocorreram na
    partida. Cada uma das R linhas seguintes contém dois inteiros, A e B
    (0 ≤ A, B ≤ 100), que correspondem, respectivamente, ao número de figurinhas
     que Aldo e Beto conseguiram virar naquela rodada. Em todos os casos de teste
     há um único vencedor (ou seja, não ocorre empate). O final da entrada é indicado
     por R = 0.

    Saída
    Para cada caso de teste da entrada, seu programa deve produzir três linhas na saída.
    A primeira linha deve conter um identificador do caso de teste, no formato “Teste n”,
    onde n é numerado seqüencialmente a partir de 1. A segunda linha deve conter o nome
    do vencedor (Aldo ou Beto). A terceira linha deve ser deixada em branco. A grafia
    mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.
    :return:
    """
    cont = 1
    while True:
        r = int(input())
        aldo, beto = 0, 0
        if r == 0:
            break
        else:
            for i in range(r):
                a, b = map(int, input().split(" "))
                aldo += a
                beto += b
        print(f"Teste {cont}")
        if aldo > beto:
            print("Aldo")
        else:
            print("Beto")
        print("")
        cont += 1


bafo()
