def reinauguracao_do_cei():
    """
    Para comemorar a reinauguração do espaço físico do Clube de Espanhóis
    Inteligentes (CEI), uma grande festa está acontecendo no clube neste
    exato momento!

    Mateuz é um integrante do CEI que está ajudando na organização da festa.
    Sempre que um convidado chega ou vai embora da festa, Mateuz anota em um
    papel quantos minutos se passaram desde o início da festa até aquele momento.

    Mateuz acabou de repassar os números anotados para os presidentes do CEI,
    Freitaz e Rodriguez. Note que os presidentes têm apenas os minutos em que
    convidados entraram e sairam da festa. Desta forma, para cada minuto recebido,
    Freitaz e Rodriguez não sabem se o convidado estava entrando ou saindo naquele
    momento. Sabe-se apenas que: a festa começou sem convidados; até este exato
    momento, nenhum convidado entrou na festa mais de uma vez; e, neste exato
    momento, não há convidados na festa, isto é, todos os convidados foram embora
    (pois foram participar de uma competição de programação, mas pretendem voltar
    à festa depois). Os números anotados também são todos distintos entre si, mas
    não são dados necessariamente em ordem.

    Sua tarefa é ajudar Freitaz e Rodriguez a determinar qual o maior número possível
    de convidados que podem ter estado na festa simultaneamente em algum momento.
    Determine também a quantidade máxima de minutos que esta quantidade de convidados
    pode ter estado na festa simultaneamente.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de cada caso contém um inteiro
    N (2 ≤ N ≤ 1000), a quantidade de números anotados. A segunda linha contém N inteiros
    distintos m1,m2,...,mN, os números anotados por Mateuz e recebidos por Freitaz e Rodriguez.
    Para cada 1 ≤ i ≤ N, o número mi (1 ≤ mi ≤ 104) indica que um convidado entrou ou saiu
    da festa mi minutos após seu início.

    A entrada termina com fim-de-arquivo (EOF).

    Saída
    Para cada caso de teste, imprima uma linha com dois inteiros separados por um espaço. O
    primeiro é o maior número possível de convidados que podem ter estado na festa
    simultaneamente. O segundo é a quantidade de máxima de minutos que esta quantidade de
    convidados pode ter estado simultaneamente na festa.
    :return:
    """
    while True:
        try:
            entrada = input().strip()
            n = int(entrada)
            tempo, simultaneo = [], 0
            festa = list(map(int, input().strip().split(" ")))
            for i in range(0, len(festa)):
                festa[i] = int(festa[i])
            festa.sort()
            simultaneo = len(festa) // 2
            for i in range(simultaneo):
                j = n - 1 - i
                tempo.append(festa[j] - festa[i])
            tempo.sort()
            print(simultaneo, tempo[0])
        except EOFError:
            break


reinauguracao_do_cei()
