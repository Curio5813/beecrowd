from collections import Counter
from traceback import print_tb


def meu_avo_e_famoso():
    """
    A família toda ficou excitada pela novidade. Todos sabiam que o meu avô
    tinha sido um excelente jogador de bridge por décadas, mas quando foi anunciado
    que ele estaria no Guinness Book, o livro dos recordes, como o jogador de bridge
    de maior sucesso de todos os tempos, wow, aquilo foi surpreendente.

    A Associação Internacional de Bridge (AIB) tem mantido, por diversos anos, um ranking
    semanal dos melhores jogadores do mundo. Considerando que cada aparição em um ranking
    semanal constitui um ponto para o jogador, meu avô foi nominado o melhor jogador de
    todos os tempos porque ele conseguiu o maior número de pontos.

    Tendo muitos amigos que também estavam competindo com ele, meu avô está extremamente
    curioso para saber que jogador(es) ficou(aram) com o segundo lugar. Ele precisa de um
    programa, o qual, dada uma lista com os ranking semanais, descubra que jogador(es)
    ficou(aram) com o segundo lugar, de acordo com o número de pontos.

    Entrada
    A entrada contém diversos casos de teste. Jogadores são identificados por inteiros
    de 1 a 10000. A primeira linha de um caso de teste contém dois inteiros N e M, indicando,
    respectivamente, o número de rankings disponíveis (2 ≤ N ≤ 500) e o número de jogadores
    em cada ranking (2 ≤ M ≤ 500). Cada uma das próximas N linhas contém a descrição de um
    ranking semanal. Cada descrição é composta por uma sequência de M inteiros, separados
    por um espaço em branco, identificando os jogadores que apareceram naquele ranking semanal.
    Você pode assumir que:

    em cada caso de teste há exatamente um melhor jogador e ao menos um segundo melhor jogador,
    cada ranking semanal consiste de M jogadores distintos.
    O final da entrada é indicado por N = M = 0.

    Saída
    Para cada caso de teste da entrada seu programa deve produzir uma linha de saída, contendo
    o identificador do jogador que é o segundo melhor, em número de aparições nos rankings. Se
    há um empate para segundo lugar, imprima os identificadores de todos os segundo colocados,
    em ordem crescente. Cada identificador produzido deve ser seguido por um espaço em branco.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, m = entrada[0], entrada[1]
    while n != 0 and m != 0:
        raking = []
        for i in range(n):
            ranking_semanal = list(map(int, input().strip().split(" ")))
            raking.extend(ranking_semanal)
        contagem  = dict(sorted(Counter(raking).items(), key=lambda item: item[1], reverse=True))
        primeiro = max(contagem.values())
        segundo, segundos, cont = 0, [], 0
        for chave, valor in contagem.items():
            if valor < primeiro and cont == 0:
                segundo = valor
                cont += 1
            if valor < primeiro and valor == segundo:
                segundos.append(chave)
        segundos.sort()
        for i in range(0, len(segundos)):
            if i >= len(segundos) - 1:
                print(f"{segundos[i]} ")
                break
            print(segundos[i], end=" ")
        entrada = list(map(int, input().strip().split(" ")))
        n, m = entrada[0], entrada[1]


meu_avo_e_famoso()
