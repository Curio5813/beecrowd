def main():
    from statistics import mean
    """
    Sabe-se que 90% dos calouros tem sempre a expectativa de serem acima da média
    no início de suas graduações. Você deve checar a realidade para ver se isso procede.

    Entrada
    A entrada contém muitos casos de teste. A primeira linha da entrada contém um inteiro C,
    indicando o número de casos de teste. Seguem C casos de teste ou instâncias. Cada caso
    de teste inicia com um inteiro N, que é o número de pessoas de uma turma (1 ≤ N ≤ 1000).
    Seguem N inteiros, separados por espaços, cada um indicando a média final (um inteiro
    entre 0 e 100) de cada um dos estudantes desta turma.

    Saída
    Para cada caso de teste imprima uma linha dando o percentual de estudantes que estão
    acima da média da turma, com o valor arredondado e com 3 casas decimais.
    """
    c = int(input())
    for k in range(c):
        cont = 0
        scores = [int(x) for x in input().split()]
        students = scores[0]
        scores.pop(0)
        media = mean(scores)
        for i in range(0, len(scores)):
            if scores[i] > media:
                cont += 1
        acima_media = (cont / students) * 100
        print(f'{acima_media:.3f}%')


if __name__ == '__main__':
    main()
