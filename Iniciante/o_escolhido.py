def main():
    """
    As aulas do Prof. Jatobá estão dando o que falar. Os representantes do MEC
    vieram até a UNIME de Lauro de Freitas para saber mais detalhes sobre essa
    nova forma de ensinar Algoritmos. Além disso, eles queriam selecionar 1 aluno
    para participar da OBI-Tec (Olimpíada Brasileira de Informática Nível Técnica)
    e representar a rede Kroton na competição, pois sabem que lá estão os melhores.
    Para selecionar o melhor, eles têm disponível uma lista com o número de inscrição
    de cada aluno e a sua respectiva nota na disciplina. Sua tarefa é ajudar o
    pessoal do MEC a encontrar o aluno mais apto a representar a instituição e quem
    sabe garantir sua vaga. Só tem um detalhe, se a nota mais alta não for maior ou
    igual a 8, você deverá imprimir “Minimum note not reached”.

    Entrada
    O arquivo contém primeiro a quantidade de alunos (3 <= n <= 100) existentes e em
    seguida, os n alunos contendo o número da matrícula (0 < m < 1000000) de cada um,
    seguido da respectiva nota (0 <= nota <= 10.0, com 1 casa decimal).

    Obs.: as notas não serão repetidas. Ou seja, não tem chance de ter dois alunos com a
    mesma nota.

    Saída
    Você deve imprimir o número do estudante que obteve a maior pontuação ou "Minimum note
    not reached" (sem aspas) caso nenhum estudante tenha tirado uma nota maior ou igual a 8.
    """
    alunos, melhor, matricula = [], 0, 0
    n = int(input())
    for k in range(0, n):
        aluno = input().split()
        alunos.append(aluno)
    for k in range(0, len(alunos)):
        alunos[k][0] = int(alunos[k][0])
        alunos[k][1] = float(alunos[k][1])
    for k in range(0, len(alunos)):
        if k == 0:
            melhor = alunos[0][1]
            matricula = alunos[0][0]
        elif k > 0 and melhor < alunos[k][1]:
            melhor = alunos[k][1]
            matricula = alunos[k][0]
    if melhor >= 8:
        print(matricula)
    else:
        print('Minimum note not reached')


if __name__ == '__main__':
    main()
