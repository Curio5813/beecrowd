def coral_perfeito():
    """
    A Maestrina do coral está planejando o espetáculo que apresentará
    na famosa Semana Brasileira de Corais. Ela pensou em preparar uma
    nova música, definida da seguinte maneira:

    • cada um dos integrantes do coral inicia cantando uma nota, e somente
    muda de nota quando determinado pela Maestrina;

    • ao final de cada compasso, a Maestrina determina que exatamente dois
    integrantes alterem a nota que cantam: um integrante passa a cantar a nota
    imediatamente acima da nota que cantava, e o outro integrante passa a
    cantar a nota imediatamente abaixo da nota que cantava;

    • a música termina ao final do primeiro compasso em que todos os integrantes
    do coral cantam a mesma nota.

    A Maestrina já tem várias ideias de como distribuir as notas no início da música
    entre os integrantes do coral, de forma a criar o efeito desejado. No entanto,
    ela está preocupada em saber se, dada uma distribuição de notas entre os integrantes,
    é possível chegar ao final da música da forma desejada (todos cantando a mesma nota)
    e, caso seja possível, qual o número mínimo de compassos da música. Você pode ajudá-la?

    Entrada
    A primeira linha de um caso de teste contém um inteiro N (2 ≤ N ≤ 104) indicando o número
    de integrantes do coral. As notas serão indicadas por números inteiros. A segunda linha
    contém N números inteiros, indicando as notas iniciais (−105 ≤ notai ≤105), onde 0 ≤ i ≤ N−1,
    que cada integrante deve cantar. As notas são dadas em ordem não decrescente de altura
    (notai ≤notai+1).

    Saída
    Para cada caso de teste imprima uma linha contendo um único número inteiro indicando o número
    mínimo de compassos que a música terá. Se não é possível terminar a música com todos os
    integrantes cantando a mesma nota, imprima o valor−1.
    :return:
    """
    while True:
        try:
            n = int(input())
            cont = 1
            notas = list(map(int, input().split(" ")))
            k, j = 0, len(notas) - 1
            soma = sum(notas)
            unissono = soma // n
            if soma % n == 0:
                while len(set(notas)) > 1:
                    if notas[j] == unissono:
                        j -= 1
                    if notas[k] == unissono:
                        k += 1
                    if k >= j:
                        break
                    notas[k] += 1
                    notas[j] -= 1
                    cont += 1
                print(cont)
            else:
                print(-1)
        except EOFError:
            break


coral_perfeito()
