from copy import deepcopy


def fila_do_recreio():
    """
    Na escola onde você estuda, a hora do recreio é a mais aguardada
    pela grande maioria dos alunos. Não só porque as vezes as aulas
    são cansativas, mas sim porque a merenda servida é muito boa, preparada
    por um chefe italiano muito caprichoso.

    Quando bate o sinal para a hora do recreio, todos os alunos saem correndo
    da sua sala para chegar o mais cedo possível na cantina, tanta é a
    vontade de comer. Um de seus professores notou, porém, que havia ali uma
    oportunidade.

    Utilizando um sistema de recompensa, seu professor de matemática disse
    que a ordem da fila para se servir será dada não pela ordem de chegada,
    mas sim pela soma das notas obtidas em sala de aula. Assim, aqueles com
    maior nota poderão se servir antes daqueles que tem menor nota.

    Sua tarefa é simples: dada a ordem de chegada dos alunos na cantina, e as
    suas respectivas notas na matéria de matemática, reordene a fila de acordo
    com as notas de matemática, e diga quantos alunos não precisaram trocar
    de lugar nessa reordenação.

    Entrada
    A primeira linha contém um inteiro N, indicando o número de casos de teste a
    seguir.

    Cada caso de teste inicia com um inteiro M (1 ≤ M ≤ 1000), indicando o número
    de alunos. Em seguida haverá M inteiros distintos Pi (1 ≤ Pi ≤ 1000), onde
    o i-ésimo inteiro indica a nota do i-ésimo aluno.

    Os inteiros acima são dados em ordem de chegada, ou seja, o primeiro inteiro
    diz respeito ao primeiro aluno a chegar na fila, o segundo inteiro diz respeito
    ao segundo aluno, e assim sucessivamente.

    Saída
    Para cada caso de teste imprima uma linha, contendo um inteiro, indicando o
    número de alunos que não precisaram trocar de lugar mesmo após a fila ser
    reordenada.
    :return:
    """
    casos = int(input())
    for i in range(casos):
        alunos = int(input())
        notas, n_trocados = [], 0
        notas = list(map(int, input().split()))
        notas_origem = deepcopy(notas)
        for j in range(0, len(notas)):
            for k in range(j + 1, len(notas)):
                if notas[k] > notas[j] and j != k:
                    notas[k], notas[j] = notas[j], notas[k]
        for k in range(0, len(notas)):
            if notas[k] == notas_origem[k]:
                n_trocados += 1
        print(n_trocados)


fila_do_recreio()
