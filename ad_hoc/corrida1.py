def corrida1():
    """
    A escola de Joãozinho tradicionalmente organiza uma corrida ao redor do
    prédio. Como todos os alunos são convidados a participar e eles estudam
    em períodos diferentes, é difícil que todos corram ao mesmo tempo.

    Para contornar esse problema, os professores cronometram o tempo que cada aluno
    demora para dar cada volta ao redor da escola, e depois comparam os tempos para
    descobrir a classificação final.

    Sua tarefa é, sabendo o número de competidores, o número de voltas de que consistiu
    a corrida e os tempos de cada aluno competidor, descobrir quem foi o aluno vencedor,
    para que ele possa receber uma medalha comemorativa.

    No segundo caso de teste abaixo, existem três competidores numa corrida de três voltas.
    Os tempos de cada competidor em cada volta foram como na tabela a seguir.

    (Imagem) https://resources.beecrowd.com/gallery/images/contests/UOJ_171_H.png

    Sendo assim, o vencedor foi o competidor 3 (com um tempo total de 3).

    Entrada
    A primeira linha da entrada contém dois inteiros N (2 ≤ N ≤ 100) e M (1 ≤ M ≤ 100) representando
    o número de competidores e o número de voltas da corrida, respectivamente.

    Cada uma das N linhas seguintes representa um competidor: a primeira linha representa o primeiro
    competidor, a segunda linha representa o segundo competidor, e assim por diante. Cada linha
    contém M inteiros representando os tempos em cada volta da corrida: o primeiro inteiro é o
    tempo da primeira volta, o segundo inteiro é o tempo da segunda volta, e assim por diante
    (1 ≤ qualquer número da entrada que represente o tempo de uma volta ≤ 106).

    Garante-se que não houve dois competidores que gastaram o mesmo tempo para completar a corrida
    inteira.

    Saída
    A saída consiste de um único inteiro, que corresponde ao número do competidor que ganhou a
    corrida.
    :return:
    """
    competidores, voltas = map(int, input().split(" "))
    tempos = []
    for i in range(competidores):
        tempo = list(map(int, input().split(" ")))
        tempos.append(sum(tempo))
    print(tempos.index(min(tempos)) + 1)


corrida1()
