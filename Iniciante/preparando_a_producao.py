def preparando_a_producao():
    """
    Uma montadora de carros, permite que os usuários criem seus próprios
    projetos de veículos da maneira que desejar e ainda compartilhar tais
    informações com outros usuários com o intuito de criar uma rede de
    utilizadores bem diversificada. O processo se inicia com o cliente
    desenvolvendo seu próprio modelo através de um software, logo após a
    conclusão, os dados do projeto são armazenados e de acordo com a
    disponibilidade da montadora vão sendo realizados.

    Porém uma falha na entrega das peças para a montadora está atrasando os
    pedidos. Acontece que as peças são entregues em pacotes, etiquetados com um
    número, que deveriam estar ordenados de forma crescente para que a produção
    inicie. A falha é que os pacotes estão sendo entregues de uma forma aleatória.
    Você deve criar um programa em que dados a ordem de entrega dos pacotes e o
    tempo que cada um deles leva para ser trocado de posição, calcule o tempo total
    para organizar os pacotes. Sabe-se que para efeito de organização dentro da empresa,
    os pacotes devem ser trocados de posição somente dois a dois e se estiverem um do
    lado do outro.
    Entrada

    A entrada consiste de vários casos de testes, lidos até EOF. Para cada caso, o primeiro
    valor da entrada é um inteiro N (1 <= N <= 1000) representando a quantidade de pacotes,
    logo após haverá duas linhas com N inteiros cada, com os números dos pacotes, na ordem
    da entrega, e o tempo, em segundos, que o n-ésimo pacote leva para ser trocado de lugar,
    respectivamente.

    É garantido que os números dos pacotes para cada caso de teste forma uma permutação dos
    inteiros de 1 a N, e que nenhum pacote demora mais do que um minuto para mover.
    Saída

    Seu programa deve apresentar, para cada caso de teste, um único inteiro que representa o tempo
    total para organizar os pacotes.

    :return:
    """
    while True:
        try:
            n = int(input())
            pecas = list(map(int, input().split()))
            tempo = list(map(int, input().split()))
            total_tempo = 0
            trocas = 0
            for i in range(n):
                trocou = False
                for j in range(n):
                    if j >= len(pecas) - 1:
                        break
                    if pecas[j] > pecas[j + 1]:
                        pecas[j], pecas[j + 1] = pecas[j + 1], pecas[j]
                        tempo[j], tempo[j + 1] = tempo[j + 1], tempo[j]
                        total_tempo += tempo[j] + tempo[j + 1]
                        trocou = True
                        # print(tempo[j], tempo[j + 1], total_tempo)
                if not trocou:
                    break
            print(total_tempo)
        except EOFError:
            break
    

preparando_a_producao()

"""
5
3 1 2 5 4
10 23 15 18 30
3
3 2 1
1 1 1
"""